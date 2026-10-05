import os 
import tratamientos

DIR_ACTUAL = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(DIR_ACTUAL, 'tratamientos.csv')

#PUNTO 2.4
def det_dni_mayor_complejidad(v):
    mayor_alta_complejidad = v[0]

    for tratamiento in v:
        if tratamiento.alta_complejidad == 'A':
            if tratamiento.calcular_monto_final() > mayor_alta_complejidad.calcular_monto_final():
                mayor_alta_complejidad = tratamiento

    return mayor_alta_complejidad.dni
            

#PUNTO 2.2 y 2.3
def det_letra_destacada(v):
    cantidad = 0
    letra_destacada = ''
    contador = [0] * 26
    for tratamiento in v:
        letra, clasificacion, porcentaje = tratamientos.procesar_codigo_icd10(tratamiento.cod_icd10) 
        if 'A' <= letra <= 'Z':
            contador[ord(letra) - ord('A')] += 1

    for i in range(26):
        if contador[i] > cantidad:
            cantidad = contador[i]
            letra_destacada = chr(i + ord('A'))

    return letra_destacada, cantidad

#PUNTO 2.1
def calcular_promedio(total, cantidad):
    if cantidad != 0:
        return round(total / cantidad, 2)
    return 0

def calcular_monto_final(v):
    total_monto_base = total_monto_final =  0
    for tratamiento in v:
        total_monto_final += tratamiento.calcular_monto_final()
        total_monto_base += tratamiento.monto_base 

    return total_monto_base, total_monto_final

#PUNTO 1
def contar_tratamientos(v):
    cant_tratamientos = 0

    for tratamiento in v:
        cant_tratamientos += 1
    return cant_tratamientos

def determinar_quinto_tratamiento(v):
    cant_alta_complejidad = 0

    for tratamiento in v:
        if tratamiento.alta_complejidad == 'A':
            cant_alta_complejidad += 1

        if cant_alta_complejidad == 5:
            return tratamiento.apellido
        
    return 'No hay suficientes tratamientos de alta complejidad.'


def procesar_archivo():
  datos = []
  linea = []

  if os.path.exists(ARCHIVO):
      archivo = open(ARCHIVO, 'rt')
      cabecera = True
      for linea in archivo:
          if cabecera:
              cabecera = False
              continue
          else:
              linea = tratamientos.cargar_tratamientos(linea.strip().split(','))
              datos.append(linea)

      archivo.close()

  return datos
              
def menu():
    print('1.Cargar Tratamientos')
    print('2.Mostrar Resultados')
    print('0.Salir')
    n = int(input('Ingrese opcion: '))
    return n


def principal():
    opc = -1
    tratamientos = []
    cant_tratamientos = 0
    total_base = total_final = 0
    letra_destacada = ''
    cantidad_letra_destacada = 0
    dni_mayor_complejidad = 0

    while opc != 0:

        opc = menu()

        if opc == 1:
            tratamientos = procesar_archivo()
            cant_tratamientos = contar_tratamientos(tratamientos)
            print('r1.1:', cant_tratamientos)
            print('r1.2:', determinar_quinto_tratamiento(tratamientos))
        elif opc == 2:
            if not tratamientos:
                continue
            else:
                total_base, total_final = calcular_monto_final(tratamientos)
                dif_promedio = round(calcular_promedio(total_final, cant_tratamientos) - calcular_promedio(total_base, cant_tratamientos), 2)
                letra_destacada, cantidad_letra_destacada = det_letra_destacada(tratamientos)
                dni_mayor_complejidad = det_dni_mayor_complejidad(tratamientos)

                print('r.2.1:', dif_promedio)
                print('r.2.2:', letra_destacada)
                print('r.2.3:', cantidad_letra_destacada)
                print('r.2.4:', dni_mayor_complejidad)

if __name__ == '__main__':
    principal()