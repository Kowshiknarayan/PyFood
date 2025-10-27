from Pyfood.Models.abstractitem import AbstractItem
from Pyfood.Models.fooditems import FoodItems

class FoodMenu(AbstractItem):
    def __init__(self,name):
        super().__init__(name)
        self.__FoodItems=[]

    @property
    def FoodItems(self):
        return self.__FoodItems

    @FoodItems.setter
    def FoodItems(self,items):
        for item in items:
            if not isinstance(item,FoodItems):
                print('Invalid option')
                return
        self.__FoodItems=items

    def DisplayItem(self,start):
        print(f'{start}-> {self.name}\n')
