
class Customer:
    def __init__(self):
        pass
    def __init__(self,CartObject):
        self.s_id=0
        self.s_name=""
        self.s_room=0
        self.CartObject=CartObject

    @classmethod
    def searchItem(self,item):
        for list in shopList:
            if item.capitalize() == list[0]:
                print("{:<15}{:<15}{:<10}{:<10}".format("Product","Category","Price","Quantity"))
                print("{:<15}{:<15}{:<10}{:<10}".format(list[0], list[1], list[2], list[3]))
                return True

    @classmethod   
    def displayItems(self):
        print("{:<15}{:<15}{:<10}{:<10}".format("Product","Category","Price","Quantity"))
        for categ in categories:
            for list in shopList:
                if list[1] == categ:     
                    print("{:<15}{:<15}{:<10}{:<10}".format(list[0], list[1], list[2], list[3]))

    @classmethod
    def showDiscount(self):
        print("Discounted items: ")
        for list in shopList:
            if (list[4] != 0):
                print("{:<15}{:<5}%".format(list[0],list[4]))  

    def payment(self,mode):
        if mode == "SWD":
            self.s_id = input("Enter your BITS ID: ")
            self.s_name = input("Enter your Name: ")
            self.s_room = input("Enter your Room Number: ")
            details_check = [self.s_id,self.s_name,self.s_room]
            if details_check in Admin.details: #details is list containing student login details in admin class 
                print("Login Successful!")
                return True
            else:
                print("Invalid details. Please try again!")
                return False
        elif mode == "CASH":
            print("Please pay cash later to our employee")
            return True
        elif mode == "UPI":
            print("Please scan the QR Code later.")
            return True

class ShopCart: 
    def __init__(self):   
        self.cart_quantity = []
        self.cart_items = []
        self.cart_price = []
        self.cart_category = []
        self.cart_discount = []

    def addItem(self):
        item = input("Enter product name to be added: ")
        
        for list in shopList:
            if item.capitalize() == list[0]:
                    if (list[0] in self.cart_items):
                        quantity=int(input("The product is already in your cart, enter new Quantity:"))#When a particular product is re-added, it reassigns the quantity instead of adding
                        if quantity>list[3]:
                            print("Quantity exceeds our stock!")
                            return True
                        index =self.cart_items.index(list[0])
                        self.cart_quantity[index] =quantity 
                        print("Item added.")
                        return True         
                        
                    else:
                        quantity = int(input("Enter quantity: "))
                        if quantity>list[3]:
                            print("Quantity exceeds our stock!")
                            return True
                        self.cart_quantity.append(quantity) 
                        self.cart_items.append(item.capitalize())
                        self.cart_price.append(list[2])
                        self.cart_category.append(list[3])
                        self.cart_discount.append(list[4])
                        print("Item added.")
                        return True
        #return True

    def delItem(self):
        item = input("Enter product name to be deleted: ")
        for cart_item in self.cart_items:
            if item.capitalize() == cart_item:
                item_index = self.cart_items.index(cart_item)
                self.cart_items.remove(cart_item) #deletes element by name
                del self.cart_quantity[item_index]# delete element by address
                print("Item  deleted")
            else:    
                print("No item found to be deleted")

    def displayBill(self):
        total_discount = 0
        total =0
        print("{:<15}{:<10}{:<10}{:<10}{:<10}".format("Product","Price","Quantity","Total","Discount%"))
        for i in range(len(self.cart_items)):
            discount = self.cart_price[i]*self.cart_quantity[i]*(self.cart_discount[i])/100
            total_discount +=discount 
            print("{:<15}{:<10}{:<10}{:<10}{:<10}".format(self.cart_items[i], self.cart_price[i], 
            self.cart_quantity[i],self.cart_price[i]*self.cart_quantity[i]-discount,self.cart_discount[i]))
            total += self.cart_price[i]*self.cart_quantity[i]-discount          
        print("Total amount to be paid: " + str(total))
        print("\nYou saved Rs. "+str(total_discount)+" shopping today!")    
        print("All prices are inclusive of taxes")
        exit()

class Admin:
    details = [
        ["2022A7PS0001P","Saksham Jain","100"],#Entered some values to chck if its wrking
        ["2022A7PS0000P","No Name","001"]] 
    def __init__(self):
        pass

shopList =[
    ["Jacket", "Clothes", 2000, 25,10],
    ["Cap", "Clothes", 400, 40,0],    
    ["Mouse", "Electronics", 500, 16,5],
    ["Charger", "Electronics", 300, 30,3],
    ["Biscuit", "Food", 20, 640,0],
    ["Chips", "Food", 20, 80,0],
    ["Pen", "Stationery", 10, 1100,0],
    ["Notebook", "Stationery", 80, 500,0],
    ["Handwash", "Toiletry", 70, 160,0],
    ["Toothpaste", "Toiletry", 100, 140,1]
]
categories=[]
for list in shopList:
    if list[1] not in categories:
        categories.append(list[1])
print('''
    Select if you are Customer or Admin
    1.Customer
    2.Admin''')
choice1 = input("Enter-")
if choice1 == "1":   
    sCart1 =ShopCart() # Creates a Shopping Cart object
    cust1 =Customer(sCart1) # Creates a Cutomer object and passes Shopping cart object for that Customer
    mode = input('''
    Enter mode of payment:
    SWD CASH UPI
    ''')
    if(cust1.payment(mode)==True):
        while(True):
            print('''
            Select a number for what you would like to do:
            1. View Shopping List
            2. Add item to Shopping List
            3. Delete item from Shopping List
            4. Search for an item from List
            5. Show Available Discounts
            6. Print Bill
            0. Exit
        ''')
        
            choice =input("Enter- ")
            if choice ==0:
                break
            elif choice == "1":
                cust1.displayItems()
            elif choice == "2":
                if(cust1.CartObject.addItem()!=True):
                    print("Wrong product entered.")
            elif choice =="3":
                cust1.CartObject.delItem()
            elif choice == "4":
                item = input("Enter item name to be searched-")
                if(cust1.searchItem(item)!=True):
                    print("Product not found.")
            elif choice == "5":
                cust1.showDiscount()
            elif choice == "6":
                cust1.CartObject.displayBill()
            else:
                print("Invalid choice.")
                break
elif choice1 =="2":
    admin1=Admin()
    Customer.displayItems() #Could not complete its functionality due to time
