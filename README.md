
# DocQuery-Assistant-Using-LLM-and-Pinecone-DB

## Overview
The DocQuery Assistant System leverages the power of Google Generative AI and Pinecone vector database to provide a robust platform for answering questions directly from uploaded PDF documents. Built with Streamlit, this application combines advanced AI techniques to extract text, generate embeddings, and perform semantic searches to retrieve relevant answers.

## Features
- **PDF Upload**: Users can upload their PDF documents directly through the UI.
- **Text Extraction**: Automatically extracts text from the uploaded PDF documents.
- **Question Answering**: Users can query any text extracted from the document, and the system provides relevant answers using AI.
- **AI Integration**: Incorporates Google's Generative AI for processing and Pinecone for indexing and retrieval.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.10 or higher
- pip (Python package installer)

## Installation
To install the PDF Document Q&A System, follow these steps:

1. Clone the repository:
   ```bash
   https://github.com/zerocool-11/DocQuery-Assistant-Using-LLM-and-Pinecone-DB.git
   cd DocQuery-Assistant-Using-LLM-and-Pinecone-DB/
   ```

2. Install the required packages:
   ```bash
   pip install -r req.txt
   ```

## Usage
To run the PDF Document Q&A System, execute the following command:

```bash
streamlit run app.py
```

Navigate to `http://localhost:8501` in your web browser to view the application.

## Configuration
You need to set up the following environment variables:

- `PINECONE_API_KEY`: Your Pinecone API key.
- `GOOGLE_GENAI_KEY`: Your Google Generative AI API key (if applicable).

These can be set in a `.env` file in the root directory of your project:

```plaintext
PINECONE_API_KEY='your-pinecone-api-key'
GOOGLE_API_KEY='your-google-genai-key'
```


## Contact
Yash Kumar – [@zeroday1202](https://x.com/zeroday1202) – zeroday1202@gmail.com


## Acknowledgments
- Google Generative AI for their powerful model APIs.
- Pinecone for providing a scalable vector database.
- Streamlit for enabling rapid application development.
