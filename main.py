"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md

import sys
from todo_manager import read_todo_file, write_todo_file

def main():
    try:
        """Sin argumentos"""
        if len(sys.argv) < 2:
            raise IndexError("Insufficient arguments provided!")

        """Apartado Help"""
        if sys.argv[1] == "--help":
            print(
                "Usage: python main.py <file_path> <command> [arguments]...\n"
                "\n"
                "Commands:\n"
                "  add \"task\"    - Add a task to the list.\n"
                "  remove \"task\" - Remove a task from the list.\n"
                "  view          - Display all tasks.\n"
                "\n"
                "Examples:\n"
                "  python main.py tasks.txt add \"Buy groceries\"\n"
                "  python main.py tasks.txt remove \"Do laundry\"\n"
                "  python main.py tasks.txt view\n"
                "  python main.py tasks.txt add \"Call mom\" remove \"Take out trash\" view"
            )
            return

        file_path = sys.argv[1]
        tasks = read_todo_file(file_path)

        """Archivo Vacio"""
        if len(sys.argv) == 2:
            write_todo_file(file_path, tasks)  # asegura que el archivo exista
            return

        """Uso del comando"""
        command = sys.argv[2]

        if command == "view":
            print("Tasks:")
            for task in tasks:
                print(task)

        elif command == "add":
            if len(sys.argv) < 4:
                raise IndexError('Task description required for "add".')
            task_description = sys.argv[3]
            tasks.append(task_description)
            print(f'Task "{task_description}" added.')
            print("Tasks:")
            for task in tasks:
                print(task)

        elif command == "remove":
            if len(sys.argv) < 4:
                raise IndexError('Task description required for "remove".')
            task_description = sys.argv[3]
            if task_description in tasks:
                tasks.remove(task_description)
                print(f'Task "{task_description}" removed.')
            else:
                print(f'Task "{task_description}" not found.')

        else:
            raise ValueError("Command not found!")

        """Adjunta todo lo guardado"""
        write_todo_file(file_path, tasks)

    except (IndexError, ValueError) as e:
        print(e)

if __name__ == "__main__":
    main()