from Pyfood.Models.abstractitem import AbstractItem
from Pyfood.Models.foodmenu import FoodMenu

class Restaurant(AbstractItem):
    def __init__(self,name,rating,location,offer):
        super().__init__(name,rating)
        self.location=location
        self.offer=offer
        self.FoodMenus=[]

    @property
    def FoodMenus(self):
        return self.__FoodItems

    @FoodMenus.setter
    def FoodMenus(self,items):
        for item in items:
            if not isinstance(item,FoodMenu):
                print('Invalid option')
                return
        self.__FoodItems=items

    def DisplayItem(self,start):
        print(f'>>{start}-> {self.name} => Rating: {self.rating}')