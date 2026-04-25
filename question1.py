"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""

# TODO: Implementar según README.md
import sys

def main():
    if len(sys.argv) != 3:
        print("Error: Invalid input! Enter numeric values only.")
        return
    
    total_arg = sys.argv[1]
    num_supports_arg = sys.argv[2]

    if not total_arg.replace('.', '', 1).isdigit() or not num_supports_arg.isdigit():
        print("Error: Invalid input! Enter numeric values only.")
        return
    