from dotenv import load_dotenv
import os
from google import genai 
from gtts import gTTS
from io import BytesIO
load_dotenv()

# st.title("AI Story Generator From Images")

def create_advanced_prompt(style):
    # --- Base prompt ---
    base_prompt = f"""
    **Your Persona:** You are a friendly and engaging storyteller. Your goal is to tell a story that is fun and easy to read.
    **Your Main Goal:** Write a story in simple, clear, and modern English.
    **Your Task:** Create one single story that connects all the provided images in order.
    **Style Requirement:** The story must fit the '{style}' genre.
    **Core Instructions:**
    1.  **Tell One Single Story:** Connect all images into a narrative with a beginning, middle, and end.
    2.  **Use Every Image:** Include a key detail from each image.
    3.  **Creative Interpretation:** Infer the relationships between the images.
    4.  **Nationality**: Use only Indian Names,Characters, Places , Persona Etc.
    **Output Format:**
    -   **Title:** Start with a simple and clear title.
    -   **Length:** The story must be between 4 and 5 paragraphs.
    """

    # --- Add Style-Specific Instructions ---
    style_instruction = ""
    if style == "Morale":
        style_instruction = "\n**Special Section:** After the story, you MUST add a section starting with the exact tag `[MORAL]:` followed by the single-sentence moral of the story."
    elif style == "Mystery":
        style_instruction = "\n**Special Section:** After the story, you MUST add a section starting with the exact tag `[SOLUTION]:` that reveals the culprit and the key clue."
    elif style == "Thriller":
        style_instruction = "\n**Special Section:** After the story, you MUST add a section starting with the exact tag `[TWIST]:` that reveals a final, shocking twist."

    return base_prompt + style_instruction

# function ---- images, style --> story
def generate_story_from_images(images, style):
  
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[images, "write a short story about the images"]
    )
    return response.text

# function -- story -- audio file
def narrate_story(story_text):
    try:
        tts = gTTS(text=story_text, lang='en', slow=False)
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        return audio_bytes
    
    except Exception as e:
        return f"An unexpected error occurred during narration: {str(e)}"