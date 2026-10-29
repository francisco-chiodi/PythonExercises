def longitud_primer_sector(t):
    if len(t) <= 1:
        return len(t)

    if t[0] == t[1]:
        return 1 + longitud_primer_sector(t[1:])

    return 1


def contar_sectores(t):
    if len(t) <= 1:
        return len(t)

    if t[0] != t[1]:
        return 1 + contar_sectores(t[1:])

    return contar_sectores(t[1:])


def mayor_longitud(t):
    if len(t) == 0:
        return 0

    n = longitud_primer_sector(t)

    m = mayor_longitud(t[1:])

    if n > m:
        return n
    else:
        return m

def principal():
    arch = open('copia.txt', 'rt')
    cadena = arch.read().strip()
    arch.close()

    long_primer = longitud_primer_sector(cadena)
    cant_sectores = contar_sectores(cadena)
    max_long = mayor_longitud(cadena)

    print('1.) Longitud del primer sector:', long_primer)
    print('2.) Cantidad total de sectores:', cant_sectores)
    print('3.) Longitud del sector más largo:', max_long)


if __name__ == '__main__':
    principal()