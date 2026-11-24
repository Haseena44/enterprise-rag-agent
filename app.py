import streamlit as st
from rag import create_vector_db
from agent import EnterpriseAgent

st.title("Enterprise RAG Agent")
st.write("Upload PDF, Ask Any Question")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")
if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    if st.button("Train AI"):
        db = create_vector_db("temp.pdf")
        st.session_state.agent = EnterpriseAgent(db)
        st.success("AI Ready!")

if "agent" in st.session_state:
    question = st.text_input("Ask Your Question:")
    if question:
        st.markdown(st.session_state.agent.run(question))
