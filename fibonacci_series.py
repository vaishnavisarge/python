n=int(input("Enter nth number:"))
n1=0
n2=1
print("Fibonacci Series",n1, n2,end=" ")

for i in range(2,n):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")
