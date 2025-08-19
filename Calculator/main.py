import streamlit as st

st.title("Calculator!")
mode = st.radio("Choose your option:", ["minus", "plus", "x", "/"])
n1 = st.text_input("Enter 1st number:")
n2 = st.text_input("Enter 2nd number:")
n1 = int(n1)
n2 = int(n2)
if mode == "x" and mode:
    st.title("Answer:")
    st.text(f"{n1} x {n2} = {n1 * n2}")
elif mode == "plus" and mode:
    st.title("Answer:")
    st.text(f"{n1} + {n2} = {n1 + n2}")
elif mode == "minus" and mode:
    st.title("Answer:")
    st.text(f"{n1} - {n2} = {n1 - n2}")
elif mode == "/" and mode:
    st.title("Answer:")
    st.text(f"{n1} / {n2} = {n1 / n2}")