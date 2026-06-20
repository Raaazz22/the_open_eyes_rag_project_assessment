from llm_service.llm_client import llm_client
from langchain_core.messages import SystemMessage, HumanMessage

def extract_rules(extracted_text):
    
    llm = llm_client()

    with open("prompts/rules_prompt.txt", "r", encoding="utf-8") as f:
        prompt = f.read()

    response = llm.invoke(
    [
        SystemMessage(content=prompt),
        HumanMessage(content=f" Document text : {extracted_text}")
    ]
    )
    return response.content

   
