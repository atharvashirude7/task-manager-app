from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Enable CORS (important for Streamlit)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data model
class Task(BaseModel):
    title: str
    description: str
    dueDate: str
    priority: str

tasks = []

# Add task
@app.post("/add-task")
def add_task(task: Task):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "description": task.description,
        "dueDate": task.dueDate,
        "priority": task.priority
    }
    tasks.append(new_task)
    return {"message": "Task added successfully", "task": new_task}

# Get all tasks
@app.get("/tasks")
def get_tasks():
    return tasks
# Add task
@app.route('/add-task', methods=['POST'])
def add_task():
    data = request.json

    new_task = {
        "id": len(tasks) + 1,
        "title": data.get("title"),
        "description": data.get("description"),
        "dueDate": data.get("dueDate"),
        "priority": data.get("priority")
    }

    tasks.append(new_task)

    return jsonify({
        "message": "Task added successfully",
        "task": new_task
    })


# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)


if __name__ == '__main__':
    app.run(debug=True, port=5000)