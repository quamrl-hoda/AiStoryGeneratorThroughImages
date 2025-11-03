import streamlit as st 
from storyGenerator import generate_story_from_images, narrate_story
from PIL import Image
import io



st.title("AI Story Generator From Images")

st.markdown("Upload 1 to 10 images, choose a style and let AI write and narrate a story for you!")


with st.sidebar:
    st.header("Controls")

    # sidebar option to upload images
    uploaded_files = st.file_uploader(
        "Upload Images",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True,
    )
    # selecting an story style
    story_style = st.selectbox(
        "Select Story Style",
        [
            "Fantasy",
            "Sci-Fi",
            "Mystery",
            "Adventure",
            "Romance",
            "Horror",
            "Comedy",
        ],
    )
    # button to generate story
    generate_button = st.button("Generate Story and Narration",type="primary")

# main logic

if generate_button:
    if not uploaded_files:
        st.warning("Please upload at least one image.")
    elif len(uploaded_files) > 10:
        st.warning("Please upload no more than 10 images.")
    else:
        with st.spinner("The AI is writing and narrating your story ... This may take a few moments."):
          try:
              pil_images = [Image.open(file) for file in uploaded_files]
              st.subheader("Your Visual Inspiration:")

              image_columns = st.columns(len(pil_images))

              for i, image in enumerate(pil_images):
                  with image_columns[i]:
                      st.image(image, use_container_width=True)

              generate_story = generate_story_from_images(pil_images, story_style)
              if "Error" in generate_story:
                  st.error("There was an error generating the story. Please try again.")
              else:
                  st.subheader(f"Your {story_style} Story:")
                  st.success(generate_story)
              st.subheader("Listen to your Story:")
              audio_file= narrate_story(generate_story)
              if audio_file:
                    st.audio(audio_file,format="audio/mp3")

          except Exception as e:
              st.error(f"Error loading images: {e}")