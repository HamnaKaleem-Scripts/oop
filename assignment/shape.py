class shape :
    def __init__(self,name,color,id, x_axis,y_axis):
        self.name=name
        self.color=color
        self.id=id
        self.x_axis=x_axis
        self.y_axis=y_axis
        self.border=None
        
        
    def set_outline(self,w,c) :
        x=outline(w,c)
        return x
          


    def set_border(self, width, color):
        self.border = outline(width,color)
    
    def area (self):
        pass            #it will be overriden by specialized shape class
        
    def __str__(self):
        a=''
        a+=f"Shape: {self.name}, ID: {self.id}, Color: {self.color}"
        if not self.border==None:
            a+=f'{self.border}' 
            return a 

class outline: 
    def __init__(self,width,color):     
        self.width=width
        self.color=color

    def __str__(self):
        return (f'width of outline : {self.width} color of outline: {self.color}')
    

class square (shape):
    def __init__(self,name,color,id,x_axis,y_axis,side,):
        super().__init__(name,color,id,x_axis,y_axis)
        self.side=side
        
    def area(self):
        return self.side * self.side
    
    def __str__(self):
        return f"{super().__str__()} it one side = {self.side}\nLocation on canvas :\nx-axis = {self.x_axis}  y-axis ={self.y_axis} "
        


class rectangle (shape):
    def __init__(self,name,color,id,x_axis,y_axis,l,w):
        super().__init__(name,color,id,x_axis,y_axis)
        self.l=l
        self.w=w

    def area(self):
        return self.l * self.w
    
    def __str__(self):
        return f"{super().__str__()} length = {self.l} width={self.w}\nLocation on canvas :\nx-axis = {self.x_axis}  y-axis ={self.y_axis} "
    

class triangle(shape):
    def __init__(self,name,color,id,x_axis,y_axis,h,base,height):
        super().__init__(name,color,id,x_axis,y_axis)
        self.h=h
        self.base=base
        self.height=height

    def area(self):
        return (self.base * self.height )*0.5
    
    def __str__(self):
        return f"{super().__str__()} hypotneus = {self.h} base = {self.base} height = {self.height}\nLocation on canvas :\nx-axis = {self.x_axis}  y-axis ={self.y_axis} "
        


class circle(shape):
    def __init__(self,name,color,id,x_axis,y_axis,radius):
        super().__init__(name,color,id,x_axis,y_axis)
        self.radius=radius

    def area(self):
        return 3.14*(self.radius)**2
    
    def __str__(self):
        return f"{super().__str__()} radius = {self.radius}\nLocation on canvas :\nx-axis = {self.x_axis}  y-axis ={self.y_axis} "



class canvas():
    def __init__(self,b_c,border,size):
        self.b_c=b_c
        self.border=border
        self.size=size
        self.l=[]

    def add(self,a):
        self.l.append(a)
        return
    
    def show (self):
        for i in self.l:
            print(i)
        return


def main():
    a=canvas(None,"Thin",12)
    c = circle("Circle 1",'red' ,1,2,3, 5)
    
    r = rectangle("Rectangle 1","Blue",2,5,8 , 10, 8)
    t = triangle("Triangle 1","Green",3 ,12,45, 6, 7, 5)
    s = square("square",None,4,56,34,4)  
    
    print(f'{s.name} has {s.set_outline (25,"grey")}')
    a.add (c)
    a.add (r)
    a.add (t)
    a.add (s)
    print (a.show())

    r1 = rectangle("Rectangle 1","Blue ",2,5,8 , 10, 8)

    r1.set_border(12,"black")
    print(r1)

main()