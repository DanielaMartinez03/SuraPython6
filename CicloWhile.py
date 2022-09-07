#tambien conocido como Mientras

#Declarar variable centinela o de conrol para evaluar la ejecucion del ciclo
'''i=0

#Menu de opciones
print("***Menú***")
print("1. Saludar")
print("2. Despedir")
print("3. Ganador")
print("4. Clima")
print("5. Salir")
#Programar la estructura del cicli Mientras
while(i!=5):
    i=int(input("Digite una opcion del menú"))

    if(i==1):
        print("Hola, como estas?")
    elif(i==2):
        print("Hasta pronto")
    elif(i==3):
        print("Ganador Medellin")
    elif(i==4):
        print("No esta Lloviendo")
    elif(i==5):
        break
    else:
        print("Digita opción válida")
    #i=i+1 #contador

print("Fin")'''

i=0
num1=0
num2=0
suma=0
resta=0
multiplicacion=0
division=0

print("***Menú***")
print("1. Sumar 2 números")
print("2. Restar 2 números")
print("3. Encontrar la raiz cuadrada de un número")
print("4. Multiplicar 2 numeros")
print("5. Salir")


while(i!=5):
    i=int(input("Digite una opcion del menú"))

    if(i==1):
        numero1=int(print("Digite número 1: "))
        numero2=int(print("Digite número 2: "))
        suma = num1+num2
        print("el resultado es: ",suma)
    elif(i==2):
        num1=int(print("Digite número 1: "))
        num2=int(print("Digite número 2: "))
        resta = num1-num2
        print("el resultado es: ",resta)
    else:
         num2=int(print("fin"))
    
