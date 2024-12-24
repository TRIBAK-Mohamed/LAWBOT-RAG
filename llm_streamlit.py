import streamlit as st
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
from langchain_community.vectorstores import Chroma

# Configuration globale
EMBEDDING_MODEL = "mxbai-embed-large:latest"
CHAT_MODEL = "llama3.2"
VECTOR_STORE_DIRECTORY = "./lawbot_DB"
VECTOR_STORE_COLLECTION = "rag-chroma"

def initialize_vector_store():
    """Initialize the Chroma vector store for retrieval."""
    return Chroma(
        persist_directory=VECTOR_STORE_DIRECTORY,
        embedding_function=OllamaEmbeddings(model=EMBEDDING_MODEL),
        collection_name=VECTOR_STORE_COLLECTION,
    )

def retrieve_from_db(question):
    """Retrieve answers from the vector store using a question."""
    db = initialize_vector_store()
    retriever = db.similarity_search(question, k=2)
    after_rag_template = """Answer the question based only on the following context:
    {context}
    Question: {question}
    If there is no answer, respond with: "I'm sorry, the context is not sufficient to answer the question."
    """
    after_rag_prompt = ChatPromptTemplate.from_template(after_rag_template)
    model = ChatOllama(model=CHAT_MODEL)
    after_rag_chain = (
        {"context": RunnablePassthrough(), "question": RunnablePassthrough()}
        | after_rag_prompt
        | model
        | StrOutputParser()
    )
    return after_rag_chain.invoke({"context": retriever, "question": question})

def process_uploaded_file(file):
    """Process an uploaded PDF file and return its text."""
    with pdfplumber.open(file) as pdf:
        return "".join([page.extract_text() for page in pdf.pages])

# Streamlit Interface
st.title("LawBot")
st.write("This is a chatbot for Moroccan family law and other legal contexts. Upload a file or ask directly.")

# Session history
if "history" not in st.session_state:
    st.session_state["history"] = []

# File Upload
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    doc_text = process_uploaded_file(uploaded_file)
    question = st.text_input("Ask a question about the uploaded document:")
    if st.button("Ask"):
        answer = retrieve_from_db(question)
        st.session_state["history"].append({"question": question, "answer": answer})
        st.write(answer)
else:
    question = st.text_input("Ask a general question:")
    if st.button("Ask"):
        answer = retrieve_from_db(question)
        st.session_state["history"].append({"question": question, "answer": answer})
        st.write(answer)

# Display conversation history
if st.session_state["history"]:
    st.write("### Conversation History")
    for i, interaction in enumerate(st.session_state["history"]):
        st.write(f"**Q{i+1}:** {interaction['question']}")
        st.write(f"**A{i+1}:** {interaction['answer']}")
