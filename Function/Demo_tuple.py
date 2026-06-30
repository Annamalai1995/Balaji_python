place=("salem","Chennai","bangalore","hyderabad","chennai")
print(place)
print(type(place))
#silcing
print(place[0:2])
print(place[2:])
#tuple method
alpha=(148,45,87,96,78,25,35,45)
beta=alpha.count(45)
print(beta)
gamma=alpha.index(45)
print(gamma)

#Append 
department=('cse','mech','ece','eee')
dept=list(department)
dept.append('csbs')
dept1=tuple(dept)
print(dept1)

#adding tuple to tuple
cosmo=('Balaji','kumar','prakash')
cosmo1=('Annamalai',)
cosmo+=cosmo1
print(cosmo)
#Join
cooling=('coorg','munnar','ooty','kodai')
places=(12,45,15)
output=cooling+places
print(output)
#join
cooling=('coorg','munnar','ooty','kodai')
join=cooling*4
print(join)

#Range in for
value=(145,182,'priya','sam')
for i in range(len(value)):
    print(value[i])
for i in value:
    print(i)
    print(value)    