"""
Programa de Gestión de Calificaciones
Autor: Gines Martinez
Fecha: 26 de febrero de 2026
Descripción: Refactorización y documentación del sistema de notas.
"""

def calcular_media(nota1, nota2, nota3):
    """
    Calcula la media aritmética de tres notas.
    Args:
        nota1, nota2, nota3 (float): Las tres notas a promediar.
    Returns:
        float: El promedio resultante.
    """
    return (nota1 + nota2 + nota3) / 3

def obtener_resultado(media):
    """
    Determina la calificación cualitativa según la media.
    Args:
        media (float): Promedio del alumno.
    Returns:
        str: Categoría (Sobresaliente, Notable, Aprobado o Suspenso).
    """
    # Usamos una estructura if-elif para evaluar rangos de forma eficiente
    if media >= 9:
        return "Sobresaliente"
    elif media >= 7:
        return "Notable"
    elif media >= 5:
        return "Aprobado"
    else:
        return "Suspenso"

def mostrar_alumno(nombre, n1, n2, n3):
    """Calcula y muestra el reporte completo del alumno por terminal."""
    print("Alumno: " + nombre)
    print(f"Notas: {n1}, {n2}, {n3}")
    
    media = calcular_media(n1, n2, n3)
    print("Media: " + str(round(media, 2)))
    
    resultado = obtener_resultado(media)
    print(f"Resultado final: {resultado}") # Imprime la etiqueta de la nota
    print("--------")

def main():
    mostrar_alumno("Ana García", 8, 7, 9)
    mostrar_alumno("Luis Pérez", 4, 5, 3)
    mostrar_alumno("Marta Gómez", 6, 7, 5)

if __name__ == "__main__":
    main()