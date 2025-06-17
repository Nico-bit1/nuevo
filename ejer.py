

def nombre_repetido(nombre):
    for user in usuarios:
        if user["nombre"] == nombre:
            return True
    return False


def clave_valida(clave):
    if len(clave) < 8:
        return False
    if " " in clave:
        return False
    tiene_letra = any(c.isalpha() for c in clave)
    tiene_numero = any(c.isdigit() for c in clave)
    return tiene_letra and tiene_numero

def ingresar_usuario():
    nombre = input("Ingrese nombre de usuario: ")
    if nombre_repetido(nombre):
        print("El nombre de usuario ya está registrado.")
        return

    sexo = input("Ingrese sexo (F o M): ").upper()
    if sexo not in ("F", "M"):
        print("Sexo inválido. Debe ingresar F o M.")
        return

    clave = input("Ingrese clave (mínimo 8 caracteres, al menos una letra y un número, sin espacios): ")
    if not clave_valida(clave):
        print("Clave inválida.")
        return

    usuario = {
        "nombre": nombre,
        "sexo": sexo,
        "clave": clave
    }
    usuarios.append(usuario)
    print("Ingreso exitoso.")

def buscar_usuario():
    nombre = input("Ingrese el nombre del usuario a buscar: ")
    for user in usuarios:
        if user["nombre"] == nombre:
            print("Usuario encontrado:")
            print(f"Nombre: {user['nombre']}")
            print(f"Sexo: {user['sexo']}")
            print(f"Clave: {user['clave']}")
            return
    print("El usuario no se encuentra registrado.")


def eliminar_usuario():
    nombre = input("Ingrese el nombre del usuario a eliminar: ")
    for user in usuarios:
        if user["nombre"] == nombre:
            usuarios.remove(user)
            print("Usuario eliminado correctamente.")
            return
    print("El usuario no se encuentra registrado.")

def main():
    while True:
        print("\n--- MENÚ ---")
        print("1. Ingresar usuario")
        print("2. Buscar usuario")
        print("3. Eliminar usuario")
        print("4. Salir")

        opcion = input("Seleccione una opción (1/2/3/4): ")

        if opcion == "1":
            ingresar_usuario()
        elif opcion == "2":
            buscar_usuario()
        elif opcion == "3":
            eliminar_usuario()
        elif opcion == "4":
            seguir = input("¿Desea seguir o salir? (s/salir): ").lower()
            if seguir == "salir":
                print("¡Hasta luego!")
                break
        else:
            print("Debe seleccionar una opción válida (1/2/3/4)")
