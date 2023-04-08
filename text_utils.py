import streamlit as st


def get_text_from_input():
    """
    Gets source text for generation from standard input
    """
    source_text_for_generation = st.text_input(label='Введите текст для генерации')
    if source_text_for_generation:
        return source_text_for_generation
    else:
        return ''


def get_length_from_input():
    """
    Gets length of text for generation from standard input
    """
    generated_text_length_txt = st.text_input(label='Введите длину сгенерированного текста')
    if generated_text_length_txt:
        try:
            generated_text_length = int(generated_text_length_txt)
        except:
            generated_text_length = 0
        return generated_text_length
    else:
        return 0
