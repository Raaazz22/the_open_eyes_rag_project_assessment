from pathlib import Path
from extractor.pdf_extractor import pdf_extractor
from extractor.word_extractor import word_extractor
from extractor.text_extractor import text_extractor
from langgraph.graph import StateGraph,START,END,message
from langchain_text_splitters import RecursiveCharacterTextSplitter
from vector_db.vector_store import vector_store
from extract_rules import extract_rules



def ingest_document(file_path):

    file_type = Path(file_path).suffix.lower()
    file_name = Path(file_path).name
    print(file_type)
    docs = []
    if file_type == ".pdf":
        docs = pdf_extractor(file_path,file_name)
    elif file_type == ".docx":
        docs = word_extractor(file_path,file_name)
    elif file_type == ".txt":
        docs = text_extractor(file_path,file_name)


    #chunking
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    chunks = text_splitter.create_documents([page.page_content for page in docs])
    print("Total Chunks :",len(chunks))

    #vector store
    vs = vector_store()
    vs.add_documents(docs)

    #extract rules
    rules = extract_rules(docs)
    
    return {
        "Status" : "Success",
        "Total Doc" : len(docs),
        "Total Chunk" : len(chunks),
        "rules" : rules
    }