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
st.markdown(f'<p style="background-color:#b3cee5;color:#414C6B;">Enter text you want to get translated</p>', unsafe_allow_html=True) 
text_to_translate = st.text_input("")
if text_to_translate:
  translator = Translator()
  lang = translator.detect(text_to_translate).lang
  if lang == 'am':
    translated_txt = translator.translate(text_to_translate, src= lang, dest= 'en')
  else:
    translated_txt = translator.translate(text_to_translate, src= lang, dest='am')
  st.markdown(f'<p style="background-color:#b3cee5;color:#414C6B;">{translated_txt.text}</p>', unsafe_allow_html=True) 
