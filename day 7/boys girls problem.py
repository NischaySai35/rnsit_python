t = int(input("Enter t : "))

boys_heights = []
girls_heights = []
n1=[]

for j in range(t):
    n=int(input("Enter no of boys/girls : "))
    boys = list(map(int, input("Enter boys height : ").split()))
    girls = list(map(int, input("Enter girls height : ").split()))
    
    boys_heights.append(sorted(boys))
    girls_heights.append(sorted(girls))
    n1.append(n)

b =boys_heights
g =girls_heights
print(b,g)
for i in range(t):
    l1=[]
    l2=[]
    for j in range(n1[i]):
        x=b[i][j]
        #print('x is ',x)
        y=g[i][j]
        #print('y is ',y)
        l1.append(x)
        l1.append(y)
        l2.append(y)
        l2.append(x)
    #print('sorted list',sorted(l1),'list',l1)
    if(l1==sorted(l1) or l2==sorted(l2)):
        print("\nYES")
    else:
        print("\nNO")

    
