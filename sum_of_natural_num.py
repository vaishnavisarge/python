num=int(input("Enter number:"))
if(num==0):
    print("Enter valid number")
else:
    sum=0
    while(num>0):
        sum+=num
        num=num-1
    print("Sum is",sum)