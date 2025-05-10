"""
#Q1
d1={}
N=int(input("Enter a natural number: "))
for e in range(1,N+1):
    d1[e]=e**2

print(d1)

#Q2

d1={1:4,5:'rahul',2:'rt',3:'gun',9:4,4:4,7:3}
l1=(list(sorted(d1)))
for e in l1[::-1]:
    print(e,d1[e])



#Q3
d1={}
N=int(input("how many players you want to enter"))
for e in range(1,N+1):
    d1[input("Enter his name ")]=tuple(input("Enter performance of player ").split(" "))
print(d1)


#Q4
d1={1:4,5:456,2:45,3:9999,9:4,4:4,7:3}
k,m=0,0
for e in d1:
    if d1[e]>m:
        m=d1[e]
        k=e
print(k,d1[k])
"""
#Q5
cities=["Patna","Bhopal","Puri","Bajipur","Kolkata"]
d1={}
for u in range(65,91):
    l1=[]
    for city in cities:
        if(city.startswith(chr(u))):
            l1.append(city)
        if len(l1)>0:
            d1[chr(u)]=l1

print(d1)


