#ENTRADAS DEL PROBLEMAS

nivelAgua = int(input("Digita el nivel de agua de la presa: "))

#PROCESO DEL PROBLEMA

if nivelAgua >= 0 and nivelAgua < 20 :
    alerta = 'no permite producción de energía'
elif nivelAgua >= 20 and nivelAgua < 400 :
    alerta = 'Estamos melos'
elif nivelAgua >= 400 :
    alerta = 'Se acabó todo, todin, todito'
else:
    print("Didgite una opción válida")

#Salida
            
print (f'El nivel de agua es {nivelAgua} y {alerta}')
    