def son_opuestos(apertura, cierre):
    if apertura == "(" and cierre == ")":
        return True
    if apertura == "[" and cierre == "]":
        return True
    if apertura == "{" and cierre == "}":
        return True
    return False


def verificar_equilibrio(expresion):
    p = []
    error = False

    for s in expresion:
        if s in "([{":
            p.append(s)
        elif s in ")]}":
            if len(p) == 0:
                print("Sobran cierres")
                error = True
                break
            else:
                ps = p.pop()
                if not son_opuestos(ps, s):
                    print("Desequilibrio interno")
                    error = True
                    break



    if not error:
        if len(p) > 0:
            print("Sobran aperturas")
        else:
            print("Ok")

def extraer_simbolos(expresion):
    q = []
    for s in expresion:
        if s in "()[]{}":
            q.append(s)

    print("Cola de símbolos:", q)
    cadena_simbolos = "".join(q)
    print("Cadena de símbolos:", cadena_simbolos)


def principal():
    m = open("expresiones.txt", "rt")
    nro_linea = 1

    for linea in m:
        expresion = linea.rstrip("\n")

        print(f"--- Expresión {nro_linea}: {expresion} ---")
        verificar_equilibrio(expresion)
        extraer_simbolos(expresion)
        print()

        nro_linea += 1

    m.close()


if __name__ == "__main__":
    principal()