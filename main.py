"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md

import sys
from todo_manager import read_todo_file, write_todo_file

def main():
   
    if len(sys.argv) < 2:
        print("Insufficient arguments provided!")
        return

    args = sys.argv[1:]

    print("Command-line arguments:")
    for arg in args:
        print(arg)

    file_path = args[0]
    tasks = read_todo_file(file_path)

    print("\nTasks:")
    for task in tasks:
        print(task)

if __name__ == "__main__":
    main()