import soporte

__author__ = 'Cátedra de AED'
def media(v):
    n = len(v)
    a = 0
    for x in v:
        a += x
    return round(a / n, 2)


def mediana(v):
    n = len(v)
    v_ord = list(v)
    v_ord.sort()

    if n % 2 != 0:
        c = n // 2
        med = v_ord[c]
    else:
        c_der = n // 2
        c_izq = c_der - 1
        med = round((v_ord[c_izq] + v_ord[c_der]) / 2, 2)

    return med
#moda 0?

def moda(v):
    n = len(v)
    c = n * [0]

    for x in v:
        c[x] += 1

    idm = 0
    cfm = 1

    for i in range(1, n):
        if c[i] > c[idm]:
            idm = i
            cfm = 1
        elif c[i] == c[idm]:
            cfm += 1


    if cfm == 1:
        val_moda = idm
    else:
        val_moda = None

    return val_moda


def principal():
    n = 3000
    v = soporte.vector_known_range(n)
    val_media = media(v)
    val_mediana = mediana(v)
    val_moda = moda(v)

    print('Resultados del Desafío 04:')
    print('1.) Media:', val_media)
    print('2.) Mediana:', val_mediana)
    print('3.) Moda:', val_moda)

if __name__ == '__main__':
    principal()