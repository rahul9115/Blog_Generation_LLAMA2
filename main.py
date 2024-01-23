import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def llama2(input,number_of_words,style_blog):
    llm=CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256, 'temperature':0.01})


    trigger=f"""
    Please generate a blog for {style_blog} for the topic {input} upto {number_of_words} words
    """
    display=PromptTemplate(input_variables=["style","text","number of words"])
    llm(display.format(style=style_blog,text=input,n_words=number_of_words))

st.set_page_config(page_title="Generate Blogs",
                   layout="centered",
                   initial_sidebar_state="collapsed")

st.head("Generate your own blogs")

input=st.text_input("Please enter the Blog Topic")

column1,column2=st.columns([5,5])


with column1:
    number_of_words=st.text_input("Number of Words")

with column2:
    style_blog=st.selectbox("Blog recipient",("Researchers","Students","General Public","AI & ML Professionals"))

submit=st.button("Generate")
if submit:
    st.write(llama2())