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