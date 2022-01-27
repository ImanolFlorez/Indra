from ast import Try
import math



def Calcular(numero,exponente):
    if exponente>1:
        conteo = numero
        for j in range(1,exponente):
            sumatoria=0
            for i in range(0, conteo):
                if i==conteo-1:
                    print(numero,end="=")
                else:
                    print(numero,end="+")
                sumatoria+=numero
            numero=sumatoria
            print(sumatoria)
    else:
        print(numero)
    
            
            

        
        

numero=int(input("numero: "))
exponente=int(input("exponente: "))   
Calcular(numero,exponente)

