class Usuario:
    def __init__(self, nombre, puntos):
        self.nombre = nombre
        self.puntos = puntos
        self.nivel = self.determinar_nivel()

    def determinar_nivel(self):
        if self.puntos >= 1000:
            return "Nivel Premium"
        elif self.puntos >= 500:
            return "Nivel Oro"
        elif self.puntos >= 250:
            return "Nivel Bronce"
        else:
            return "Nivel Inicial"

    def determinar_descuento(self):
        if self.nivel == "Nivel Premium":
            return 25
        elif self.nivel == "Nivel Oro":
            return 10
        else:
            return 0

    def mensaje(self):
        if self.nivel == "Nivel Premium":
            return f"Hola {self.nombre}, eres un usuario nivel premium. Recuerda que puedes canjear tus puntos por un descuento del 25% en tu próxima compra."
        elif self.nivel == "Nivel Oro":
            return f"Hola {self.nombre}, eres un usuario nivel oro. Recuerda que puedes canjear tus puntos por un descuento del 10% en tu próxima compra."
        elif self.nivel == "Nivel Bronce":
            return f"Hola {self.nombre}, eres un usuario nivel bronce. Recuerda que puedes canjear tus puntos por grandes premios en nuestra tienda."
        else:
            return f"Hola {self.nombre}, eres un usuario nivel inicial. Recuerda que puedes empezar a ganar puntos comprando en nuestra tienda y alcanzar niveles más altos."

def main():
    usuarios = [
        Usuario("Marcos", 1500),
        Usuario("Jose Luis", 2500),
        Usuario("Sebastian", 300)
    ]

    for usuario in usuarios:
        print(f"Nombre: {usuario.nombre}")
        print(f"Nivel: {usuario.nivel}")
        print(f"Descuento: {usuario.determinar_descuento()}%")
        print(usuario.mensaje())
        print("")

if __name__ == "__main__":
    main()
