from array import *
a=array('i',[])
n=int(input('enter the no of elements'))
for i in range(n):
    val=int(input('enter the value'))
    a.append(val)
print(a)
for i in range(n//2):
    a[i],a[n-i-1]=a[n-1-i],a[i]
print(a)
