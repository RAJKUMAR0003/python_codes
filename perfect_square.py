from math import sqrt,floor
n=int(input('enter a no upto which you wanna print the perfect square no '))
for i in range(1,n+1):
    a= sqrt(int(i))
    if(a-floor(a)==0):
        print(int(i),end= ' ')




