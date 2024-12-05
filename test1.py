#készítsen python kódot ami bekér egy egész hőmréséklet értéket
#kiirja hogy az adott értéken milyen halmazállapotú a víz
hofok=0
def homerseklet():
    hofok=int(input("Adja mega víz hőmérsékletét: "))
    
    if(hofok<=0):
        return "szilárd"
    elif(hofok>100):
        return"gáz"
    else:
        return"folyékony"
           
print (homerseklet())

