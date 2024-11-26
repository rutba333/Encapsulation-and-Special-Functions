class Computer:
    def __init__(self):
        self.max_price=900

    def sell(self):
        print("Selling price {}".format(self.max_price))

    def setMaxPrice(self,price):
        self.max_price=price

c=Computer()
c.sell()


#change the price
c.max_price=2000
c.sell()

#using setter function
c.setMaxPrice(2000)
c.sell()
        