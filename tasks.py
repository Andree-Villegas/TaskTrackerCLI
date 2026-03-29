# Se define la lógica de negocio, cómo se crean y gestionan las tareas.
from datetime import datetime
from storage import load_tasks, save_tasks

def add_task(description):
    tasks = load_tasks()
    new_id = len(tasks) + 1
    now = datetime.now().isoformat(timespec="seconds")
    task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt" : now,
        "updateAt" : now
    }
    tasks.append(task)
    save_tasks(tasks)
    return f"Tarea añadida exitosamente (ID: {new_id})"

def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [t for t in tasks if t["status"] == status]
    if not tasks:
        print("No tasks found")
        return
    for task in tasks:
        print(f"[{task["id"]}] {task["description"]} - {task["status"]}")