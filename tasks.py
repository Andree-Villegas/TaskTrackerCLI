# Se define la lógica de negocio, cómo se crean y gestionan las tareas.
from datetime import datetime
from storage import load_tasks, save_tasks

def add_task(description):
    tasks = load_tasks()
    new_id = max([t["id"] for t in tasks], default=0) + 1
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

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updateAt"] = datetime.now().isoformat(timespec="seconds")
            save_tasks(tasks)
            return f"Tarea {task_id} actualizada exitosamente"
    return f"Tara con ID {task_id} no encontrada"       

def delete_task(task_id):
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            save_tasks(tasks)
            return f"Tarea {task_id} eliminada exitosamente"
    return f"Tarea con ID {task_id} no encontrada"

def mark_task(task_id, new_status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updateAt"] = datetime.now().isoformat(timespec="seconds")
            save_tasks(tasks)
            return f"Tarea {task_id} marcada como {new_status}"
    return f"Tarea con ID {task_id} no encontrada"
