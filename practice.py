import sys
l=list(map(int,sys.argv[1:]))
l1=[x for x in l[::2]]
print('odd list :',l1)
sum=0
l2=[]
for i in l1:
    if(i%2==0):
        sum+=i
        l2.append(i)
print('odd placed even list : ',l2)
print(sum)