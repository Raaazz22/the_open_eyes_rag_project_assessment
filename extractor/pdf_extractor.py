from langchain_community.document_loaders import PyPDFLoader

def pdf_extractor(file_path, file_name):
    try:
        loader = PyPDFLoader(file_path)
        return loader.load()

    except Exception as e:
        return None