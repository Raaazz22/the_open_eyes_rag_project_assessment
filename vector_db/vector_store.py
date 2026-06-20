from langchain_chroma import Chroma
from embedding.embeddings import embedder

def vector_store():
    ## Vector Store
    embeddings = embedder()
    vector_store = Chroma(
        collection_name="my_docs",
        persist_directory="./chroma_db",
        embedding_function=embeddings,
    )
    return vector_store


def retreive_chunks(query):
    vs = vector_store()
    retriever = vs.as_retriever(
            search_kwargs={"k": 10}
        )   
    results = retriever.invoke(query)
    return results