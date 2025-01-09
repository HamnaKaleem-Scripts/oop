class N_Dimension_Vector:
    def __init__(self,*tuple):
        self.tuple=tuple
    def magnitude(self):
        s=0
        for i in self.tuple:
            s+=i 
        answer=(s)**0.5
        return answer
    def dot_product(v1,v2):
        s=0
        if len(v1.tuple)==len(v2.tuple):
            for i in range(len(v1.tuple)):
                s+=v1.tuple[i]*v2.tuple[i]
        else:
            print("error")
        return s
    def __add__(v1, v2):
        if len(v1.tuple) != len(v2.tuple):
            print("Vectors must have the same dimension for addition.")
        new = [v1.tuple[i] + v2.tuple[i] for i in range(len(v1.tuple))] #adds and returns a list to new _components
        return N_Dimension_Vector(*new)  #unpacking

    def __sub__(v1, v2):
        if len(v1.tuple) != len(v2.tuple):
            print("Vectors must have the same dimension for subtraction.")
        new = [v1.tuple[i] - v2.tuple[i] for i in range(len(v1.tuple))]
        return N_Dimension_Vector(*new)
        # return new_components
    def __str__(self):
        return f"{self.tuple}"
    def scalar_multiply(self, scalar):
        new = [scalar * x for x in self.tuple]
        return N_Dimension_Vector(*new)
def main():
    # 1-dimensional vector
    v1 = N_Dimension_Vector(3)
    print("this is v1 magnitude:",v1.magnitude())
    # 2-dimensional vector
    v2 = N_Dimension_Vector(3, 4)
    print("Dot product of v2 with another vector (1,2) :",v2.dot_product(N_Dimension_Vector(1, 2)))
    print("addition of v2 with another vector (15,9) :",v2+(N_Dimension_Vector(15, 9)))         #adition function

    # 3-dimensional vector
    v3 = N_Dimension_Vector(1, 2, 3)
    print("this is v3 magnitude:",v3.magnitude())
    print("Dot product of v3 with another vector (4,5,6) :",v3.dot_product(N_Dimension_Vector(4, 5, 6)))
    print("subtraction of v3 with another vector (4,5,6) :",v3-(N_Dimension_Vector(6, 15, 8)))      #subtraction function

    # 4-dimensional vector
    v4 = N_Dimension_Vector(1, 2, 3, 4)
    print("this is v4 magnitude:",v4.magnitude())       #magnitude
    print("Dot product of v4 with another vector (2,3,4,5) :",v4.dot_product(N_Dimension_Vector(2, 3, 4, 5)))       #dot product
    print("scalar product  of v4 with 5 :",v4.scalar_multiply(2))       #scalar product

    # 5-dimensional vector
    v5 = N_Dimension_Vector(1, 2, 3, 4, 5)              #magnitude
    print("this is v5 magnitude:",v5.magnitude())
    print("Dot product of v5 with another vector (2,3,4,5,6) :",v5.dot_product(N_Dimension_Vector(2, 3, 4, 5, 6)))
    #All test cases passed!
main()

        