import googletrans
from googletrans import Translator
import streamlit as st
import base64
def add_background_image(image_file):
  with open(image_file, "rb") as image_file:
     encoded_string = base64.b64encode(image_file.read())
  st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_background_image('bgi.png')   
st.markdown(f'<span style="background-color:#DFF2FF;color:#0F52BA;font-family:book-antiqua;font-size:24px;">AI App For Translation</span>', unsafe_allow_html=True)
text_to_translate = st.text_area("Text to Translate", "Hello")
translator = Translator()
lang = translator.detect(text_to_translate)
if lang == 'am':
  translated_txt = translator.translate(am_txt, src= lang, dest='en')
else:
  translated_txt = translator.translate(am_txt, src= lang, dest='am')
st.write(translated_txt)
