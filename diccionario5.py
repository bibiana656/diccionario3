1#mostrar libros

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


mostrar_libros(biblioteca)