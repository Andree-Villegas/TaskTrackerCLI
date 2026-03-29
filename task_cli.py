import sys
from tasks import add_task, list_tasks

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

if __name__ == "__main__":
    main()