# Este archivo maneja la persistencia de datos en JSON
import json, os
TASKS_FILE = "tareas.json" 

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return[]
    with open(TASKS_FILE, "r") as f: 
        return json.load(f)
    
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)
