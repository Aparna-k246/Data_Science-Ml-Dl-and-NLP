import streamlit as st
import pandas as pd

st.title("Streamlit text input")

name=st.text_input("Enter your name:")

age=st.slider("Select your age:",0,100,25)
st.write(f"Your age is  {age}.")

options= ["Python", "Java" , "JavaScript"]
choice= st.selectbox("Choose your favourite lang:" ,options)

st.write(f"You selected {choice}.")

if name:
    st.write(f"Hello {name}.")

df=pd.DataFrame({
    'Name':["John","Jake","Jill"],
    'Age':[28,26,24],
    'City':["New York","Chicago","LA"]
})
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file=st.file_uploader("Choose a csv file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
