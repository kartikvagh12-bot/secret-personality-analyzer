import streamlit as st
import random
import time

st.title("🔮 Secret Personality Analyzer")

st.write("Answer these questions to reveal your hidden personality.")

name = st.text_input("State your first name only?")
birthday = st.text_input("State your birthdate (dd/mm/yyyy)")
birthplace = st.text_input("What is your birthplace?")
bloodgrp = st.text_input("State your blood group")
gender = st.text_input("What do you think your gender is based upon your appearance?")
number = st.number_input("Pick a number between 1 to 20", 1, 20)

if st.button("Analyze Personality 😏"):

    name = name.lower()

    with st.spinner("Analyzing biometric data..."):
        time.sleep(2)

    if name == "pushpraj":
        st.success("Result: You are bisexual 😆")
    elif name == "kartik":
        st.success("Result: You are straight 😎")
    else:
        responses = [
            "The information is incorrect 😂",
            "Please try again 😜",
            "You are straight 😌"
        ]

        result = random.choice(responses)
        st.success(f"Result: {result}")
