from transformers import pipeline
import streamlit as st
import Router as rt

@st.cache(allow_output_mutation=True)
def load_model():
    return pipeline("text-generation", "gpt2")

model = load_model()

st.title('Генерация текста')
st.markdown('<span style="color: red; font-weight: bold">NB!</span> Поддерживается только английский язык', unsafe_allow_html=True)
txt = rt.load_text()
txt_len = rt.load_len()
result = st.button('Сгенерировать текст')
if result:
    if len(txt) > 0 and txt_len > 0:
        generator = load_model()
        with st.spinner('Дождитесь генерации...'):
            generated_text = generator(txt, max_length=txt_len)
            st.write('**Результаты генерации:**')
            st.write(generated_text[0]['generated_text'])
    else:
        st.write('<span style="color: red">Введите текст для генерации и длину!</span>', unsafe_allow_html=True)
