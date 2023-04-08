import streamlit as st

def load_text():
    generation_text = st.text_input(label='Введите текст для генерации')
    if generation_text:
        return generation_text
    else:
        return ''

def load_len():
    generation_len_txt = st.text_input(label='Введите длину сгенерированного текста')
    if generation_len_txt:
        try:
            generation_len = int(generation_len_txt)
        except:
            generation_len = 0
        return generation_len
    else:
        return 0