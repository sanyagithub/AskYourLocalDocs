import os
import pandas as pd
import PyPDF2
import docx
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

# Initialize the NLP model for generating embeddings
nlp_model = SentenceTransformer('all-MiniLM-L6-v2')

# Supported file types
SUPPORTED_FILES = ['.pdf', '.docx', '.txt', '.xlsx']

# Data structures to hold document text and embeddings
documents = []
doc_texts = []
doc_embeddings = []

# Function to extract text from PDFs
def extract_pdf_text(file_path):
    text = ""
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() or ""
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text

# Function to extract text from DOCX files
def extract_docx_text(file_path):
    text = ""
    try:
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        print(f"Error reading DOCX: {e}")
    return text

# Function to extract text from TXT files
def extract_txt_text(file_path):
    text = ""
    try:
        with open(file_path, 'r') as file:
            text = file.read()
    except Exception as e:
        print(f"Error reading TXT: {e}")
    return text

# Function to extract text from Excel files
def extract_excel_text(file_path):
    text = ""
    try:
        df = pd.read_excel(file_path, sheet_name=None)
        for sheet_name, sheet_data in df.items():
            text += f"\nSheet: {sheet_name}\n"
            text += sheet_data.to_string()
    except Exception as e:
        print(f"Error reading Excel: {e}")
    return text

# Function to process all supported documents in the given directory
def process_documents(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        file_ext = os.path.splitext(file)[1].lower()

        if file_ext in SUPPORTED_FILES:
            if file_ext == '.pdf':
                text = extract_pdf_text(file_path)
            elif file_ext == '.docx':
                text = extract_docx_text(file_path)
            elif file_ext == '.txt':
                text = extract_txt_text(file_path)
            elif file_ext == '.xlsx':
                text = extract_excel_text(file_path)
            else:
                continue

            if text:
                documents.append(file)
                doc_texts.append(text)

# Process documents in the current directory
process_documents("YOUR_DIRECTORY_HERE")

# Generate embeddings for the processed documents
if doc_texts:
    doc_embeddings = nlp_model.encode(doc_texts, show_progress_bar=True)
    doc_embeddings = np.array(doc_embeddings).astype('float32')

    # Create FAISS index
    dimension = doc_embeddings.shape[1]
    faiss_index = faiss.IndexFlatL2(dimension)
    faiss_index.add(doc_embeddings)

# Function to answer questions based on the indexed documents
def answer_question(question):
    query_embedding = nlp_model.encode([question]).astype('float32')
    D, I = faiss_index.search(query_embedding, 1)
    if D[0][0] < 1.0:
        return f"Best Match ({documents[I[0][0]]}):\n{doc_texts[I[0][0]][:500]}..."
    else:
        return "No relevant information found."

# Example query
question = input("Enter your question: ")
print(answer_question(question))
