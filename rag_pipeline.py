from llm_service.llm_client import llm_client
from vector_db.vector_store import retreive_chunks
from langchain_core.messages import SystemMessage, HumanMessage


def rag_pipeline(query: str,history:str):

    #retreive chunks
    results = retreive_chunks(query)

    context = [doc.page_content for doc in results]
    metadata = [doc.metadata for doc in results]

    #Prompt
    # Read prompt from txt file
    with open("prompts/qa_prompt.txt", "r", encoding="utf-8") as f:
        prompt = f.read()
    
    assembled_system_prompt =  f"{prompt} . Retreived Document Context :  {context} , Metadata  : {metadata} , Chat Histroy : {history}"

    #call LLM
    llm = llm_client()
    response = llm.invoke(
    [
        SystemMessage(content=assembled_system_prompt),
        HumanMessage(content=query)
    ]
    )

    return response.content



    






