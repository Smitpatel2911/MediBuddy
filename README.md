# 💊 MediBuddy: Medicine Reminder App ⏰🔔

MediBuddy is a **Streamlit-based** desktop web app built with Python that helps users **schedule and receive reminders** to take their medications on time. It also supports **desktop notifications** and has a beautiful custom background image.

---

## 🚀 Features

- 📋 **Add medicine details** (name, time, dosage)
- 👀 **View scheduled medicines** in a neat table
- ⏰ **Live background reminder engine** (checks every minute)
- 🔔 **Desktop notification alerts** using `plyer`
- 🖼️ **Custom background image** using `set_background()`

---

## 📂 Project Structure

├── app.py # Main Streamlit app
├── reminder.py # Background reminder engine
├── utills.py # Helper functions (load/save, background)
├── schedule.csv # Stores medicine schedules
├── bg.jpg # Background image for the app
├── requirement.txt # Required modules


---

## 📸 UI Preview

![App Screenshot](bg.jpg) <!-- Optional: Replace with your own image or remove -->

---

## 🔧 Setup Instructions

### 1. 📦 Install Requirements

```bash
pip install streamlit
pip install plyer
