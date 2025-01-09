

class bill_line:
    def __init__(self,no=0,d=None,name=None,item=[],ad=None):
        self.no=no
        self.name=name
        self.d=d
        self.item=item
        self.adress=ad
        self.__total=0          #private
        
    def __str__(self):
        r=('MOBILO\nMobile City\nDeals in all kinds of Mobile sets and Accsessories\nCell No: 0321-0000000\nBILL_PRACTICE')
        r+=(f'\nNo. : {self.no}\nDtae : {self.d}\nCustomer Name : {self.name}\nCustomer Address : {self.adress}')
        r+=(f'\nPartiulars\tRate\tQuantity\tAmount\n')
         
        for i in self.item:
            r+=str(i)
            r+=(f'\n')
            self.__total+=i._amount()
        r+=(f'\n\t\t\t\t\tTotal :{self.__total}')
        r+=(f'\nsignature :{input("enter signature : ")}')
        r+=('\nAdress: Basement # 2, Allahwala Plaza, Markaz K8, Islamabad')   
        return  r

# class Date:
#     # def __new__(cls,self):
#     #    day,month,year=map( int,self.split( )) 
#     #    instance = super().__new__(cls)
#     #    instance.__init__(day, month,year)  
#     #    instance.day=day
#     #    instance.month=month
#     #    instance.year=year
       
#     #    return instance

class Date:
    def __init__(self,date,month,year):
        self.date=date
        self.month=month
        self.year=year
    def __str__(self):
        return(f"{self.date}/{self.month}/{self.year}")
        
class address :

    def __init__(self,hno,town,city):
        self.hno=hno
        self.town=town
        self.city=city
    def __str__(self):
        return (f'{self.hno} {self.town} , {self.city}')
    

class item_line:
    def __init__(self,qty,product,rate):
        self.qty=qty
        self.product=product
        self.rate=rate
        
    def __str__(self) :
        return (f"{self.product}\t{self.rate}\t{self.qty}\t{self._amount()}")
    
    def _amount (self):                 #protected
        a=(self.qty)*(self.rate)     
        return a
    


def main():
    print("ADDRESS INFO")
    house_no = input("Enter House Number: ")
    town = input("Enter Town: ")
    city = input("Enter City: ")
    user_address = address(house_no, town, city)  #user address information
    d=Date(12,'may',2023)                       #Date
    i=[item_line(2,"handsfree",200),item_line(4,"charger cable",500),item_line(1,'laptop',50000)] #items on bill
    b=(bill_line(7567,d,"john",i,user_address))         #Bill
    print(b)
    
if __name__ == "__main__":
    main()







