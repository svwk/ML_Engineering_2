import streamlit as st
import text_utils as tut
from generator import Generator


st.title('Генерация текста')
st.markdown('<span style="color: red; font-weight: bold">NB!</span> Поддерживается только английский язык', unsafe_allow_html=True)
source_text = tut.get_text_from_input()
text_length = tut.get_length_from_input()
result_text = st.button('Сгенерировать текст')
if result_text:
    if len(source_text) > 0 and text_length > 0:
        with st.spinner('Дождитесь генерации...'):
            generated_text = Generator().generate_text(source_text, text_length)
            st.write('**Результаты генерации:**')
            st.write(generated_text)
    else:
        st.write('<span style="color: red">Введите текст для генерации и длину!</span>', unsafe_allow_html=True)
