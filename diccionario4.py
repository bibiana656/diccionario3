#devolver

biblioteca = {
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "disponible": True},
    "1984": {"autor": "George Orwell", "año": 1949, "disponible": True},
    "El principito": {"autor": "Antoine de Saint-Exupéry", "año": 1943, "disponible": False}
}

def devolver_libro(biblioteca):
    titulo = input("Introduce el título del libro que deseas devolver: ")
    
    if titulo in biblioteca:
       
        if not biblioteca[titulo]["disponible"]:
            biblioteca[titulo]["disponible"] = True
            print(f"El libro '{titulo}' ha sido marcado como disponible.")
        else:
            print(f"El libro '{titulo}' ya está disponible.")
    else:
        print("El libro no se encuentra en la biblioteca.")

        devolver_libro(biblioteca)

print(biblioteca)