import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("Student Management System")

menu = ["Create", "Read", "Update", "Delete", "List"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Create":
    st.subheader("Add a New Student")
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    dob = st.date_input("Date of Birth")
    amount_due = st.number_input("Amount Due", min_value=0.0)
    if st.button("Add Student"):
        student_data = {
            "first_name": first_name,
            "last_name": last_name,
            "dob": dob.isoformat(),
            "amount_due": amount_due
        }
        response = requests.post(f"{API_URL}/students/", json=student_data)
        if response.status_code == 200:
            st.success("Student added successfully!")
        else:
            st.error("Failed to add student.")

elif choice == "Read":
    st.subheader("View Student Details")
    student_id = st.number_input("Student ID", min_value=1, step=1)
    if st.button("Get Student"):
        response = requests.get(f"{API_URL}/students/{student_id}")
        if response.status_code == 200:
            student = response.json()
            st.json(student)
        else:
            st.error("Student not found.")

elif choice == "Update":
    st.subheader("Update Student Information")
    student_id = st.number_input("Student ID", min_value=1, step=1)
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    dob = st.date_input("Date of Birth")
    amount_due = st.number_input("Amount Due", min_value=0.0)
    if st.button("Update Student"):
        student_data = {
            "first_name": first_name,
            "last_name": last_name,
            "dob": dob.isoformat(),
            "amount_due": amount_due
        }
        response = requests.put(f"{API_URL}/students/{student_id}", json=student_data)
        if response.status_code == 200:
            st.success("Student updated successfully!")
        else:
            st.error("Failed to update student.")

elif choice == "Delete":
    st.subheader("Delete a Student")
    student_id = st.number_input("Student ID", min_value=1, step=1)
    if st.button("Delete Student"):
        response = requests.delete(f"{API_URL}/students/{student_id}")
        if response.status_code == 200:
            st.success("Student deleted successfully!")
        else:
            st.error("Failed to delete student.")

elif choice == "List":
    st.subheader("List All Students")
    response = requests.get(f"{API_URL}/students/")
    if response.status_code == 200:
        students = response.json()
        st.write(students)
    else:
        st.error("Failed to retrieve students.") 