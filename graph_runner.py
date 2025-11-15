# graph_runner.py
import sys
import os
sys.path.append(os.path.dirname(__file__))

from langgraph import Graph
from intent_classifier import classify_intent
from llm_client_hf import call_huggingface
from retriever import CodeRetriever

retriever = CodeRetriever()

# --- Node functions ---
def node_input(state):
    return {"next": "intent_node"}

def node_intent(state):
    intent = classify_intent(state["query"])
    state["intent"] = intent
    return {"next": "retrieve_node"}

def node_retrieve(state):
    docs = retriever.retrieve(state["query"], k=5)
    state["docs"] = docs
    return {"next": "compose_node"}

def node_compose_prompt(state):
    docs_text = "\n\n".join(state["docs"])

    if state["intent"] == "generate":
        prompt = f"""
You are a Python coding assistant.

User request:
{state['query']}

Useful examples:
{docs_text}

Generate clean, correct Python code.
"""
    else:
        prompt = f"""
Explain the following Python concept clearly:

Question:
{state['query']}

Useful references:
{docs_text}
"""
    state["prompt"] = prompt
    return {"next": "llm_node"}

def node_llm(state):
    state["answer"] = call_huggingface(state["prompt"])
    return {"next": "final_node"}

def node_final(state):
    return {"done": True}

# --- Build graph ---
def build_graph():
    g = Graph()

    g.add_node("input_node", node_input)
    g.add_node("intent_node", node_intent)
    g.add_node("retrieve_node", node_retrieve)
    g.add_node("compose_node", node_compose_prompt)
    g.add_node("llm_node", node_llm)
    g.add_node("final_node", node_final)

    return g
