from ingestion_pipeline import ingest_document
from rag_pipeline import rag_pipeline
import streamlit as st
import os

st.set_page_config(
    page_title="QA Assistant",
    layout="wide"
)

page = st.sidebar.radio(
    "Menu",
    [ "Document Ingestion","QA Assistant"]
)


if page == "Document Ingestion":

    st.title("Document Ingestion")

    uploaded_file = st.file_uploader(
        "Upload Document",
        type=["pdf", "docx", "txt"]
    )

    if uploaded_file is not None:

        temp_file = f"{uploaded_file.name}"

        try:
            with open(temp_file, "wb") as f:
                f.write(uploaded_file.getbuffer())

            if st.button("Ingest Document"):

                with st.spinner("Processing document..."):
                    result = ingest_document(temp_file)

                st.success("Document ingested successfully!")
                st.header("Document contains following rules")
                st.markdown(result["rules"])
                

        except FileNotFoundError:
            st.error("The uploaded file could not be found.")

        except PermissionError:
            st.error("Permission denied while accessing the file.")

        except ValueError as e:
            st.error(f"Invalid document: {e}")

        except Exception as e:
            st.error(f"Error during document ingestion: {str(e)}")

        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)


elif page == "QA Assistant":

    st.title("QA Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

 
    for msg in st.session_state.messages:

        with st.chat_message("user"):
            st.write(msg["user_message"])

        with st.chat_message("assistant"):
            st.write(msg["ai_response"])

    # Last 3 conversations
    history = st.session_state.messages[-3:]

    user_input = st.chat_input("Ask something...")

    if user_input:

        with st.chat_message("user"):
            st.write(user_input)

        try:

            with st.spinner("Generating answer..."):
                ai_response = rag_pipeline(
                    user_input,
                    history
                )

            with st.chat_message("assistant"):
                st.write(ai_response)

            st.session_state.messages.append(
                {
                    "user_message": user_input,
                    "ai_response": ai_response
                }
            )

        except FileNotFoundError as e:
            st.error(str(e))

        except ValueError as e:
            st.error(f"Input Error: {e}")

        except Exception as e:
            st.error(f"Error generating response: {str(e)}")
            