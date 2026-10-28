"""

2. Cadena capicúa
Desarrollar un programa que cargue por teclado una cadena de caracteres y use una pila para
determinar si esa cadena es capicúa: esto es, queremos determinar si una cadena de caracteres
 que se recibe para analizar puede leerse igual en dirección izquierda–derecha que en dirección
  derecha–izquierda
"""
import stack


def cap(chain):
    # Instanciamos la clase Stack del módulo stack
    # Usamos un nombre de variable distinto (pila) para evitar conflictos
    pila = stack.Stack()

    for char in chain:
        pila.push(char)

    # invert debe inicializarse FUERA del bucle for
    invert = ""

    while not pila.is_empty():
        invert += pila.pop()

    return chain == invert


def main():
    t = input("ingrese cadena: ")
    if cap(t):
        print("clean")
    else:
        print("not")


if __name__ == "__main__":
    main()

def main():
    t = input("ingrese cadena")
    if cap(t):
        print("clean")
    else:
        print("not")

if __name__ == "__main__":
    main()