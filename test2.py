#töltsön fel egy listát 20 véletlen számmal 1 és 50 között
import random
lista=[]
def veletlen():
    hossz=20
    
    for i in range(hossz):
        lista.append(random.randint(1,50))
        
    return lista

def kiir():
    for i in lista:
        print(i, end="")
        
def osszead():
    sum=0
    for i in veletlen():
        sum=sum+i
    return sum

def legnagyobbElem():
    max=lista[0]
    
    for item in lista:
        if item > max:
             max=item
    return max

    

veletlen()
kiir()
print(f"Alista elemeinek az összege {osszead()}")
print(f"Alista elemeinek a legnagyobb {legnagyobbElem()}")
