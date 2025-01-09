class fraction:
    def __init__(self,num=0,den=0) :
        self.num=num
        self.den=den
    def __str__(self):
       fstr=str(self.num)
       fstr+='/'
       fstr+=str(self.den)
       return fstr
    def multi(self,sec):
      new=fraction()
      new.num=self.num*sec.num
      new.den=self.den*sec.den
      return (new)
    def real(self):
       x=self.num/self.den
       return x
    def add(first,sec):
       add=fraction()
       add.num=(first.num*sec.den)+ (sec.num*first.den)
       add.den=first.den*sec.den
       return add
    def sub(first,sec):
       sub=fraction()
       sub.num=(first.num*sec.den)- (sec.num*first.den)
       sub.den=first.den*sec.den
       return sub
       
   
def  main():
   f=fraction(2,3)
   print(f'first fraction is {f}')
   s=fraction(5,4)
   print(f'second fraction is {s}')
   multiply=f.multi(s)
   print(f"multiplying two fraction{multiply}")
   print(f.real())
   a=fraction(2,3)
   b=fraction(4,5)
   print(f'a={a} b={b} a+b={fraction.add(a,b)}')
   print(f'a={a} b={b} a-b={fraction.sub(a,b)}')



main()