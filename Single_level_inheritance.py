class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("Student name:",self.name)
        print("Age:",self.age)
class Teacher(Student):
    def __init__(self, name, age,sub):
        super().__init__(name, age)
        self.sub=sub
    def show(self):
        super().show()
        print("Subject:",self.sub)

obj=Teacher("Priya",12,"science")
obj.show()
