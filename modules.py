import io
import os
from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter



def save_uploaded_file(uploaded_file, path='./docs/'):
    """ Saves the uploaded file to a specified directory. """
    try:
        # Create the directory if it does not exist
        os.makedirs(path, exist_ok=True)
        
        file_path = os.path.join(path, uploaded_file.name)
        
        # Write the contents of the uploaded file to the new file.
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getvalue())
        
        return file_path
    except Exception as e:
        # Handle errors in saving the file
        return str(e)

def read_document(file_directory='./docs/budget_speech.pdf'):
    pdf_loader = PyPDFLoader(file_directory)
    pdf_text = pdf_loader.load()
    return pdf_text

def chunk_data(docs,chunk_size=800,chunk_overlap=50):
    data_spliter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap)
    doc = data_spliter.split_documents(docs)
    return doc

def retrive_query(query,index,k=2):
    matching_results = index.similarity_search(query,k=k)
    print("+====================")
    print("matching res: ",matching_results)
    return matching_results

def retrieve_answers(query,chain,index):
    doc_search = retrive_query(query,index)
    print(doc_search)
    input_data = {
    'input_documents': doc_search,
    'question': query,
}
    response = chain.invoke(input=input_data)
    return response