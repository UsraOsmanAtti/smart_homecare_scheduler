"""
Smart Homecare Scheduler (Streamlit Edition)
All Rights Reserved © Dr. Yousra Abdelatti
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

st.set_page_config(page_title="Smart Homecare Scheduler", page_icon="💙", layout="centered")

# ----------------------
# Data Storage
# ----------------------
if "patients" not in st.session_state:
    st.session_state["patients"] = []
if "doctors" not in st.session_state:
    st.session_state["doctors"] = []
if "schedule" not in st.session_state:
    st.session_state["schedule"] = []

# ----------------------
# Helper Functions
# ----------------------
def generate_schedule():
    if not st.session_state["patients"] or not st.session_state["doctors"]:
        return []
    schedule = []
    start_date = datetime.today()
    for i, patient in enumerate(st.session_state["patients"]):
        doctor = random.choice(st.session_state["doctors"])
        visit_date = start_date + timedelta(days=i % 7)
        schedule.append({
            "Patient": patient,
            "Doctor": doctor,
            "Date": visit_date.strftime("%A, %d %B %Y")
        })
    return schedule

# ----------------------
# UI
# ----------------------
st.title("💙 Smart Homecare Scheduler")
st.markdown("A simple & colorful scheduler tool for **Dr. Yousra Abdelatti** 💐")

menu = st.sidebar.radio("📌 Menu", ["Add Patients", "Add Doctors", "View Patients", "View Doctors", "Generate Schedule", "View Schedule", "Edit Names"])

if menu == "Add Patients":
    name = st.text_input("Enter patient name")
    if st.button("Add Patient"):
        if name:
            st.session_state["patients"].append(name)
            st.success(f"Patient **{name}** added!")

elif menu == "Add Doctors":
    name = st.text_input("Enter doctor name")
    if st.button("Add Doctor"):
        if name:
            st.session_state["doctors"].append(name)
            st.success(f"Doctor **{name}** added!")

elif menu == "View Patients":
    st.subheader("👩‍⚕️ Patients")
    st.write(st.session_state["patients"])

elif menu == "View Doctors":
    st.subheader("👨‍⚕️ Doctors")
    st.write(st.session_state["doctors"])

elif menu == "Generate Schedule":
    st.session_state["schedule"] = generate_schedule()
    st.success("✅ Schedule generated!")

elif menu == "View Schedule":
    st.subheader("📅 Weekly Schedule")
    if st.session_state["schedule"]:
        df = pd.DataFrame(st.session_state["schedule"])
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No schedule yet. Please generate one.")

elif menu == "Edit Names":
    st.subheader("✏️ Edit or Delete Names")

    st.write("**Patients:**")
    for i, p in enumerate(st.session_state["patients"]):
        new_name = st.text_input(f"Edit Patient {i+1}", p, key=f"pat_{i}")
        if new_name != p:
            st.session_state["patients"][i] = new_name

    st.write("**Doctors:**")
    for i, d in enumerate(st.session_state["doctors"]):
        new_name = st.text_input(f"Edit Doctor {i+1}", d, key=f"doc_{i}")
        if new_name != d:
            st.session_state["doctors"][i] = new_name
