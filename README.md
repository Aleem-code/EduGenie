# EduGenie – AI Educational Assistant

EduGenie is an AI-powered educational assistant designed to help students learn more effectively. The application provides topic explanations, question answering, quiz generation, text summarization, and personalized learning path recommendations using Generative AI.

## Features

### Topic Explanation
Generate simple and easy-to-understand explanations for educational topics.

### Question Answering
Ask questions on any topic and receive AI-generated answers.

### Quiz Generation
Automatically generate quizzes from a given topic to support self-assessment.

### Text Summarization
Convert lengthy educational content into concise summaries.

### Learning Path Recommendation
Generate a structured learning roadmap for a selected subject or skill.

---

## Technologies Used

### Backend
- Python
- FastAPI
- Google Gemini API
- Transformers
- LaMini-T5

### Frontend
- HTML
- CSS
- JavaScript

---

## Project Structure

```text
EduGenie/
│
├── backend/
│   ├── main.py
│   ├── explanation_module.py
│   ├── qna.py
│   ├── quiz_module.py
│   ├── summary_module.py
│   └── learning_path.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/EduGenie.git
cd EduGenie
```

### Install Dependencies

```bash
pip install fastapi uvicorn google-generativeai transformers torch sentencepiece
```

---

## Gemini API Configuration

Open the backend configuration file and replace:

```python
api_key = "ENTER_YOUR_GEMINI_API_KEY"
```

with your own Gemini API key.

You can obtain a Gemini API key from Google AI Studio.

---

## Running the Backend

Navigate to the backend folder:

```bash
cd backend
```

Start the FastAPI server:

```bash
python -m uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Running the Frontend

Open:

```text
frontend/index.html
```

in your browser while the FastAPI server is running.

---

## Future Improvements

- User authentication
- Learning progress tracking
- PDF and document upload support
- Personalized study recommendations
- Deployment to cloud platforms

---

## Author

Developed as an AI-powered educational assistance project using FastAPI, Gemini AI, and LaMini-T5.
