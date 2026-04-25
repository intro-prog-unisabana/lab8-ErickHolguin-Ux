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
    
    total_load = float(total_arg)
    num_supports = int(num_supports_arg)

    if num_supports == 0:
        print("Error: Cannot divide by zero! Supports must be greater than zero.")
        return
    
    load_per_support = total_load / num_supports
    print(f"Load per support point: {load_per_support:.2f} N")

if __name__ == "__main__":
    main()