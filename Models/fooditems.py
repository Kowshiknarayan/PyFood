from Pyfood.Models.abstractitem import AbstractItem

class FoodItems(AbstractItem):
    def __init__(self,name,rating,price,desc):
        super().__init__(name,rating)
        self.price=price
        self.desc=desc

    def DisplayItem(self,start):
        print(f'{start}-> Name: {self.name}, Rating: {self.rating}, Price: {self.price}')