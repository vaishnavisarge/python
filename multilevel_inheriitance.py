class Student:
    def __init__(self,name,rollno): 
        self.name=name
        self.rollno=rollno
    def stud_detail(self):
        print(self.name)
        print(self.rollno)
class Marks(Student):
    def __init__(self,name,rollno,m1,m2,m3):
        super().__init__(name,rollno)
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def marks_detail(self):
        super().stud_detail()
        print(self.m1)
        print(self.m2)
        print(self.m3)
class Result(Marks):
    
    def __init__(self, name,rollno,m1,m2,m3):
        super().__init__(name,rollno,m1,m2,m3,)
        self.total=m1+m2+m3
        self.per=(self.total/300)*100
    def display(self):
        super().marks_detail()
        print("Total:",self.total)
        print("Percentage:",self.per)
obj=Result("Abhi",19,69,77,80)
obj.display()