import streamlit as st

st.title("My Streamlit App")

name = st.text_input("Enter your name")
button = st.button("Click me")

if button:
    st.write(f"Hello, {name}!")
