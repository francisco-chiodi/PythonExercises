def persistencia(num):
    secuencia = [num]
    pasos = 0
    while num >= 10:
        producto = 1
        temp = num
        while temp > 0:
            dig = temp % 10
            producto = producto * dig
            temp = temp // 10
        num = producto
        secuencia.append(num)
        pasos += 1
    return pasos, secuencia

mayor_persistencia = -1
numero_mayor = None
secuencia_mayor = []

for n in range(4000, 7001):
    pasos, secuencia = persistencia(n)
    if pasos > mayor_persistencia:
        mayor_persistencia = pasos
        numero_mayor = n
        secuencia_mayor = secuencia

print("Número con mayor valor de persistencia:", numero_mayor)
print("Persistencia del", numero_mayor, ":", mayor_persistencia)
print("Secuencia de productos para el", numero_mayor, ":",
      "(" + ", ".join(str(x) for x in secuencia_mayor) + ")")