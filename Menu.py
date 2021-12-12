class MenuJT:#Class Name
    def __init__(self,name,amount):#Initial Method
        self.name=name
        self.amount=amount
        self.price=0
        self.total=0

    def __PricelistJT(self):#Making the list of products and its price attributes private using "__"
        if self.name.lower() == "dry cured iberian ham":
            self.price = 177.8 
        elif self.name.lower() == "wagyu steak":
            self.price = 450
        elif self.name.lower() == "matsutake mushrooms":
            self.price = 272
        elif self.name.lower() == "kopi luwak coffee":
            self.price = 306.5
        elif self.name.lower() == "moose cheese":
            self.price = 487.2
        elif self.name.lower() == "white truffles":
            self.price = 3600
        elif self.name.lower() == "blue fin tuna":
            self.price = 3603
        elif self.name.lower() == "le bonnotte potatoes":
            self.price = 270.81
        else:
            self.price = 0
    
    def totalPriceJT(self):
        self.__PricelistJT()
        self.total=self.price*self.amount
        return self.total

    def __str__(self):
        self.__Pricelist()
        return f"Name: {self.name}\n Amount: {self.amount}\n Price: {self.price}\n Total: {self.total}"

    def getPriceJT(self):
        self.__PricelistJT()
        return self.price