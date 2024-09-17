#realizar menu
def agregar_libro(biblioteca):
    titulo = input("Ingresa el título del libro: ")
    autor = input("Ingresa el nombre del autor: ")
    año = int(input("Ingresa el año de publicación: "))
    
    nuevo_libro = {
        "autor": autor,
        "año": año,
        "disponible": True
    }
    
    biblioteca[titulo] = nuevo_libro
    print(f"El libro '{titulo}' ha sido añadido a la biblioteca.")

def prestar_libro(biblioteca):
    titulo = input("Ingresa el título del libro que deseas prestar: ")

    if titulo in biblioteca:
        if biblioteca[titulo]["disponible"]:
            biblioteca[titulo]["disponible"] = False
            print(f"El libro '{titulo}' ha sido marcado como prestado.")
        else:
            print(f"El libro '{titulo}' ya está prestado.")
    else:
        print(f"No se encontró el libro con el título '{titulo}' en la biblioteca.")

def devolver_libro(biblioteca):
    titulo = input("Ingresa el título del libro que deseas devolver: ")

    if titulo in biblioteca:
        if not biblioteca[titulo]["disponible"]:
            biblioteca[titulo]["disponible"] = True
            print(f"El libro '{titulo}' ha sido marcado como disponible.")
        else:
            print(f"El libro '{titulo}' ya está disponible.")
    else:
        print(f"No se encontró el libro con el título '{titulo}' en la biblioteca.")

def mostrar_libros(biblioteca):
    if not biblioteca:
        print("La biblioteca está vacía.")
        return

    print("\n=== Lista de Libros ===")
    for titulo, info in biblioteca.items():
        print(f"Título: {titulo}")
        print(f"  Autor: {info['autor']}")
        print(f"  Año: {info['año']}")
        disponibilidad = "Disponible" if info['disponible'] else "Prestado"
        print(f"  Disponibilidad: {disponibilidad}")
        print() 

def menu():
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

    while True:
        print("\n=== Menú de Biblioteca ===")
        print("1. Agregar un nuevo libro")
        print("2. Prestar un libro")
        print("3. Devolver un libro")
        print("4. Ver todos los libros")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ")

        if opcion == '1':
            agregar_libro(biblioteca)
        elif opcion == '2':
            prestar_libro(biblioteca)
        elif opcion == '3':
            devolver_libro(biblioteca)
        elif opcion == '4':
            mostrar_libros(biblioteca)
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


menu()