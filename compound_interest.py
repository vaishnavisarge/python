import math
def compound_interest(p,r,t):
    amount=p*(math.pow((1+(r/100)),t))
    ci=amount-p
    print("Compound Interest:",ci)
Principal_amount=int(input("Enter principal "))
Rate=int(input("Enter rate:"))
Time=int(input("Enter time:"))
compound_interest(Principal_amount,Rate,Time)   