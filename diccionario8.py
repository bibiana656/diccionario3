#bucle para mostrar año for
def mostrar_libros_por_año(biblioteca):
   
    año_buscar = int(input("Ingresa el año de publicación para filtrar los libros: "))

    # Bucle for para recorrer los libros y mostrar los que coinciden con el año
    libros_encontrados = False
    print(f"\nLibros publicados en {año_buscar}:")
    for titulo, info in biblioteca.items():
        if info['año'] == año_buscar:
            print(f"Título: {titulo}")
            print(f"  Autor: {info['autor']}")
            print(f"  Año: {info['año']}")
            disponibilidad = "Disponible" if info['disponible'] else "Prestado"
            print(f"  Disponibilidad: {disponibilidad}")
            print()  
            libros_encontrados = True
    
    if not libros_encontrados:
        print(f"No se encontraron libros publicados en el año {año_buscar}.")

biblioteca = {
    "Cien años de soledad": {
        "autor": "Gabriel García Márquez", 
        "año": 1967, 
        "disponible": True
    },
    "1984": {
        "autor": "George Orwell", 
        "año": 1949, 
        "disponible": True
    },
    "El principito": {
        "autor": "Antoine de Saint-Exupéry", 
        "año": 1943, 
        "disponible": False
    }
}


mostrar_libros_por_año(biblioteca)