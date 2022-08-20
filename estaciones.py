#Entrada

mes = input("Digita el mes: ")

#Proceso

if mes == "enero" or mes == 'febrero' or mes == 'marzo' :
    print (f'Es {mes} y es invierno')
elif mes == 'abril' or mes == 'mayo' or mes == 'junio':
    print (f'Es {mes} y es Primavera')
elif mes == 'julio' or mes == 'agosto' or mes == 'septiembre':
    print (f'Es {mes} y es Verano')
elif mes == 'octubre' or mes == 'noviembre' or mes == 'diciembre':
    print (f'Es {mes} y es Otoño')
else:
    print("Didgite un dato válido")

#Salida