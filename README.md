# Cellula-5-Week-Project-
# 🤖 LangGraph Powered Python Code Assistant  
A smart, modular, and production-ready Python assistant built using **LangGraph**, **RAG**, **LLMs**, and **Vector Databases**, with full deployment and presentation.

---

## 📌 **Project Overview**
This project implements an intelligent Python code assistant capable of:

- Understanding user intent (code generation or code explanation).
- Retrieving relevant coding examples using **Retrieval Augmented Generation (RAG)**.
- Calling an external **LLM API** (OpenRouter / HuggingFace) to produce high-quality Python code.
- Running all logic through a clean **LangGraph state machine**.
- Providing continuous conversational interaction.
 

This project includes **three major tasks**:

1. **Task 0:** Build a LangGraph-powered smart assistant.  
2. **Task 1:** Merge tasks from weeks 3, 4, and 5 into one deployable system.  


---

# 🧭 **Task 0 — LangGraph Powered Code Assistant**

### ✅ **1. State Machine Design**
- Implement `StateGraph` from LangGraph to define system behavior.
- Build a clear state flow:
  - `idle → intent_detected → retrieve → call_llm → respond → idle`
- Avoid conditional branching—use actions/functions inside graph instead.

### 🧠 **2. Retrieval Augmented Generation (RAG)**
- Use **Sentence Transformers** to embed code descriptions.
- Store embeddings in **FAISS** or **ChromaDB**.
- Retrieve semantically similar examples as context for the LLM.

### 🔍 **3. Intent Classification (Routing)**
- Lightweight keyword-based classifier:
  - “generate”, “create”, “write” → code generation  
  - “explain”, “describe”, “what does this do” → explanation  
- Determines the path in the LangGraph state machine.

### 🤖 **4. LLM API Integration**
- Call open-source models from:
  - **OpenRouter**
  - **HuggingFace**
- Build strong prompt templates to guide model behavior.

### 💬 **5. Conversational Agent**
- Continuous loop that:
  - Accepts input  
  - Finds intent  
  - Retrieves examples  
  - Calls LLM  
  - Returns final answer  

---

# 🧩 **Task 1 — Combined System Deployment**

After finishing all projects from **Weeks 3, 4, and 5**, combine them into a single functioning system that includes:

- The LangGraph assistant
- RAG + embeddings + FAISS
- LLM client
- Conversation loop
- API or UI layer

### 🌐 **Deployment (Choose One)**

### 🔸 **1. Streamlit**
Simple frontend for testing and demo:
