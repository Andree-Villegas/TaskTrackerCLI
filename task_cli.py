import sys
from tasks import add_task, list_tasks, update_task, delete_task

def main():
    args = sys.argv[1:]
    if not args:
        print("No command provided")
        return
    
    command = args[0]
    if command == "add":
        description = " ".join(args[1:])
        print(add_task(description))
    elif command == "list":
        if len(args) > 1:
            list_tasks(args[1])
        else:
            list_tasks()
    elif command == "update":
        if len(args) < 3:
            print("Uso: update <id> <nueva descripción>")
        else:
            task_id = int(args[1])
            new_description = " ".join(args[2:])
            print(update_task(task_id, new_description))
    elif command == "delete":
        if len(args) < 2:
            print("Uso: delete <id>")
        else:
            task_id = int(args[1])
            print(delete_task(task_id))

if __name__ == "__main__":
    main()