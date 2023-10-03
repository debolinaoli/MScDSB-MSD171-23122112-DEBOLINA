#create a class restrurant,that accepts/ item name and quantity as input/ inside your class you having the item/ and its cost(unit price) as a dictionary/ create a function and total cost...........  calculate total cost/ that prints the itemname quantity
class resturant:
    def __init__(self,itemname,qty):
        self.itemname = itemname 
        self.qty = qty
        self.menuitems = {
               "rice" : 30,
               "chicken": 60,
               "dal": 40
        }
    def totalcost(self):
        print("total cost of the order ")
        print("item\t\t:", self.itemname)
        print("quantity\t:", self.qty)
        total = self.qty * self.menuitems[self.itemname]
        print("total\t\t:" , total)
        
order = resturant("rice",90)
order.totalcost()
def totalcost(self):
        print("total cost of the order ")
        print("item\t\t:", self.itemname)
        print("quantity\t:", self.qty)
        total = self.qty * self.menuitems[self.itemname]
        print("total\t\t:" , total)
        
order = resturant("rice",90)
order.totalcost()
order = resturant("chicken",90)
order.totalcost()
order = resturant("dal",90)
order.totalcost()