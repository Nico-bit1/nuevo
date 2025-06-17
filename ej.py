
class Pelicula:
    def __init__(self, nombre, categoria, duracion):
        self.nombre = nombre
        self.categoria = categoria
        self.duracion = duracion

class Menu:
    def __init__(self):
        self.peliculas = []
        self.opciones = {
            "1": {"nombre": "Añadir película", "categorias": ["Acción", "Ciencia ficción", "Terror", "Comedia"], "duracion": "Ingrese la duración"},
            "2": {"nombre": "Salir", "categorias": [], "duracion": "No aplica"}
        }

    def mostrar_menu(self):
        print("\nMenú de opciones de entretenimiento")
        for opcion, datos in self.opciones.items():
            print(f"{opcion}. {datos['nombre']}")

    def agregar_pelicula(self):
        nombre = input("Ingrese el nombre de la película: ")
        categoria = input("Ingrese la categoría de la película (Acción, Ciencia ficción, Terror, Comedia): ")
        while categoria not in self.opciones["1"]["categorias"]:
            categoria = input("Ingrese una categoría válida: ")
        duracion = input("Ingrese la duración de la película: ")
        self.peliculas.append(Pelicula(nombre, categoria, duracion))
        print("Pelicula agregada con éxito.")

    def mostrar_peliculas(self):
        if not self.peliculas:
            print("No hay películas agregadas.")
        else:
            print("\nPeliculas agregadas:")
            for i, pelicula in enumerate(self.peliculas, start=1):
                print(f"{i}. {pelicula.nombre} ({pelicula.categoria}, {pelicula.duracion})")

def main():
    menu = Menu()
    while True:
        menu.mostrar_menu()
        opcion = input("Ingrese la opción deseada: ")
        if opcion == "1":
            menu.agregar_pelicula()
        elif opcion == "2":
            print("Saliendo del menú...")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
