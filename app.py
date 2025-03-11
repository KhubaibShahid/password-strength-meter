import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", layout="wide")

st.title("Password Strength Checker")

user_password = st.text_input("Enter your password")

points = 0

if st.button("Check") or user_password:

    # check condition for minimum 8 length of password 

    if (len(user_password) >= 8):
        points += 1
    else:
        st.text("password contain minimum 8 characters")

    # check condition for lowercase and uppercase letters
    
    if re.search(r"[A-Z]", user_password) and re.search(r"[a-z]", user_password):
        points += 1
    else:
        st.text("password must contain at least 1 uppercase and lowercase letters")

    # check condition for digit

    if re.search(r"\d", user_password):
        points += 1
    else:
        st.text("password contain at least 1 digit")
    
    # check condition for special characters

    if re.search(r"[!@#$%^&*]", user_password):
        points += 1
    else:
        st.text("password contain at least 1 special character")

    # check condition for score and display the result

    if points == 4:
        st.text("💪 Strong password")
    elif points == 3:
        st.text("⚠️ Moderate password, should be better")
    else:
        st.text("❌ Weak password, improve it using above suggestions")
    
    
st.text(points)