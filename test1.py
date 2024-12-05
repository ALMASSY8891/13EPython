#készítsen python kódot ami bekér egy egész hőmréséklet értéket
#kiirja hogy az adott értéken milyen halmazállapotú a víz

def homerseklet():
    hofok=int(input("Adja mega víz hőmérsékletét: "))
    
    if(hofok<=0):
        print("szilárd")
    elif(hofok>100):
        print("gáz")
    else:
        print("folyékony")
           
homerseklet()