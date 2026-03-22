import streamlit as st
import requests
from datetime import date

st.title("📝 Task Manager - ToDo App")

st.write("Add a new task")

# Input fields
task_title = st.text_input("Task Title")
description = st.text_area("Description")
due_date = st.date_input("Due Date", min_value=date.today())

priority = st.selectbox(
    "Priority",
    ["Low", "Medium", "High"]
)

# Button
if st.button("Add Task"):

    if task_title == "":
        st.warning("Task title is required")

    else:

        data = {
            "title": task_title,
            "description": description,
            "dueDate": str(due_date),
            "priority": priority
        }

        
try:
    response = requests.post(
        "https://task-manager-app-production-9c8f.up.railway.app/add-task",
        json=data
    )

    st.write("Status Code:", response.status_code)
    st.write("Response:", response.text)

    if response.status_code == 200:
        st.success("Task added successfully")
    else:
        st.error("Failed to add task")

except:
    st.error("Backend server not running")


st.write("---")

# Show tasks
st.subheader("📋 All Tasks")

try:
    response = requests.get(
        "https://task-manager-app-production-9c8f.up.railway.app/tasks"
    )

    if response.status_code == 200:
        tasks = response.json()

        if len(tasks) == 0:
            st.info("No tasks added yet")

        for task in tasks:
            st.write(f"**{task['title']}**")
            st.write(f"Description: {task['description']}")
            st.write(f"Due Date: {task['dueDate']}")
            st.write(f"Priority: {task['priority']}")
            st.write("---")

except:
    st.error("Cannot connect to backend server")