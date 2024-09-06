from dotenv import load_dotenv
import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.chains.question_answering import load_qa_chain
from pinecone.grpc import PineconeGRPC as Pinecone_Client
from modules import save_uploaded_file, read_document, chunk_data, retrieve_answers

load_dotenv()



# doc = read_document('./docs/')
# documents_chunks = chunk_data(doc)

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# vectors = embeddings.embed_query("hello howsdsdsd are you")
# len(vectors)
pc = Pinecone_Client(api_key=os.environ['PINECONE_API_KEY'],region="us-east-1")
index_name="langchainvectordb"

# index= Pinecone.from_documents(doc,embeddings,index_name=index_name)


llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

chain = load_qa_chain(llm,chain_type="stuff")


# Streamlit UI for uploading PDF and asking questions
def main():
    st.title("PDF Document Q&A System")
    uploaded_file = st.file_uploader("Upload your PDF document", type=['pdf'])
    query = st.text_input("Enter your question here:")

    if uploaded_file is not None and query:
        save_path = save_uploaded_file(uploaded_file)
        document_text = read_document(save_path)
        if document_text:
            if st.button("Get Answer"):
                documents_chunks = chunk_data(document_text)
                index = Pinecone.from_documents(documents_chunks, embeddings, index_name=index_name)
                answer = retrieve_answers(query, chain,index)
                st.write("Answer:", answer['output_text'])
        else:
            st.write("Unable to extract text from the uploaded PDF.")

if __name__ == "__main__":
    main()