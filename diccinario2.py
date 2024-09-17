biblioteca = {
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "disponible": True},
    "1984": {"autor": "George Orwell", "año": 1949, "disponible": True},
    "El principito": {"autor": "Antoine de Saint-Exupéry", "año": 1943, "disponible": False}
}
def agregar_libro(biblioteca):
    # Solicitar los datos del nuevo libro
    titulo = input("Ingresa el título del libro: ")
    autor = input("Ingresa el autor del libro: ")
    try:
        año = int(input("Ingresa el año de publicación: "))
    except ValueError:
        print("Por favor, ingresa un año válido.")
        return

    # Agregar el libro a la biblioteca
    biblioteca[titulo] = {
        "autor": autor,
        "año": año,
        "disponible": True  
    }
    
    print(f'El libro "{titulo}" ha sido agregado a la biblioteca.')


biblioteca = {
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "disponible": True},
    "1984": {"autor": "George Orwell", "año": 1949, "disponible": True},
    "El principito": {"autor": "Antoine de Saint-Exupéry", "año": 1943, "disponible": False}
}


agregar_libro(biblioteca)

print("\nBiblioteca actualizada:")
for libro, info in biblioteca.items():
    print(f"Título: {libro}, Autor: {info['autor']}, Año: {info['año']}, Disponible: {info['disponible']}")
