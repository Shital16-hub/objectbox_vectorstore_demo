import os

import streamlit as st
from dotenv import load_dotenv
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_objectbox.vectorstores import ObjectBox

load_dotenv()

# load groq API key
groq_api_key = os.getenv("GROQ_API_KEY")

st.title("Objectbox VectorstoreDB With Llama3 Demo")

llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama-8b-8192")

prompt = ChatPromptTemplate.from_template(
    """
     Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question
    <context>
    {context}
    <context>
    Questions:{input}

    """
)


def vector_embedding():

    if "vectors" not in st.session_state:
        st.session_state.embeddings = OllamaEmbeddings()
        st.session_state.loader = PyPDFDirectoryLoader("./us_census")
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200
        )
        st.session_state.final_document = (
            st.session_state.text_splitter.split_documents(st.session_state.docs[:20])
        )
        st.session_state.vectors = ObjectBox.from_documents(
            st.session_state.final_document,
            st.session_state.embeddings,
            embedding_dimensions=768,
        )


input_prompt = st.text_input("Enter your question from document")

if st.button("Documents Embedding"):
    vector_embedding()
    st.write("Objectbox Dataset is ready.")

import time

if input_prompt:
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriver = st.session_state.vectors.as_retriever()
    retriver_chain = create_retrieval_chain(retriver, document_chain)
    start = time.process_time()

    response = retriver_chain.invoke({"input": input_prompt})

    print("Response time :", time.process_time() - start)
    st.write(response["answer"])

    # With a streamlit expander
    with st.expander("Document Similarity Search"):
        # Find the relevant chunks
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("--------------------------------")