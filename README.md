
# ObjectBox VectorStore with LLama3 Demo

This project demonstrates the use of ObjectBox VectorStore database with LLama3 for document retrieval and question answering.

## Description

This Streamlit application allows users to load PDF documents, embed them into an ObjectBox vector database, and then query the documents using natural language. The application uses LLama3 (via Groq) for generating responses and OpenAI's embeddings for document vectorization.

## Features

- PDF document loading from a specified directory
- Document chunking and embedding
- Vector storage using ObjectBox
- Question answering using LLama3 model
- Similarity search display for context

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/objectbox-vectorstore-llama3-demo.git
   cd objectbox-vectorstore-llama3-demo
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   Create a `.env` file in the project root and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   GROQ_API_KEY=your_groq_api_key
   ```

## Usage

1. Place your PDF documents in the `./us_census` directory.

2. Run the Streamlit app:
   ```
   streamlit run objectbox_vectorstore_demo.py
   ```

3. In the web interface:
   - Click "Documents Embedding" to process and embed the documents.
   - Enter your question in the text input field.
   - View the answer and related document chunks.

## Dependencies

- streamlit
- langchain-groq
- langchain-openai
- langchain-core
- langchain-objectbox
- langchain-community
- python-dotenv
- pypdf

## Note

Ensure you have the necessary API keys for OpenAI and Groq services. The application uses the Llama3-8b-8192 model via Groq.

## License

[MIT License](LICENSE)

