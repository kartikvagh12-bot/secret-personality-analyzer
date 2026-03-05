import streamlit as st
import random

st.title("🔮 Secret Personality Analyzer")

name = st.text_input("Enter your first name only")

if st.button("Analyze Me 😏"):
    name = name.lower()

    if name == "pushpraj":
        st.success("You are bisexual 😆")
    elif name == "kartik":
        st.success("You are straight 😎")
    else:
        responses = [
            "The information is incorrect 😂",
            "Please try again 😜",
            "You are straight 😌"
        ]
        st.success(random.choice(responses))
