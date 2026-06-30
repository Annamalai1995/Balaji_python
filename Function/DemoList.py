#["Annamalai",'Balaji',25,5.4]
# prop=['Balaji',21,5.4,60,'M']
# print(prop)
# #adding new element
# prop.append("KIOT")
# print(prop)
# print(len(prop))
# #Adding new element but particalur position
# prop.insert(3,'BE cse')
# print(prop)
# #replace the Elements
# prop[6]='Knowlege college'
# print(prop)

salary=[60000,80000,85000,95000,105000]
print(min(salary))
print(max(salary))
print(sum(salary))
#Remove or pop
salary.remove(60000)
print(salary)
print(salary.pop(2))
print(salary)



#List Methods
#copy and Count

# li=[15,45,10,25,30,30]
# alpha=li.copy()
# print("copy data",alpha)
# counting=li.count(30)
# print(counting)

# li=input("Enter the List")
# list=li.split(',')
# print("List vALues")
# for i in list:
#     print(i)

##Looping List
n=int(input("En ter the List"))
Empty_list=[]

for i in range(n):
    livalue=input("enter value of the List")
    Empty_list.append(livalue)
print("List Data",Empty_list)    