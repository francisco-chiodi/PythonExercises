"""
Enunciado y Consignas:

En este Desafío 03 se propone el desarrollo y prueba de un programa que implemente funciones recursivas simples para
 resolver el problema del conteo de sectores.

Una expedición ha registrado la dureza del terreno que está explorando, mediante una cadena compuesta por letras
mayúsculas y números. Cada letra/número representa un tipo de suelo, y los tramos iguales consecutivos forman un sector.
 En este desafío se pedirá programar funciones recursivas para procesar esa cadena y obtener algunos resultados.

Ejemplo: la cadena "AAABBBCCCCCBAAADD" tiene 6 sectores: "AAA", "BBB", "CCCCC", "B", "AAA" y "DD".

Consigna completa:
Desarrollar un programa en Python que tome una cadena que representa un terreno (en forma similar al ejemplo anterior)
y aplique sobre ella tres funciones recursivas para obtener los siguientes resultados:

1.) Longitud del primer sector representado en la cadena (en el ejemplo anterior, esa longitud es 3).

2.) Cantidad total de sectores que tiene la cadena (en el ejemplo anterior, como ya se indicó, hay 6 sectores).

3.) Longitud de segmento más largo de la cadena (en el ejemplo anterior, la mayor longitud es 5 [el sector "CCCCC"].

La cadena a procesar debe ser leída desde el archivo de texto copia.txt (haga click en el nombre del archivo para
 descargarlo) en forma similar a lo hecho para cargar las cadenas a procesar en el Parcial 2 de la materia.

Cada alumno tendrá 5 intentos disponibles para cargar sus respuestas correctas, y como siempre, quedará como nota
 final la mayor que haya obtenido.

A continuación, le dejamos un breve y muy general esquema de pseudocódigo para el planteo de cada una de las funciones
 pedidas. Puede mirar estos pseudocódigos si lo desea o le hace falta, o puede no mirarlo e intentar resolver el problem
 a con sus propias ideas. Y por supuesto, estos pseudocódigos no muestran el proceso para el Desafío 03 completo,
 sino solo para las funciones pedidas y con un  nivel de detalle que requiere que el estudiante haga un esfuerzo para obtener el código fuente definitivo.

Es absolutamente obvio que cualquiera de ustedes puede resolver este problema sin usar recursión. Es absolutamente obvio
 que pueden pedirle a una IA que programe por ustedes. Es absolutamente obvio que simplemente pueden copiarle el
 programa y sus respuestas a otro alumno que ya lo tenga hecho. Nadie controlará eso en un desafío. Pero el objetivo
 es que apliquen recursividad y trabajen en forma responsable. Si no lo hacen... pues... es problema de ustedes.

# longitud del primer sector (recursiva)
def longitud_primer_sector(t):
    1.) Si la longitud de t es 0 o 1 retornar esa longitud y terminar.
    2.) Si los dos primeros caracteres de t son iguales:
        2.1.) Retornar 1 + la longitud del primer sector de t pero sin incluir el primer caracter.
    3.) Retornar 1 si llegó hasta aquí.

# conteo de sectores (recursiva)
def contar sectores(t):
    1.) Si la longitud de t es 0 o 1 retornar esa longitud y terminar.
    2.) Si los dos primeros caracteres de t son diferentes:
        2.1.) Retornar 1 + la cantidad de sectores de t pero sin incluir el primer caracter.
    3.) Retornar la cantidad de sectores de t pero sin incluir el primer caracter si llegó hasta aquí.


# longitud del sector más largo (recursiva)
def mayor_longitud(t):
    1.) Si la longitud de t es 0 retornar 0 y terminar.
    2.) Sea n la longitud del primer sector de t.
    3.) Retornar el mayor entre n y la mayor longitud en t pero sin incluir el primer caracter.

Tómese su tiempo para tratar de entender estas funciones. La primera línea de cada una de ellas es el control de
los casos base (no recursivos). Está claro que podrían aplicarse procesos que no empleen recursividad y posiblemente
esos procesos sería más eficientes. Pero este desafío es para aplicar recursividad. No dejen pasar la oportunidad de hacerlo.

Que lo disfruten.

"""