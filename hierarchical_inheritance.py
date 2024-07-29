class Shape:
    def __init__(self,radius,lenght,width):
        self.radius=radius
        self.lenght=lenght
        self.width=width
class Circle(Shape):
    def __init__(self, radius,lenght,width ):
        super().__init__(radius,lenght,width )
        self.result=3.14*radius*radius
    def show_c(self):
        print(self.result)
class Rectangle(Shape):
    def __init__(self, radius,lenght,width):
        super().__init__( radius,lenght,width)
        self.result=lenght*width
    def show_r(self):
        print(self.result)
obj1=Circle(5,2,1)
obj2=Rectangle(12,12,4)
obj1.show_c()
obj2.show_r()