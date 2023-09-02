
#Programa para calcular la gasolina
#By Ivar


def Consumo ():

    print("Bienvenido al Asistente de Consumo")

    PROMEDIO= 100
    n1= int(input("Introduce el consumo de tu coche : "))
    n2= int(input("Introduce los km que has hecho : "))
    n3= float(input('Introduce pvp gasolina : '))
    resultado= (n2*n1/PROMEDIO)*n3

    print('Tienes que pagar : ', resultado, 'Eur')

    

Consumo() 

print('-----------------------------------------------------')

Consumo()

print('-----------------------------------------------------')

Consumo()