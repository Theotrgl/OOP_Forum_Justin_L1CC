from Menu import MenuJT#import class

def listJT():#Basically creating a loop to make sure the user input is valid
    shoppingListJT=[]

    while True:
        number_amount=eval(input("Amount of items: "))
        if number_amount<1:
            print("Amount has to be at least 1")
        else:
            break
    for i in range (number_amount):
        while True:
            itemName=input("What do you want to buy: ")
            mass=eval(input("How much(lbs): "))
            item=MenuJT(itemName,mass)
            if itemName=="" or item.getPriceJT()==0:
                print("Enter Valid Item Name!")
            elif mass<0:
                print("Mass has to be more than 0")
            else:
                break
        shoppingListJT.append(item)
    return shoppingListJT

def displayJT(itemList):
    print("-----------------------------------")#For aesthetics??
    print("The following are your purchased items: ")
    for i in range(len(itemList)):
        print(f"Item {i+1}")
        print(itemList[i].totalPriceJT())

def totalCostJT(itemList):
    total=0
    for i in range(len(itemList)):
        total+=itemList[i].totalPriceJT()
        return total

shoppingListJT=listJT()#PrintOut Command
displayJT(shoppingListJT)
print(f"Total:${totalCostJT(shoppingListJT)}"
)

