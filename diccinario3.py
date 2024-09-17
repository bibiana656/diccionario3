#prestar
biblioteca = {
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "disponible": True},
    "1984": {"autor": "George Orwell", "año": 1949, "disponible": True},
    "El principito": {"autor": "Antoine de Saint-Exupéry", "año": 1943, "disponible": False}
}



def prestar_libro(biblioteca):
    titulo = input("introduce el libro que deseas prestar: ")
    
    
    if titulo in biblioteca:
        
        if biblioteca["titulo"]["disponible"]:
            biblioteca[titulo]["disponible"] = False
            print(f"El libro '{titulo}' ha sido marcado como no disponible.")
        else:
            print(f"El libro '{titulo}' ya está prestado.")
    else:
        print("El libro no se encuentra en la biblioteca.")


prestar_libro(biblioteca)

print("\nBiblioteca actualizada:")
for libro, info in biblioteca.items():
    print(f"Título: {libro}")
    for clave, valor in info.items():
        print(f"  {clave.capitalize()}: {valor}")
    print()

