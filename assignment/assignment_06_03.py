
from abc import ABC, abstractmethod 
import tkinter as tk
class Shape(ABC):
    def __init__(self,name,color,x,y):
        self.name=name
        self.color=color
        self.x=x
        self.y=y
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self, canvas):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def display_info(self):
        print("This is a shape.")

    def shape_discription(self):
        return f"this i {self.name} area : {self.area()} \nthis is {self.name} perimeter : {self.perimeter()}"
class Rectangle(Shape):
    def __init__(self,name,color, x, y, width, height):
        super().__init__(name,color,x, y)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, outline="black", fill=f"{self.color}")

class Circle(Shape):
    def __init__(self,name,color, x, y, radius):
        super().__init__(name,color,x, y)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14* self.radius

    def draw(self, canvas):
        canvas.create_oval(self.x - self.radius, self.y - self.radius, 
                            self.x + self.radius, self.y + self.radius, outline="black", fill=f"{self.color}")
class Square(Rectangle):
    def __init__(self,name,color, x, y, side):
        super().__init__(name,color,x, y, side, side)

    def area(self):
        return self.width ** 2
    
    def perimeter(self):
        return 4 * self.width
    
    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, outline="black", fill=f"{self.color}")

    

class Oval(Circle):
    def __init__(self,name,color, x, y, major_axis, minor_axis):
        super().__init__(name,color,x, y, major_axis)
        self.minor_axis = minor_axis

    def area(self):
        return 3.14 * self.radius * self.minor_axis

    def draw(self, canvas):
        canvas.create_oval(self.x - self.radius, self.y - self.minor_axis,
                            self.x + self.radius, self.y + self.minor_axis, outline="black", fill=f"{self.color}")



    
def draw_shapes(shapes):
    window = tk.Tk()
    window.title("Shapes Drawing")

    canvas = tk.Canvas(window, width=1000, height=1000)
    canvas.pack()

    for shape in shapes:
        shape.draw(canvas)

    window.mainloop()

shapes = [
    Rectangle("rectangle","Blue",10, 15, 100, 50),
    Circle("Circle","Red",150, 100, 30),
    Square("Square","Green",250, 10, 60),
    Oval("Oval","Yellow",450, 100, 80, 40),
    Square("Square","pink",450, 350, 90),
    Circle("Circle","grey",300, 300, 150),
    Oval("Oval","white",850, 500, 100, 50)
    ]
draw_shapes(shapes)
for x in shapes:
    print(x.shape_discription())

    

