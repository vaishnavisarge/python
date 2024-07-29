class Cal1:
    def Sum(self,a,b):
        return a+b
class Cal2:
    def Sub(self,a,b):
        return a-b
class Cal3(Cal1,Cal2):
    def Mul(self,a,b):
        return a*b
obj=Cal3()
print(obj.Sum(10,20))
print(obj.Sub(40,20))
print(obj.Mul(22,10))

