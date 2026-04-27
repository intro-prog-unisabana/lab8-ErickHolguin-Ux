"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md

import sys
from todo_manager import read_todo_file, write_todo_file

def main():
    try:
        """No brinda Argumentos"""
        if len(sys.argv) < 2:
            print("Insufficient arguments provided!")
            return

        """Información de ayuda"""
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

        """Archivo vacio"""
        if len(sys.argv) == 2:
            write_todo_file(file_path, tasks)  
            return

        """Programa main y comandos"""
        i = 2
        while i < len(sys.argv):
            command = sys.argv[i]

            if command == "view":
                print("Tasks:")
                for task in tasks:
                    print(task)
                i += 1

            elif command == "add":
                if i + 1 >= len(sys.argv):
                    print('Task description required for "add".')
                    return
                task_description = sys.argv[i + 1]
                tasks.append(task_description)
                print(f'Task "{task_description}" added.')

                """Guarda inmediatamente al finalizar"""
                write_todo_file(file_path, tasks)
                i += 2

            elif command == "remove":
                if i + 1 >= len(sys.argv):
                    print('Task description required for "remove".')
                    return
                task_description = sys.argv[i + 1]
                if task_description in tasks:
                    tasks.remove(task_description)
                    print(f'Task "{task_description}" removed.')
                else:
                    print(f'Task "{task_description}" not found.')

                """Guarda inmediatamente al finalizar"""
                write_todo_file(file_path, tasks)
                i += 2

            else:
                print("Command not found!")
                return
    
    except Exception as e:
        """Error Inesperado"""
        print(e)

if __name__ == "__main__":
    main()
