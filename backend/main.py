from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai

# -----------------------------------------------------------
# Gemini API Configuration
#
# Replace the placeholder below with your Gemini API key
# while testing locally.
#
# -----------------------------------------------------------

genai.configure(
    api_key="Enter_your_Gemini_api_key"
)

# -----------------------------------------------------------
# Import Project Modules
# -----------------------------------------------------------

from explanation_module import explain_topic
from qna import answer_question_with_gemini
from summary_module import summarize_text
from quiz_module import generate_quiz
from learning_path import get_learning_recommendations

# -----------------------------------------------------------
# FastAPI Application
# -----------------------------------------------------------

app = FastAPI(
    title="AI Educational Assistant",
    description="Educational Assistant powered by LaMini-Flan-T5 and Gemini",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------------------------------------
# Request Models
# -----------------------------------------------------------

class TopicRequest(BaseModel):
    topic: str


class QuestionRequest(BaseModel):
    question: str


class TextRequest(BaseModel):
    text: str


# -----------------------------------------------------------
# Home Endpoint
# -----------------------------------------------------------

@app.get("/")
def home():
    """
    Basic route to verify that the API is running.
    """

    return {
        "message": "AI Educational Assistant API is running successfully."
    }


# -----------------------------------------------------------
# Topic Explanation Endpoint
# -----------------------------------------------------------

@app.post("/explain")
def explain(request: TopicRequest):
    """
    Generate a beginner-friendly explanation for a topic.
    """

    explanation = explain_topic(
        request.topic
    )

    return {
        "topic": request.topic,
        "explanation": explanation
    }


# -----------------------------------------------------------
# Question Answering Endpoint
# -----------------------------------------------------------

@app.post("/ask")
def ask_question(request: QuestionRequest):
    """
    Answer user questions using Gemini.
    """

    answer = answer_question_with_gemini(
        request.question
    )

    return {
        "question": request.question,
        "answer": answer
    }


# -----------------------------------------------------------
# Summary Endpoint
# -----------------------------------------------------------

@app.post("/summary")
def generate_summary(request: TextRequest):
    """
    Generate a concise educational summary.
    """

    summary = summarize_text(
        request.text
    )

    return {
        "summary": summary
    }


# -----------------------------------------------------------
# Quiz Generation Endpoint
# -----------------------------------------------------------

@app.post("/quiz")
def create_quiz(request: TextRequest):
    """
    Generate quiz questions from educational content.
    """

    quiz = generate_quiz(
        request.text
    )

    return {
        "quiz": quiz
    }


# -----------------------------------------------------------
# Learning Path Recommendation Endpoint
# -----------------------------------------------------------

@app.post("/learning-path")
def generate_learning_path(request: TopicRequest):
    """
    Generate a structured learning roadmap.
    """

    roadmap = get_learning_recommendations(
        request.topic
    )

    return {
        "topic": request.topic,
        "learning_path": roadmap
    }


# -----------------------------------------------------------
# Run Instructions
#
# Start the server using:
#
# uvicorn main:app --reload
#
# Open Swagger UI:
#
# http://127.0.0.1:8000/docs
#
# ----------------------------------------------------------
