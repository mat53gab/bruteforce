import time

mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
simbolos = "!@#$%&*"
alphabeths = mayusculas + minusculas + numeros + simbolos

def bruteforce(contraseña):
    intentos = 0
    inicio = time.time()
    
    for a in alphabeths:
        intentos += 1
        if a == contraseña:
            print("Contraseña encontrada:", a)
            print("Intentos:", intentos)
            print("Tiempo:", time.time() - inicio)
            return intentos
    
    for a in alphabeths:
        for b in alphabeths:
            intento = a + b
            intentos += 1
            if intento == contraseña:
                print("Contraseña encontrada:", intento)
                print("Intentos:", intentos)
                print("Tiempo:", time.time() - inicio)
                return intentos
    

    for a in alphabeths:
        for b in alphabeths:
            for c in alphabeths:
                intento = a + b + c
                intentos += 1
                if intento == contraseña:
                    print("Contraseña encontrada:", intento)
                    print("Intentos:", intentos)
                    print("Tiempo:", time.time() - inicio)
                    return intentos
    
    return intentos

contraseña = "abc"
print("Intentos totales:", bruteforce(contraseña))