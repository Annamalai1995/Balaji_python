#function with default parameter
# def register(name,location,prefix="Mr/Mrs/Miss"):
#     if location == 'Bangalore':
#         print(prefix,name,"Has approved in",location)
#     elif location == 'Hyderabad':
#         print(prefix,name,'Relocation the Hyderabad',location)
#     else:
#         print("Business Not Approved")
# register('CTS','Bangalore')
# register('Tcs','Hyderabad','Mr')                
# register("Finish",'Balaji')


#Banking
amount=[15000,25000,45000,3000]
def debit(money=0,pos=0):
    if money <= amount[pos]:
        amount[pos]-=money
        print(money,'AMount')
        return amount[pos]
    else:
        print("cannot debit")
bank=debit(1500,1)
debit(bank)        
    