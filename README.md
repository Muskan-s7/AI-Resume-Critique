# 📄 AI Resume Critique — Your Smart Career Companion

Welcome to **AI Resume Critique**, an **AI-powered web app** that reviews resumes and provides **intelligent, actionable feedback** using **Cohere’s powerful language model**.

---

## 📌 What is AI Resume Critique?

**AI Resume Critique** is a **Streamlit-based Python application** that allows users to:

- 📤 **Upload resumes** in PDF or TXT format
- 🧠 **Analyze them using a Large Language Model (LLM)** via the **Cohere API**
- 💡 Get **smart suggestions** for improving:
  - ✍️ Content clarity
  - 🧩 Format & structure
  - 🧑‍💼 Role-specific relevance
  - ✅ Skills & experience descriptions

Perfect for **students, job seekers, and professionals** looking to improve their resume quality with AI feedback.

---

## ✨ Features

✅ Upload a resume (PDF or TXT format)  
🧠 AI-generated suggestions powered by Cohere  
📋 Real-time critique display in the Streamlit web app  
🔐 API key hidden securely using `.env` and `.gitignore`  
🌐 Clean, minimal, and responsive UI built with Streamlit  

---

## 📁 Folder Structure
Resume_Critique/
├── .env.example # Template for environment variables (API key placeholder)
├── app.py # Main Streamlit application
├── .gitignore # Files and folders to ignore in version control
├── pyproject.toml # Project dependencies
├── README.md # You're reading it!

---

## 🛠️ Built With
- **Python 3.11+** – Core programming language
- **Streamlit** – Web application framework
- **Cohere** – Large Language Model for natural language understanding
- **PyPDF2** – PDF reading and processing
- **python-dotenv** – Environment variable handling
  
---

## ⚙️ Project Setup & Usage

Follow these steps to set up the project on your local machine:

---

### 1.Clone the repository  

```bash
git clone https://github.com/your-username/AI-Resume-Critique.git
cd AI-Resume-Critique
```

### 2.Create a virtual environment

```bash
python -m venv .venv
```

### 3.Activate the environment

**On Windows:**

```bash
.venv\Scripts\activate
```

**On macOS/Linux:**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

If ***requirements.txt*** is not present, install manually:

```bash
pip install streamlit cohere python-dotenv PyPDF2
```

### 5. Set Up Environment Variables

Create a `.env` file in the root of the project directory and add your **Cohere API key** like this:

```ini
CO_API_KEY=your_actual_api_key_here
```

### 6. Run the App

```bash
streamlit run app.py
```

---

## 🔐 Security

- Your `.env` file is excluded from GitHub using `.gitignore`.
- **Do NOT upload your API key publicly.**
- Instead, provide a `.env.example` file with a placeholder like:
  ```ini
  CO_API_KEY=your_api_key_here
  ```

---

🙋‍♀️ About the Developer
👤 Shaik Muskan
A passionate developer exploring the intersection of **AI** and **web development**. This project was built as part of a learning journey in **natural language processing** and **Streamlit apps** for career enhancement tools.


💬 Final Notes
Whether you're a **student**, **professional**, or just curious about how AI can boost your resume, **AI Resume Critique** offers a fast and simple way to get personalized feedback.

