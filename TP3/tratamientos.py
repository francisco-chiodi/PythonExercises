class Tratamiento:
    def __init__(self, dni, nombre, apellido, cod_icd10, monto_base, alta_complejidad, id_algoritmo):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.cod_icd10 = cod_icd10 
        self.monto_base = monto_base
        self.alta_complejidad = alta_complejidad
        self.id_algoritmo = id_algoritmo

    def __str__(self):
        return f'DNI: {self.dni} - Nombre: {self.nombre} - Apellido: {self.apellido} - CODICD10: {self.cod_icd10} - Monto: {self.monto_base} - Complejidad: {self.alta_complejidad} - ID Algoritmo: {self.id_algoritmo}'

    def calcular_monto_final(self):
       
        letra, clasificacion, porcentaje_icd10 = procesar_codigo_icd10(self.cod_icd10)
        
        porcentaje_extra_normal = (self.monto_base * porcentaje_icd10) / 100

        if self.id_algoritmo == 1:
            if self.monto_base <= 60000:
                porcentaje_extra = 0
            else:
                porcentaje_extra = porcentaje_extra_normal

            suma_fija = 0
            if self.alta_complejidad == 'A' and letra != 'U':
                suma_fija = self.monto_base / 2

            monto_final = self.monto_base + porcentaje_extra + suma_fija

        elif self.id_algoritmo == 2:
            if 'A' <= letra <= 'P':
                porcentaje_extra = porcentaje_extra_normal
            else:
                if self.alta_complejidad == 'A':
                    porcentaje_extra = (self.monto_base * (porcentaje_icd10 * 2)) / 100
                else:
                    porcentaje_extra = self.monto_base * 0.15

            monto_final = self.monto_base + porcentaje_extra

        elif self.id_algoritmo == 3:
            monto_extra = 0
            if self.alta_complejidad == 'A':
                monto_extra = self.monto_base * 0.30

            if 'A' <= letra <= 'L':
                monto_extra += 20000
            elif 'M' <= letra <= 'P':
                monto_extra += 15000 + (5000 * clasificacion)
            else:
                monto_extra += self.monto_base * 0.10

            if monto_extra > 60000:
                monto_extra = 60000

            monto_final = self.monto_base + monto_extra
            
        else:
            monto_final = self.monto_base + 25000

            if 'A' <= letra <= 'L':
                monto_final += 25000
            elif 'M' <= letra <= 'Z' and letra != 'U':
                monto_final += 40000
            elif letra == 'U':
                monto_final += 100000

            monto_final += (monto_final * porcentaje_icd10) / 100

            if self.alta_complejidad == 'A':
                monto_final += (monto_final * 5) / 100

        return monto_final


def cargar_tratamientos(datos):
    dni = int(datos[0])
    nombre = datos[1]
    apellido = datos[2]
    cod_icd10 = datos[3]
    monto_base = float(datos[4])
    alta_complejidad = datos[5]
    id_algoritmo = int(datos[6])

    return Tratamiento(dni, nombre, apellido, cod_icd10, monto_base, alta_complejidad, id_algoritmo)



def procesar_codigo_icd10(cod_icd10):
    bd_paso_punto = False
    letra = ''
    clasificacion = ''
    porcentaje = ''

    for car in cod_icd10:
        if car != ' ':
            if 'A' <= car <= 'Z' and letra == '':
                letra = car

            elif '0' <= car <= '9' and not bd_paso_punto :
                clasificacion += car

            elif car == '.':
                bd_paso_punto = True

            elif '0' <= car <= '9' and bd_paso_punto:
                porcentaje += car
                if clasificacion != '':
                    clasificacion = int(clasificacion)
                else:
                    clasificacion = 0

                    if porcentaje != '':
                        porcentaje = int(porcentaje)
                    else:
                        porcentaje = 0

    return letra, clasificacion, int(porcentaje)
