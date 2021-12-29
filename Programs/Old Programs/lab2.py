import math
class Receipt():
    def __init__(self,purchases=list()):
        self.__tax_rate = .07
        self.__purchases = purchases
        
    def GetTax(self):
        return self.__tax_rate
    
    def __str__(self):
        import datetime
        sidespace = int((40 - len(str(datetime.datetime.now())))/2)
        sidespace_ = "-" * sidespace
        print(sidespace_+str(datetime.datetime.now())+sidespace_)
        
        subtotal = float()
        total = float()
        tax = float()
        
        for i in range(0,len(self.__purchases)):
            obj = self.__purchases[i]
            print(obj)
            total += obj.GetPrice()
            subtotal += obj.GetAltPrice()
            if obj.GetTax() == True:
                tax = obj._Item__price * self.GetTax()
        
        print('')
        space = 40 - len('Sub Total') - len(str(round(subtotal,2)))
        print('Sub Total'+('_'*space)+str(round(subtotal,2)))
        space = 40 - len('Tax') - len(str(round(tax,2)))
        print('Tax'+('_'*space)+str(round(tax,2)))
        space = 40 - len('Total') - len(str(round(total,2)))
        print('Total'+('_'*space)+str(round(total,2)))
        
        return ''
        
    def additem(self,object):
        self.__purchases.append(object)
    
class Item():
    def __init__(self,name = "",price=0,taxable=True):
        self.__name = name
        self.__price = price
        self.__taxable = taxable
        
    def GetPrice(self):
        price = self.__price
        if self.__taxable == True:
            price = self.__price + (self.__price * Receipt().GetTax())
        return price
    
    def GetTax(self):
        return self.__taxable
    
    def __str__(self):
        space = 40 - len(self.__name) - len(str(self.GetPrice()))
        return(self.__name + ("_"*space) + str(self.__price))
    
    def GetAltPrice(self):
        return self.__price
           

def Menu(receipt):
    item_Name = input('Enter Item name: ')
    item_Price = float(input('Enter Item Price: '))
    item_isTaxable = input('Is the item taxable (yes/no): ')
    item_Taxable = True
    
    if item_isTaxable.lower().strip() == "yes":
        item_Taxable = True
    elif item_isTaxable.lower().strip() == "no":
        item_Taxable = False
    
    userItem = Item(item_Name,item_Price,item_Taxable)
    receipt.additem(userItem)
    
    reMenu = input('Add another item (yes/no): ')
    if reMenu.lower().strip() == 'yes':
        Menu()
    else:
        print(receipt)
        
list = []
if __name__ == '__main__':
    print('Welcome to Receipt Creator')
    p1 = Receipt()
    Menu(p1)