import streamlit as st
import pandas as pd
import numpy as np

#title
st.title("Hello Streamlit")

#Display simple text
st.write("Simple text")

#creating simple dataframe
df=pd.DataFrame({
    'first':[1,2,3,4],
    'second':[10,20,30,40]
})

#Display the dataframe
st.write("Here is the dataframe")
st.write(df)

#create a line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)