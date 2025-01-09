class polynomial:
    
    def __init__(self,var='x',deg=0,list=[0]):
        self.var=var
        self.deg=deg
        self.list=list
    def __str__(self):
        d=self.deg
        l=len(self.list)-1
        pstr=''
        for i in self.list:
            if d>=1:
                 pstr+=str(i)+str(self.var)+'^'+str(d)+'+'
                 d-=1      
        pstr+=str(self.list[l])
        return pstr 
   
    # def __del__(self):
    #     print(f"{self} is getting garbage")
    #     return
    
    
    @property
    def var(self):
        return self.__var
    @var.setter
    def var(self, d):
        self.__var = d
        return
    
    @property
    def deg(self):
        return self.__deg
    @deg.setter
    def deg(self, d):
        self.__deg = d
        return
    
    @property
    def list(self):
        return self.__list
    @list.setter
    def list(self, d):
        self.__list = d
        return
       
    def __add__(a,b):
        x=a
        y=b
        a=polynomial()
        a.list=[]
        m=x.deg
        if x.var!=y.var:
            print(f'{x} and {y} does not have same variables')
            return 
        length_x=len(x.list)
        length_y=len(y.list)
        if length_x>length_y:
           m=x.deg
           b=length_x-length_y
           for i in range (b):
               y.list.insert(i,0)
        elif length_y>length_x:
            b=length_y-length_x
            m=y.deg
            for i in range (b):
               x.list.insert(i,0)
        for i in range (length_x):
            result=x.list[i]+y.list[i]
            a.list.append(result)  
        a.deg=m
        a.var=x.var
        return a 
    @staticmethod
    def compare(x,y):
        if x.deg==y.deg and x.var==y.var and x.list==y.list:
            print(f'{x}and {y}are equal')
        else:
            print(f'{x}and {y}are not equal')
        return
    
    def __mul__(x,y):
        m=polynomial()
        m.list=[]
        m.deg=x.deg
        m.var=x.var
        length_x=len(x.list)
        length_y=len(y.list)
        if length_x > length_y:
           m.deg=x.deg
           b=length_x-length_y
           for i in range (b):
               y.list.insert(i,1)
        elif length_y > length_x:
            b=length_y-length_x
            m.deg=y.deg
            for i in range (b):
               x.list.insert(i,1)
        
        for i in range (length_x):
            for j in range (length_y):
                result=(y.list[i])* (x.list[j])
                m.list.append(result)
        return m

        # if length_x>length_y:
        #    m.deg=x.deg
        #    b=length_x-length_y
        #    for i in range (b):
        #        y.list.insert(i,1)
        # elif length_y>length_x :
        #     b=length_y-length_x
        #     m.deg=y.deg
        #     for i in range (b):
        #        x.list.insert(i,1)
        # for i in range (length_x):
        #     result=x.list[i]*y.list[i]           
        #     m.list.append(result)
        #     print(result)
        
        return m
   
    def evaluate(self,value):
        result=0
        for i in range(len(self.list)):
            result+=(self.list[i]) * (value**(self.deg - i))
        return result
        # for i in range(length_x):
        #     result=(x.list[i]) +(y.list[i]) 
        #     a.list.append(result)
        # return a    


        

       
