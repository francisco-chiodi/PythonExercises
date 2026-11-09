import os
import pickle
import clases

ARCHIVO_CSV = 'papers.csv'
ARCHIVO_BIN = 'resumen.dat'

def ordenar_vector(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].id_paper > v[j].id_paper:
                v[i], v[j] = v[j], v[i]


def procesar_archivo():
    datos = []

    if os.path.exists(ARCHIVO_CSV):
        archivo = open(ARCHIVO_CSV, 'rt')
        cabecera = True

        for linea in archivo:
            if cabecera:
                cabecera = False
                continue
            else:
                campos = linea.strip().split(';')
                id_paper = campos[0]
                titulo = campos[1]
                autor = campos[2]
                motivo = int(campos[3])
                obviedad = int(campos[4])

                nuevo_paper = clases.Paper(id_paper, titulo, autor, motivo, obviedad)
                datos.append(nuevo_paper)  # Carga simple al final

        archivo.close()

        # Una vez cargado completo, se ordena de menor a mayor por id_paper
        ordenar_vector(datos)

    return datos


def mostrar_r1_1(v):
    encontrados = []
    for paper in v:
        if paper.motivo == 3 and paper.obviedad == 5:
            encontrados.append(paper)
            if len(encontrados) == 2:
                break

    print('r.1.1:')
    if len(encontrados) == 2:
        for p in encontrados:
            print(p)
    else:
        print('Cantidad insuficiente')


def mostrar_r1_2(v):
    total_vocales = 0
    vocales = "aeiouAEIOU"

    for paper in v:
        titulo = paper.titulo
        palabra_actual = ""

        for car in titulo:
            if car != ' ' and car != '.':
                palabra_actual += car
            else:
                if len(palabra_actual) > 0:
                    if palabra_actual[0] in vocales:
                        total_vocales += 1
                palabra_actual = ""

    print('r.1.2:', total_vocales)


# Punto 2
def opcion_2(v):
    print('r.2.1:')
    mostrados = 0
    mayor_motivo = -1

    for paper in v:
        if paper.obviedad == 1:
            print(paper)
            if paper.motivo > mayor_motivo:
                mayor_motivo = paper.motivo

            mostrados += 1
            if mostrados == 5:
                break

    print('r.2.2:', mayor_motivo)


# Punto 3
def opcion_3(v):
    # a) Generar matriz de conteo (6 motivos x 5 obviedades)
    conteo = [[0] * 5 for i in range(6)]

    for paper in v:
        f = paper.motivo - 1
        c = paper.obviedad - 1
        conteo[f][c] += 1

    # b) Grabar el archivo binario usando pickle
    archivo_bin = open(ARCHIVO_BIN, 'wb')
    cant_guardados = 0

    for f in range(6):
        for c in range(5):
            if conteo[f][c] > 0:
                desc_m = clases.MOTIVOS[f]
                desc_o = clases.OBVIEDADES[c]
                tot = clases.Totalizador(desc_m, f + 1, c + 1, desc_o, conteo[f][c])
                pickle.dump(tot, archivo_bin)
                cant_guardados += 1

    archivo_bin.close()
    print('r.3.1:', cant_guardados)

    # c) Mostrar filtrando por la cantidad del primer registro
    print('r.3.2:')
    if os.path.exists(ARCHIVO_BIN):
        tam = os.path.getsize(ARCHIVO_BIN)
        if tam > 0:
            archivo_bin = open(ARCHIVO_BIN, 'rb')

            # Leer solo el primero para obtener la cantidad a comparar
            primer_registro = pickle.load(archivo_bin)
            cantidad_base = primer_registro.cantidad

            # Volver el cursor al principio para recorrer todo de nuevo
            archivo_bin.seek(0)

            while archivo_bin.tell() < tam:
                registro = pickle.load(archivo_bin)
                if registro.cantidad >= cantidad_base:
                    print(
                        f"Motivo: {registro.desc_motivo} ({registro.nro_motivo}), Obviedad: {registro.nro_obviedad}, Cantidad: {registro.cantidad}")

            archivo_bin.close()


# Punto 4
def opcion_4(v, id_buscado):
    encontrado = False

    for paper in v:
        if paper.id_paper == id_buscado:
            encontrado = True
            print('r.4.1:', paper)

            if paper.obviedad == 1:
                paper.obviedad = 5
                print('r.4.2:', paper)
            else:
                print('r.4.2: Sin cambios')
            break

    if not encontrado:
        print('r.4.1: Paper inexistente')


# Menú y Main
def menu():
    print('\n=== Menú de opciones ===')
    print('1) Cargar papers')
    print('2) Listar cinco papers por obviedad')
    print('3) Totalizar por motivo y obviedad')
    print('4) Buscar paper')
    print('0) Salir')
    n = int(input('Ingrese opción: '))
    return n


def principal():
    opc = -1
    papers = []

    while opc != 0:
        opc = menu()

        if opc == 1:
            papers = procesar_archivo()
            mostrar_r1_1(papers)
            mostrar_r1_2(papers)

        elif opc == 2:
            if not papers:
                print("Primero debe cargar los datos (Opción 1)")
            else:
                opcion_2(papers)

        elif opc == 3:
            if not papers:
                print("Primero debe cargar los datos (Opción 1)")
            else:
                opcion_3(papers)

        elif opc == 4:
            if not papers:
                print("Primero debe cargar los datos (Opción 1)")
            else:
                id_buscado = input('Ingrese ID a buscar: ')
                opcion_4(papers, id_buscado)


if __name__ == '__main__':
    principal()