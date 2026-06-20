from langchain_core.documents import Document

def text_extractor(file_path,file_name):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    return [
        Document(
            page_content=text,
            metadata={"file_name": file_name}
        )
    ]

# docs = text_extractor("sample.txt","abc")

# print(docs)