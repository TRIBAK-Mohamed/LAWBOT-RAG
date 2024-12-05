import os
import pdfplumber
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document

# Configuration globale
PDF_DIRECTORY = "./documents"
VECTOR_STORE_DIRECTORY = "./lawbot_DB"
VECTOR_STORE_COLLECTION = "rag-chroma"
EMBEDDING_MODEL = "mxbai-embed-large:latest"

def read_pdf(file_path):
    """Extract text from a PDF file."""
    with pdfplumber.open(file_path) as pdf:
        return "".join([page.extract_text() for page in pdf.pages])

def load_documents_from_directory(directory_path):
    """Load PDF documents from a specified directory."""
    return [
        Document(page_content=read_pdf(os.path.join(directory_path, file)))
        for file in os.listdir(directory_path)
        if file.endswith(".pdf")
    ]

def split_documents(documents, chunk_size=2000, chunk_overlap=200):
    """Split documents into smaller chunks for vector storage."""
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap, separator="."
    )
    return text_splitter.split_documents(documents)

def ingest_into_vector_store(documents):
    """Ingest documents into the Chroma vector store."""
    doc_splits = split_documents(documents)
    db = Chroma(
        persist_directory=VECTOR_STORE_DIRECTORY,
        embedding_function=OllamaEmbeddings(model=EMBEDDING_MODEL),
        collection_name=VECTOR_STORE_COLLECTION,
    )
    db.add_documents(doc_splits)
    db.persist()
    print("Documents successfully ingested into vector store.")

def initialize_vector_store():
    """Initialize the Chroma vector store for retrieval."""
    return Chroma(
        persist_directory=VECTOR_STORE_DIRECTORY,
        embedding_function=OllamaEmbeddings(model=EMBEDDING_MODEL),
        collection_name=VECTOR_STORE_COLLECTION,
    )

def main():
    documents = load_documents_from_directory(PDF_DIRECTORY)
    if documents:
        ingest_into_vector_store(documents)
    else:
        print("No PDF files found in the specified directory.")

if __name__ == "__main__":
    main()
