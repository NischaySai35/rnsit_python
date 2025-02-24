n=int(input("Enter no. of oranges : "))
l1=list(map(int,input("Enter size of oranges : ").split()))
print(l1)
l2=[]
l3=[]
l4=[]
l5=[]

k=l1[n-1]
print('k=',k)
for i in l1:
    if i<k:
        l2.append(i)
        print("appended i",i)
    elif i==k:
        l3.append(i)
        print("appended i",i)
    else:
        l4.append(i)
        print("appended i",i)
    print(f'l2={l2},l3={l3},l4={l4}')
print(l2,l3,l4,l5)
l5=l2+l3+l4
print(l5)