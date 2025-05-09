promedio = float(input("Ingresa su promedio academico fianl porfavor: "))
quintil = int(input("Ingrese su Condición Socioeconómica: "))

matricula = 90.000
arancel = 1.800000
beneficios = 0
beneficio_arancel = 0
beneficio_matricula = 0



if promedio > 6.0  and quintil in {1, 2}:
     beneficio_arancel += 0.20
elif promedio > 6.0  and quintil in {3, 4}:
     beneficio_arancel += 0.15 
elif  promedio 5.0 or promedio <= 6.0 quintil and quintil in {1, 2}:
     beneficio_arancel += 0.15 
elif  promedio 5.0 or promedio <= 6.0 quintil and quintil in {3, 4}:
     beneficio_arancel += 0.10 


if quintil in {1, 3}:
     beneficio_arancel += 0.10

if promedio >= 5.5:
     beneficio_arancel += 0.5

resultado_aracel = arancel + (1 - beneficio_arancel)
resultado_aracel = matricula + (1 - beneficio_matricula)

print(f"El valor del aracel es de $")
print(f"El valor de la matricula es de $")


