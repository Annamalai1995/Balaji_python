#FOR IN Loop
# 1 < 5
# 1
# 2
# 3
# 4
# for variablename in values:
#     stmts;
# for name in "Balaji":
#     print(name)

#STock:
# stock=[150,450,850,1000,950]
# total=0
# for price in stock:
#     total+=price
#     print("Total",total)
# print("Total Amount:",total)    

#Even Numbers
# even =[2,10,15,21,30,60,99,210]
# for a in even:
#     if a%2==0:
#         print("Even  number",a)
#     else:
#         print("ODD number",a)    


# #FOR IN RANGE LOOP

# for hai in range(1,10): #start ending

#     print(hai)


#Tables:
# table=int(input("Enter the Table number"))
# for i in range(1,11):
#     print(f"{table}*{i}={table*i}") #5*1=5


#Sale:

stock=5
for stock in range(5,0,-1):
    amt=int(input("Enter the amount to purchase"))
    if amt >=15000:
        print("stock quantity one has purchase ")
        
    else:
        print("Insuffcient amount to purchase")    
