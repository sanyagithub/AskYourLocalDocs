# 📄🤖 AskYourDocs: AI-Powered Local Document Q&A Tool

**AskYourDocs** is an AI tool that allows you to ask questions and get answers from your **local documents** — all while keeping your data private and offline. Whether you have PDFs, Word docs, Excel sheets, or text files, this tool helps you find what you need instantly. No cloud, no uploading — just **you and your files**.

---

## 🚀 Features

- **Works Offline**: Keeps everything on your computer — your data never leaves your system.
- **Multiple File Types**: Supports PDFs, DOCX, TXT, and XLSX files.
- **Quick Answers**: Uses advanced NLP models to understand your documents and answer your questions.
- **Privacy-First**: No cloud dependency — perfect for sensitive or personal data.

---

## 📥 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/AskYourDocs.git
   cd AskYourDocs
   
2. **Install Dependencies:**

   ```bash
   pip install sentence-transformers faiss-cpu PyPDF2 python-docx pandas openpyxl

3. **Run the Script:**

   ```bash
   python document_qna.py

## 📂 How to Use
Place your documents (PDF, DOCX, TXT, XLSX) into a folder.

Specify the folder path in document_qna.py by updating the line:

   ```python
   process_documents("YOUR_DOCUMENT_DIRECTORY")
   ```

Run the script and type your question when prompted:

   ```bash
   Enter your question: What are the key takeaways from the report?
   ```

Get instant answers from your local files! 🪄

## 📝 Examples of Questions You Can Ask
1. “What are the key takeaways from last week’s meeting notes?” 📝
2. “Show me the sales numbers for Q2 in the Excel reports.” 📊
3. “Where did I write about feature updates in my project docs?” 💼
4. “What’s the summary of that research paper?” 📚

## ❤️ Inspiration
This project was inspired by a conversation with my dad, who pointed out the need for a private, local way to search through documents. His insight sparked this idea, and I’m thrilled to share the first version with you.

## 🤝 Contributing
I’d love to hear your thoughts and ideas to make this tool better! Feel free to:

Open issues for feature requests or bugs.
Submit pull requests to contribute improvements.

## 📜 License
This project is licensed under the MIT License.
---

🌟 Let’s keep building and learning together!
