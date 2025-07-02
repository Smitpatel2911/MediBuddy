import streamlit as st
from utills import set_background, load_data, save_data,load_schedule, save_schedule
import pandas as pd
from reminder import check_reminders

set_background("bg.jpg")

st.title("💊 MediBuddy : Medicine Reminder ⏰🔔")
menu = st.sidebar.selectbox("Menu", ["Add Medicine", "View Schedule", "Reminder Running..."])

if menu == "Add Medicine":
    name = st.text_input("Medicine Name")
    time = st.time_input("Time to Take")
    dosage = st.text_input("Dosage (e.g. , 1 tablet)")
    if st.button("Add to Schedule"):
        med = load_schedule()
        med = med._append({"Medicine" : name , "Time" : str(time) , "Dosage" : dosage}, ignore_index = True)
        save_schedule(med)
        st.success("Medicine Added Successfully! ..")

elif menu == "View Schedule":
    st.dataframe(load_schedule())

elif menu == "Reminder Runing":
    st.info("Reminders are running in the background... keep this tab open.")
    check_reminders()
