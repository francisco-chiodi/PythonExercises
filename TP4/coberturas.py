class Afiliado:
    def __init__(self, dni, cod_obra_social, nivel_cobertura, tope_atencion):
        self.dni = dni
        self.cod_obra_social = cod_obra_social
        self.nivel_cobertura = nivel_cobertura
        self.tope_atencion = tope_atencion

    def __str__(self):
        return f"DNI: {self.dni} - Obra Social: {self.cod_obra_social} - Nivel: {self.nivel_cobertura} - Tope: {self.tope_atencion}"


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
        return f"DNI: {self.dni} - Nombre: {self.nombre} {self.apellido} - ICD10: {self.cod_icd10} - Monto Base: {self.monto_base} - Complejidad: {self.alta_complejidad} - ID Algoritmo: {self.id_algoritmo}"

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
            # Algoritmo normal TP1
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


def procesar_codigo_icd10(cod_icd10):
    paso_punto = False
    letra = ''
    str_clasificacion = ''
    str_porcentaje = ''

    for car in cod_icd10:
        if car != ' ':
            if 'A' <= car <= 'Z' and letra == '':
                letra = car
            elif '0' <= car <= '9' and not paso_punto:
                str_clasificacion += car
            elif car == '.':
                paso_punto = True
            elif '0' <= car <= '9' and paso_punto:
                str_porcentaje += car

    clasificacion = int(str_clasificacion) if str_clasificacion != '' else 0
    porcentaje = int(str_porcentaje) if str_porcentaje != '' else 0

    return letra, clasificacion, porcentaje


def obtener_porcentaje_cobertura(nivel_cobertura, alta_complejidad):
    if nivel_cobertura == 1:
        return 0.40 if alta_complejidad == 'A' else 0.50
    elif nivel_cobertura == 2:
        return 0.60 if alta_complejidad == 'A' else 0.70
    elif nivel_cobertura == 3:
        return 0.80 if alta_complejidad == 'A' else 0.90
    return 0.0


def calcular_cobertura_tratamiento(monto_final, alta_complejidad, afiliado):
    if afiliado is None:
        return 0.0, monto_final, False

    pct = obtener_porcentaje_cobertura(afiliado.nivel_cobertura, alta_complejidad)
    monto_cubierto_calculado = monto_final * pct

    se_aplico_tope = False
    if monto_cubierto_calculado > afiliado.tope_atencion:
        monto_cubierto = afiliado.tope_atencion
        se_aplico_tope = True
    else:
        monto_cubierto = monto_cubierto_calculado

    monto_no_cubierto = monto_final - monto_cubierto
    return monto_cubierto, monto_no_cubierto, se_aplico_tope