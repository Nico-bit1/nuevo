print("::::::::::::::::::::::::::::::::::::::::::")
print("BIENVENIDO AL SISTEMA DE PAGO DE CERTIFIKA")
print("::::::::::::::::::::::::::::::::::::::::::")

Nombre = input("Ingresa tu nombre: ")

print(f"Bienvenido {Nombre}")

def descuento(n):
    if n > 6.0:
        print(f"Tu promedio es {promedio}")
        print("Excelente desempeño")
        print("Tu descuento será del 20 %")
    elif n > 5.0:
        print(f"Tu promedio es {promedio}")
        print("Puede mejorar un poco más, VAMOS!!!")
        print("Tu descuento será del 15 %")
    elif n > 4.0:
        print(f"Tu promedio es {promedio}")
        print("Tiene mucho que mejorar, TU PUEDES")
        print("Tu descuento será del 10 %")
    else:
        print(f"Tu promedio es {promedio}")
        print("Puedes subir tus notas, SOLO TIENES QUE TRABAJAR EN ELLO ")
        print("Desgraciadamente no tienes descuento en la matricula ")


notas = []
print("Por favor ingresa tus calificaciones para saber cual sera el descuento en tu matricula")
while True:
    print("1.Agregar calificaciones")
    print("0.Finalizar y mostrar el descuento de la matricula")
    opcion = input("Ingresa una opcion: ")
    if opcion == "1":
        nota = float(input("Ingresa tu nota: "))
        notas.append(nota)
    elif opcion == "0":
        break
    else: 
        print("Opcion invalida")

suma = sum(notas)
promedio = suma/len(notas)
descuento(promedio)




