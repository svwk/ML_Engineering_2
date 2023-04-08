import streamlit as st
import Router as rt
from generator import Generator


st.title('Генерация текста')
st.markdown('<span style="color: red; font-weight: bold">NB!</span> Поддерживается только английский язык', unsafe_allow_html=True)
txt = rt.load_text()
txt_len = rt.load_len()
result = st.button('Сгенерировать текст')
if result:
    if len(txt) > 0 and txt_len > 0:
        with st.spinner('Дождитесь генерации...'):
            generated_text = Generator().generate_text(txt, txt_len)
            st.write('**Результаты генерации:**')
            st.write(generated_text)
    else:
        st.write('<span style="color: red">Введите текст для генерации и длину!</span>', unsafe_allow_html=True)
