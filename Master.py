# How to show the analysis of our code in webapp

import streamlit as st
import pandas as pd

st.title("Doing Streamlit")


st.header("Random Header")

st.write("Hello Learners!!!")


# step 1 - install libary
# step 2 - create file
# step 3 - write on terminal : 'streamlit run file.py' 



df = pd.DataFrame({
    'Name' : ['John', 'Adam', 'Bob', 'Mary'] ,
    'Marks': [78, 92, 61, 85]
})

st.write(df.head(2))

st.write("Description of the dataframe:")
st.write( df.describe() )

st.write("Visualisation")
st.line_chart(df['Marks'])
