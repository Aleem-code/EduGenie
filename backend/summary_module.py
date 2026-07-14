import google.generativeai as genai

# -----------------------------------------------------------
# Summary Module
#
# This module generates concise and easy-to-understand
# summaries from educational content using Gemini.
# -----------------------------------------------------------

# Create the Gemini model once when the application starts
model = genai.GenerativeModel(
    model_name="models/gemini-3.5-flash"
)


def summarize_text(text: str) -> str:
    """
    Generates a simplified summary of the provided text.

    Parameters:
        text (str): Educational content to summarize.

    Returns:
        str: Simplified summary or an error message.
    """

    try:

        # Prevent empty input
        if not text or not text.strip():
            return "Please provide text to summarize."

        # Prompt designed for educational summaries
        prompt = f"""
        You are an AI Educational Assistant.

        Summarize the following text:
        - Use simple language.
        - Keep the summary concise.
        - Focus only on the most important points.
        - Make it easy for students to understand.

        Text:

        {text}
        """

        # Send request to Gemini
        response = model.generate_content(prompt)

        # Ensure a response was generated
        if hasattr(response, "text") and response.text:
            return response.text.strip()

        return "No summary was generated."

    except Exception as e:
        return f"Error in Summary Module: {str(e)}"


