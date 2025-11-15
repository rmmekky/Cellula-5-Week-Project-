# app_streamlit.py
import streamlit as st
from graph_runner import build_graph, retriever
import glob

st.title("LangGraph + HuggingFace Python Code Assistant 🤖")

query = st.text_area("Ask your question (generate code OR explain):")

if st.button("Run"):
    # Build retriever index from example files if empty
    if not getattr(retriever, "index", None):
        docs = []
        for p in glob.glob("examples/*.txt"):
            with open(p, "r") as f:
                docs.append({"id": p, "text": f.read()})
        retriever.build(docs)

    # Build and run graph
    graph = build_graph()
    state = {"query": query}
    graph.run("input_node", state)

    st.subheader("Response")
    st.code(state.get("answer", "No answer generated"))
