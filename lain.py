beneficiario = input("Ingrese nombre completo")
codigo = input("Ingrese ICD10 X##.##: ") #L00-L99  #P00–P96
monto_base = int(input("Ingrese un monto base"))

letra = codigo[0]
bloque = int(codigo[1] + codigo[2])

if codigo < len(codigo[6]):
    codigo
# Obtención del porcentaje


porcentaje = int(codigo[5])

monto_final = monto_base + 25000

if "A" <= letra <= "L":
    monto_final += 25000
elif letra == "U":
    monto_final += 100000
elif "M" <= letra <= "Z":
    monto_final += 40000

monto_final += monto_final * porcentaje / 100

# Determinación del capítulo
if letra == "A" or letra == "B":
    capitulo = "Capítulo I: Ciertas enfermedades infecciosas y parasitarias"
elif letra == "C":
    capitulo = "Capítulo II: Neoplasias[neoplasias]"
elif letra == "D":
    if bloque <= 48:
        capitulo = "Capítulo II: Neoplasias[neoplasias]"
    else:
        capitulo = "Capítulo III: Enfermedades de la sangre y de los órganos hematopoyéticos y ciertos trastornos que afectan el mecanismo de la inmunidad"
elif letra == "E":
    capitulo = "Capítulo IV: Enfermedades endocrinas, nutricionales y metabólicas"
elif letra == "F":
    capitulo = "Capítulo V: Trastornos mentales y del comportamiento"
elif letra == "G":
    capitulo = "Capítulo VI: Enfermedades del sistema nervioso"
elif letra == "H":
    if bloque <= 59:
        capitulo = "Capítulo VII: Enfermedades del ojo y sus anexos"
    else:
        capitulo = "Capítulo VIII: Enfermedades del oído y de la apófisis mastoides"
elif letra == "I":
    capitulo = "Capítulo IX: Enfermedades del sistema circulatorio"
elif letra == "J":
    capitulo = "Capítulo X: Enfermedades del sistema respiratorio"
elif letra == "K":
    capitulo = "Capítulo XI: Enfermedades del sistema digestivo"
elif letra == "L":
    capitulo = "Capítulo XII: Enfermedades de la piel y del tejido subcutáneo"
elif letra == "M":
    capitulo = "Capítulo XIII: Enfermedades del sistema osteomuscular y del tejido conjuntivo"
elif letra == "N":
    capitulo = "Capítulo XIV: Enfermedades del sistema genitourinario"
elif letra == "O":
    capitulo = "Capítulo XV: Embarazo, parto y puerperio"
elif letra == "P":
    capitulo = "Capítulo XVI: Ciertas afecciones originadas en el período perinatal"
elif letra == "Q":
    capitulo = "Capítulo XVII: Malformaciones congénitas, deformidades y anomalías cromosómicas"
elif letra == "R":
    capitulo = "Capítulo XVIII: Síntomas, signos y hallazgos anormales clínicos y de laboratorio, no clasificados en otra parte"
elif letra == "S" or letra == "T":
    capitulo = "Capítulo XIX: Traumatismos, envenenamientos y algunas otras consecuencias de causas externas"
elif letra == "V" or letra == "W" or letra == "X" or letra == "Y":
    capitulo = "Capítulo XX: Causas externas de morbilidad y de mortalidad"
elif letra == "Z":
    capitulo = "Capítulo XXI: Factores que influyen en el estado de salud y contacto con los servicios de salud"
elif letra == "U":
    capitulo = "Capítulo XXII: Códigos para propósitos especiales"
else:
    capitulo = "Capítulo no válido"



print("Beneficiario:", beneficiario)
print("Codigo:", codigo)
print("Capitulo:", capitulo)
print("Monto a pagar:", monto_final)
