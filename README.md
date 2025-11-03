
## AI Story Generator Through Images

### Overview
**AI Story Generator Through Images** is a **multimodal Generative AI project** that transforms images into complete narrated stories.  
It combines **vision-language models**, **Large Language Models (LLMs)**, and **Text-to-Speech (TTS)** to understand images, generate creative stories, and narrate them in a natural voice — bringing your visuals to life through storytelling.  

---

####  Features
-  **Image Understanding:** Extracts visual context using transformer-based models like **CLIP** or **BLIP**.  
-  **Story Generation:** Uses **LLMs** ( Gemini) to craft detailed and coherent stories.  
-  **Voice Narration:** Converts the generated story into natural speech using **gTTS**.  
-  **Interactive Interface:** Built with **Streamlit** for easy user interaction and real-time output.

---

##  Tech Stack
| Category | Tools / Frameworks |
|-----------|-------------------|
| Language | Python |
| AI Frameworks | LangChain
| LLMs | Gemini 
| Vision Models | CLIP / BLIP |
| TTS | gTTS
| UI | Streamlit |
| Environment | myenv (Python virtual environment) |

---

###  How It Works
1. **Upload Images:** User uploads one or more images.  
2. **Visual Analysis:** The model extracts semantic meaning and captions.  
3. **Story Generation:** An **LLM** generates a coherent story connecting all images.  
4. **Voice Generation:** The story text is converted into voice narration using **TTS**.  
5. **Output:** Displays both story text and audio playback in the Streamlit interface.

---

###  Installation

### 1️ Clone the Repository
```bash
git clone https://github.com/<your-username>/AiStoryGenerator.git
cd AiStoryGenerator
````

### 2️ Create & Activate Virtual Environment

```bash
python -m venv myenv
myenv\Scripts\activate       # (Windows)

```

### 3️ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run the App

```bash
streamlit run app.py
```

Then open the link shown in your terminal (usually `http://localhost:8501`) to use the app.

---

### Example Output

**Input:** 3 images of a child, a park, and a balloon.
**AI Output:**

> “Once upon a time, a curious child wandered into a sunny park, chasing a red balloon that floated beyond the trees…”

The system also plays a **narrated version** of this story through AI-generated voice.

---

### Future Enhancements

*  Auto-generate story videos with narration
*  Add expressive voice emotion control
*  Multilingual story and narration support

---

###  Author

**Quamrul Hoda**
AI/ML Engineer | Generative & Agentic AI Specialist

*  [Portfolio](#)
*  [LinkedIn](https://www.linkedin.com/in/quamrul-hoda-1a4247285/)
*  [GitHub](https://github.com/quamrl-hoda)

---

##  License

This project is licensed under the **MIT License** — feel free to use and modify it for learning or research purposes.

---

### ✨ Tagline

> “Turns images into creative, narrated stories using Generative AI, LLMs, and voice synthesis.”

```

---

Would you like me to generate a matching **`requirements.txt`** file next (with all the correct Python dependencies for this project)?
```
