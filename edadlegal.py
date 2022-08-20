#Entrada
edad = int(input("Digite su edad: "))

#Proceso

if edad == 0 and edad < 14 :
    print(f'Su edad es {edad} y está en el grupo de Niño')
elif edad >= 14 and edad < 28 :
    print(f'Su edad es {edad} y está en el grupo de Joven')
elif edad >= 28 and edad < 60 :
    print(f'Su edad es {edad} y está en el grupo de Adulto')
elif edad >= 60 and edad < 100 :
    print(f'Su edad es {edad} y está en el grupo de Adulto mayor')
elif edad >= 100 or edad < 0 :
    print(f'Su edad es {edad} ¿Matusalem o el Extraño caso de Benjamin Buttom?')
else:
    print("Didgite una opción válida")