def College():
    COllege_name=input("ENter The College NAme")
    if COllege_name =="PSG":
        print("Best Placemnet in Tamilnadu")
    elif COllege_name =="Kumaraguru":
        print    ("High Pakage salary ")
    elif COllege_name =="Karpagam":
        print("Better college")
    else:
        print("Not eligible")
College()

#Function Parameter
def hiring(qual,ref):
    if qual =='ug' and ref=='hr':
        print("You are hired in US Based Project")
    elif qual == 'Pg' and ref=='Team lead':
        print("You are hired in KPo company") 
    else:
        print("You are Hired")
hiring(qual='ug',ref='hr')
hiring(qual='pg',ref='Team lead')

