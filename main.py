"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md

import sys
from todo_manager import read_todo_file, write_todo_file

def main():
    """sin argumentos"""
    if len(sys.argv) < 2:
        print("Insufficient arguments provided!")
        return

    """Adyuda"""
    if sys.argv[1] == "--help":
        print("""age: python main.py <file_path> <command> [arguments]...
              
        Commands:
        add "task"    - Add a task to the list.
        remove "task" - Remove a task from the list.
        view          - Display all tasks.
              
        Examples:
        python main.py tasks.txt add "Buy groceries"
        python main.py tasks.txt remove "Do laundry"
        python main.py tasks.txt view
        python main.py tasks.txt add "Call mom" remove "Take out trash" view""")
        return
    

    file_path = sys.argv[1]

    """Archivo vacio"""
    if len(sys.argv) == 2:
        return

    """Comando"""
    command = sys.argv[2]

    if command == "view":
        tasks = read_todo_file(file_path)
        print("Tasks:")
        for task in tasks:
            print(task)

    elif command == "add":
        if len(sys.argv) < 4:
            print('Task description required for "add".')
            return
        task_description = sys.argv[3]
        tasks = read_todo_file(file_path)
        tasks.append(task_description)
        write_todo_file(file_path, tasks)
        print(f'Task "{task_description}" added.')

    elif command == "remove":
        if len(sys.argv) < 4:
            print('Task description required for "remove".')
            return
        task_description = sys.argv[3]
        tasks = read_todo_file(file_path)
        if task_description in tasks:
            tasks.remove(task_description)
            write_todo_file(file_path, tasks)
            print(f'Task "{task_description}" removed.')
        else:
            print(f'Task "{task_description}" not found.')

    elif command == "--help":
        print("Usage: python main.py <file_path> <command> [arguments]...")

    else:
        print("Command not found!")

if __name__ == "__main__":
    main()