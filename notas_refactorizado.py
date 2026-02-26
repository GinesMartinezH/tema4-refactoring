def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def obtener_resultado(media):
    if media >= 9:
        return "Sobresaliente"
    elif media >= 7:
        return "Notable"
    elif media >= 5:
        return "Aprobado"
    else:
        return "Suspenso"

def mostrar_alumno(nombre, n1, n2, n3):
    print("Alumno: " + nombre)
    print("Nota 1: " + str(n1))
    print("Nota 2: " + str(n2))
    print("Nota 3: " + str(n3))
    
    media = calcular_media(n1, n2, n3)
    print("Media: " + str(round(media, 2)))
    
    resultado = obtener_resultado(media)
    print(resultado)
    print("--------")

def main():
    mostrar_alumno("Ana García", 8, 7, 9)
    mostrar_alumno("Luis Pérez", 4, 5, 3)
    mostrar_alumno("Marta Gómez", 6, 7, 5)

if __name__ == "__main__":
    main()