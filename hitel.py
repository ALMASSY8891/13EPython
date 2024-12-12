import math
def torleszto():
   P=float(input("Kérem adja meg hitel összegét (ft): ")) 
   r=float(input("kérem adja meg a havi kamatlábat(%): "))
   n=float(input("kérem adja meg hány hónap a futamidő: "))
   kamatlab=r/100/12
   
   T=(P*kamatlab*(1+kamatlab)**n)/((1+kamatlab)**n-1)
   print(f"a havi törlesztő: {round(T)} Ft")
   return 

torleszto()

             