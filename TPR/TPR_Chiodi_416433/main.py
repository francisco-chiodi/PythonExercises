"""Pido disculpas en mi entrega anterior no estaba ordenandose en todo momento el vector porque implemente mal mi
funcion de ordenamiento, ordene todo al final con seleccion directa y cuando me puse a practicar para el recuperatorio
me volvi a encontrar con la funcion de insercion ordenada con busqueda binaria, que cumple correctamente e hice la revision.
"""

import os
import pickle
import clases

ARCHIVO_CSV = 'papers.csv'
ARCHIVO_BIN = 'resumen.dat'
def anadir_orden(v, paper):
    izq = 0
    der = len(v) - 1
    pos = 0
    while izq <= der:
        medio = (izq + der) // 2
        if v[medio].id_paper == paper.id_paper:
            pos = medio
            break
        if paper.id_paper < v[medio].id_paper:
            der = medio - 1
        else:
            izq = medio + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [paper]

def procesar_archivo():
    datos = []

    if os.path.exists(ARCHIVO_CSV):
        archivo = open(ARCHIVO_CSV, 'rt')
        cabecera = True

        for linea in archivo:
            if cabecera:
                cabecera = False
                continue #recordamos que continue vive dentro del for, entonces si bien ignora el resto del codigo , la segunda vuelta
                #del for ocurrira y alli la cabezera ya fue saltada(que es la primer linea leida).
            else:
                linea = linea.strip()
                campos = linea.split(';')
                id_paper = campos[0]
                titulo = campos[1]
                autor = campos[2]
                motivo = int(campos[3])
                obviedad = int(campos[4])

                nuevo_paper = clases.Paper(id_paper, titulo, autor, motivo, obviedad)
                anadir_orden(datos, nuevo_paper)

        archivo.close()
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

def opcion_3(v):

    conteo = [[0] * 5 for i in range(6)]#Mi Nota: filas (0-5 motivos), columnas (0-4 obviedades)

    for paper in v:
        f = paper.motivo - 1 #ajusto indices
        c = paper.obviedad - 1
        conteo[f][c] += 1

    archivo_bin = open(ARCHIVO_BIN, 'wb')
    cant_guardados = 0

    for f in range(6):
        for c in range(5):
            if conteo[f][c] > 0:
                desc_m = clases.MOTIVOS[f]
                desc_o = clases.OBVIEDADES[c]
                totalclass = clases.Totalizador(desc_m, f + 1, c + 1, desc_o, conteo[f][c]) #ajusto indices, cargo
                pickle.dump(totalclass, archivo_bin)
                cant_guardados += 1

    archivo_bin.close()
    print('r.3.1:', cant_guardados)

    print('r.3.2:')
    if os.path.exists(ARCHIVO_BIN):
        tam = os.path.getsize(ARCHIVO_BIN)
        if tam > 0:
            archivo_bin = open(ARCHIVO_BIN, 'rb')

            primer_registro = pickle.load(archivo_bin)
            cantidad_base = primer_registro.cantidad
            archivo_bin.seek(0)#vuelvo al inicio el puntero

            while archivo_bin.tell() < tam:
                registro = pickle.load(archivo_bin)
                if registro.cantidad >= cantidad_base:
                    print(
                        f"Motivo: {registro.desc_motivo} ({registro.nro_motivo}), Obviedad: {registro.nro_obviedad}, Cantidad: {registro.cantidad}")

            archivo_bin.close()

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
        print('r.4.1: El paper no existe')

def menu():
    print('=== Menú de opciones ===')
    print('1. Cargar papers')
    print('2. Listar cinco papers por obviedad')
    print('3. Totalizar por motivo y obviedad')
    print('4. Buscar paper')
    print('0. Salir')
    n = int(input('Ingrese opción: '))
    return n

def principal():
    opcion = -1
    papers = []
    while opcion != 0:
        opcion = menu()

        if opcion == 1:
            papers = procesar_archivo()
            mostrar_r1_1(papers)
            mostrar_r1_2(papers)

        elif opcion == 2:
            if not papers:
                print("Primero debe cargar los datos")
            else:
                opcion_2(papers)

        elif opcion == 3:
            if not papers:
                print("Primero debe cargar los datos")
            else:
                opcion_3(papers)

        elif opcion == 4:
            if not papers:
                print("Primero debe cargar los datos ")
            else:
                id_buscado = input('Ingrese ID a buscar: ')
                opcion_4(papers, id_buscado)

#mis salidas no se muestran perfectamente alineadas, pero la consigna pide no tocar la clase paper y priorice seguirla.
#gracias por todo! por su tiempo y dedicacion. es increible esta facultad.

if __name__ == '__main__':
    principal()