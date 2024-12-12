def bmi():
    suly=float(input("kérem adja meg a sulyát(kg): "))
    magassag=float(input("kérem adja meg a magasságát (m): "))
    bmi=(suly)/(magassag*magassag)
    if bmi<=18.5:
        print(f"{(bmi)} alultáplált")
    elif 18.5<bmi<=24.9:
        print(f"{bmi} Normál ")
    elif 25<bmi<=29.9:
        print(f"{bmi} Túlsúlyos")
    else: 
        print(f" {bmi} Elhízott")
        
    return ()

bmi()
