"""
Diseñe un algoritmo que calcule el resultado de cualquier exponente de un numero, solo usando sumas.
Ejemplo:
	52 = 5 + 5 + 5 + 5 + 5 = 25
	33 = 3 + 3 + 3 = 9 
9 + 9 + 9 = 27

"""
import math


if __name__ == "__main__":
    print('Ingrese la Base:')
    base=int(input())
    print('Ingrese el Exponente:')
    exponente=int(input())
    resultado=base**exponente
    #print(resultado)
    if(exponente==2):
        r=0
        for i in range(base):
            if(i<base-1):
                print(base,end=" + ")
            else:
                print(base)
            r=r+base
        print(f'Resultado: {r}')
    elif(exponente>2):
        exp=list()
        exp.append(2)
        auxiliar=exponente-2
        for i in range(auxiliar):
            exp.append(1)
            e=exponente-1
            if(e==0):
                break
        r=0
        for j in exp:
            if(j==2):
                for k in range(base):
                    if(k<base-1):
                        print(base,end=" + ")
                    else:
                        print(base,end=' = ')
                    r=r+base
                print(r,end='.')
                print(' ')
            if(j==1):
                re=r
                for k in range(base):
                    if(k<base-1):
                        print(r,end=' + ')
                        re=re+r
                    else:
                        print(r, end=' = ')
                    
                print(re, end='.')
                print(' ')
                r=re     

    
            
