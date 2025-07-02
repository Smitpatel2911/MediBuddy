# All required function are here

import base64
import streamlit as st
import pandas as pd

def set_background(img_file):
    """Provide you imaged streamlit app""" 
    with open(img_file, "rb") as file:
        data = file.read()
    
    # encoding the data of image file
    encoded = base64.b64encode(data).decode()
    bg_style = f"""
    <style>
    .stApp{{
        background-image : url("data:image/jpg; base64, {encoded}");
        background-size : cover;
        background-repeat : no-repeat;
        background-attachment:fixed;
    }}
    </style>
    """
    st.markdown(bg_style, unsafe_allow_html=True)

def load_schedule():
    """Help in loading Schedule"""
    try:
        return pd.read_csv("schedule.csv")
    except:
        return pd.DataFrame(columns=["Medicine", "Time", "Dosage"])

def save_schedule(df):
    """Help in saving Schedule"""
    df.to_csv("schedule.csv", index=False)