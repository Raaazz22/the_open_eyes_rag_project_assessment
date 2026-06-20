from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
load_dotenv()
import streamlit as st

groq_api_key = st.secrets["GROQ_API_KEY"]

def llm_client():
    return ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=groq_api_key
)

