#Realizar un menu que le presente las siguientes opciones al usuario las sig opciones:
#1.Un saludo
#2. Una despedida
#3.Edad 
#mensaje de salida: "Opcion invalida"

while True:
    print("Hola Bienvenid@")
    print("---MENU DE OPCIONES---")
    print("1.Mostrar saludo")
    print("2.Mostras depedida")
    print("3.Mostrar edad")
    print("0.Terminar programa ")
    opcion = input("ELiga una opción: ")
    if opcion == "1":
        nombre = input("Ingresa tu nombre: ")
        print("Hola " ,nombre,  " bienvenid@")
    elif opcion == "2":
        nombre = input("Ingresa tu nombre: ")
        print(f"Hasta luego {nombre}, que estes bien")
    elif opcion == "3":
        edad = int(input("Ingresa tu edad: "))
        if edad >= 18:
            print(f"Tu edad es {edad}, eres mayor de edad")
        elif edad <= 18:
            print(f"Tu edad es {edad}, eres menor de edad")
        else: 
            print("Edad ingresada invalida")
    
    elif opcion == "0":
        break
    else:
        print("Opcion invalida")

print("Fin del programa")