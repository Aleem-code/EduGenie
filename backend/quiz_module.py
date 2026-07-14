import json
import re
import google.generativeai as genai

# -----------------------------------------------------------
# Quiz Generation Module
#
# Generates multiple-choice quiz questions from educational
# content using the Gemini model.
# -----------------------------------------------------------

# Create the Gemini model once when the application starts
model = genai.GenerativeModel(
    model_name="models/gemini-3.5-flash"
)


def clean_json_block(text: str) -> str:
    """
    Removes Markdown JSON code fences if Gemini returns them.
    """

    return re.sub(
        r"```(?:json)?\n(.*?)```",
        r"\1",
        text,
        flags=re.DOTALL
    ).strip()


def generate_quiz(text: str) -> list:
    """
    Generates 3 multiple-choice questions from a passage.

    Parameters:
        text (str): Educational content provided by the user.

    Returns:
        list: Quiz questions in JSON format.
    """

    try:

        # Prevent empty passages
        if not text or not text.strip():
            return []

        prompt = f"""
You are an educational quiz generator.

From the passage below, create exactly 3 multiple-choice questions.

Requirements:
- Each question must have 4 options.
- Each question must have one correct answer.
- The answer must exactly match one of the options.
- Return ONLY valid JSON.
- Do NOT include explanations.
- Do NOT include Markdown formatting.

Output format:

[
  {{
    "question": "Question text",
    "options": ["A", "B", "C", "D"],
    "answer": "Correct option"
  }}
]

Passage:

{text}
"""

        # Generate quiz
        response = model.generate_content(prompt)

        quiz_text = response.text.strip()

        # Remove markdown code blocks if present
        cleaned_text = clean_json_block(quiz_text)

        # Convert JSON string to Python list
        quiz_data = json.loads(cleaned_text)

        # Validate overall structure
        if not isinstance(quiz_data, list):
            return []

        validated_quiz = []

        # Validate each question object
        for item in quiz_data:

            if (
                isinstance(item, dict)
                and "question" in item
                and "options" in item
                and "answer" in item
            ):
                validated_quiz.append(item)

        return validated_quiz

    except Exception as e:
        print(f"Quiz Generation Error: {e}")
        return[]
        
        
