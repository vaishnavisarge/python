def simple_interest(p,t,r):
    p=P
    t=  T 
    r=  R 
    si=(p*t*r)/100
    print("simple intereset is",si)
P=int(input("Enter principle amount: "))
T=int(input("Enter total time: "))
R=int(input("Enter rate: "))
simple_interest(P,T,R)