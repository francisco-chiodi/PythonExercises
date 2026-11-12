import os
import pickle
import Paper, Totalizador, MOTIVOS, OBVIEDADES


def add_in_order(papers, nuevo_paper):
    """Inserta un objeto Paper en el vector manteniendo el orden ascendente por id_paper."""
    pos = len(papers)
    for i in range(len(papers)):
        if nuevo_paper.id_paper < papers[i].id_paper:
            pos = i
            break
    papers.insert(pos, nuevo_paper)

def contar_vocales_titulo(titulo):
    """Cuenta cuántas palabras del título comienzan con vocal."""
    titulo_limpio = titulo.replace(".", "")
    palabras = titulo_limpio.split(" ")
    vocales = "aeiouAEIOU"
    cantidad = 0
    for palabra in palabras:
        if len(palabra) > 0 and palabra[0] in vocales:
            cantidad += 1
    return cantidad

def opcion_1():
    """Carga los papers desde el archivo CSV e imprime los resultados esperados."""
    papers = []

    if not os.path.exists('papers.csv'):
        print("El archivo papers.csv no existe en el directorio.")
        return papers

    with open('papers.csv', 'r', encoding='utf-8') as archivo:
        next(archivo)  # Saltar la primera línea (cabecera)
        for linea in archivo:
            campos = linea.strip().split(';')
            if len(campos) == 5:
                id_paper = campos[0]
                titulo = campos[1]
                autor = campos[2]
                motivo = int(campos[3])
                obviedad = int(campos[4])

                nuevo_paper = Paper(id_paper, titulo, autor, motivo, obviedad)
                add_in_order(papers, nuevo_paper)

    # r.1.1: Buscar los dos primeros con motivo == 3 y obviedad == 5
    encontrados_r1 = []
    for p in papers:
        if p.motivo == 3 and p.obviedad == 5:
            encontrados_r1.append(p)
            if len(encontrados_r1) == 2:
                break

    print("r.1.1:")
    if len(encontrados_r1) == 2:
        for p in encontrados_r1:
            print(p)
    else:
        print("Cantidad insuficiente")

    # r.1.2: Cantidad total de palabras que comienzan con vocal en los títulos
    total_vocales = 0
    for p in papers:
        total_vocales += contar_vocales_titulo(p.titulo)

    print(f"r.1.2: {total_vocales}")
    return papers


def opcion_2(papers):
    """Lista hasta 5 papers con obviedad 1 y muestra el mayor motivo entre ellos."""
    print("r.2.1:")
    mostrados = 0
    max_motivo = 0

    for p in papers:
        if p.obviedad == 1:
            print(p)
            if p.motivo > max_motivo:
                max_motivo = p.motivo
            mostrados += 1
            if mostrados == 5:
                break

    print(f"r.2.2: {max_motivo}")


def opcion_3(papers):
    """Genera matriz de conteo, guarda en archivo binario y muestra filtrados."""
    # a) Determinar cantidad de casos (matriz 6 motivos x 5 obviedades)
    matriz = [[0] * 5 for _ in range(6)]
    for p in papers:
        f = p.motivo - 1
        c = p.obviedad - 1
        matriz[f][c] += 1

    # b) Generar archivo binario resumen.dat
    cantidad_guardados = 0
    with open('resumen.dat', 'wb') as archivo_binario:
        for f in range(6):
            for c in range(5):
                if matriz[f][c] > 0:
                    tot = Totalizador(
                        desc_motivo=MOTIVOS[f],
                        nro_motivo=f + 1,
                        nro_obviedad=c + 1,
                        desc_obviedad=OBVIEDADES[c],
                        cantidad=matriz[f][c]
                    )
                    pickle.dump(tot, archivo_binario)
                    cantidad_guardados += 1

    print(f"r.3.1: {cantidad_guardados}")

    # c) Leer archivo y mostrar mayores o iguales al primer registro
    print("r.3.2:")
    if os.path.exists('resumen.dat') and os.path.getsize('resumen.dat') > 0:
        with open('resumen.dat', 'rb') as archivo_binario:
            # Leer el primero para obtener la cantidad base
            primer_registro = pickle.load(archivo_binario)
            cantidad_base = primer_registro.cantidad

            # Volver al inicio para el recorrido completo
            archivo_binario.seek(0)

            while archivo_binario.tell() < os.path.getsize('resumen.dat'):
                registro = pickle.load(archivo_binario)
                if registro.cantidad >= cantidad_base:
                    print(f"Motivo: {registro.desc_motivo} ({registro.nro_motivo}), "
                          f"Obviedad: {registro.nro_obviedad}, Cantidad: {registro.cantidad}")


def busqueda_binaria(papers, id_buscado):
    """Busca un paper por ID usando algoritmo de búsqueda binaria (el vector está ordenado)."""
    izq, der = 0, len(papers) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if papers[medio].id_paper == id_buscado:
            return medio
        elif papers[medio].id_paper < id_buscado:
            izq = medio + 1
        else:
            der = medio - 1
    return -1


def opcion_4(papers):
    """Busca un paper, lo muestra y modifica su obviedad si corresponde."""
    id_buscado = input("Ingrese ID a buscar: ")
    indice = busqueda_binaria(papers, id_buscado)

    if indice != -1:
        p = papers[indice]
        print(f"r.4.1: {p}")

        if p.obviedad == 1:
            p.obviedad = 5
            print(f"r.4.2: {p}")
        else:
            print("r.4.2: Sin cambios")
    else:
        print("r.4.1: Paper inexistente")


def main():
    papers = []
    opcion = -1

    while opcion != 0:
        print("\n=== Menú de opciones ===")
        print("1) Cargar papers")
        print("2) Listar cinco papers por obviedad")
        print("3) Totalizar por motivo y obviedad")
        print("4) Buscar paper")
        print("0) Salir")

        try:
            opcion = int(input("Ingrese opción: "))

            if opcion == 1:
                papers = opcion_1()
            elif opcion == 2:
                if len(papers) > 0:
                    opcion_2(papers)
                else:
                    print("Debe cargar los papers primero (Opción 1).")
            elif opcion == 3:
                if len(papers) > 0:
                    opcion_3(papers)
                else:
                    print("Debe cargar los papers primero (Opción 1).")
            elif opcion == 4:
                if len(papers) > 0:
                    opcion_4(papers)
                else:
                    print("Debe cargar los papers primero (Opción 1).")
            elif opcion == 0:
                print("Saliendo del programa...")
            else:
                print("Opción incorrecta. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.")


if __name__ == '__main__':
    main()