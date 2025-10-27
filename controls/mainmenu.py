from Pyfood.controls.foodmanager import FoodManager
from Pyfood.Models.cart import Cart

class MainMenu:
    __options={1:'Show Restaurant',2:'Show FoodItems',3:'Search Restaurant',4:'Search FoodItems',5:'Logout'}

    def __init__(self):
        self.__FoodManager=FoodManager()

    def ShowRestaurant(self):
        for i,res in enumerate(self.__FoodManager.Restaurants,1):
            res.DisplayItem(i)
        choice = int(input('Enter your choice'))
        res = self.__FoodManager.Restaurants[choice-1]
        self.ShowFoodMenus(res.FoodMenus)

    def ShowFoodItems(self,foodItems=None):
        if foodItems is not None:
            for i, foodItem in enumerate(foodItems,1):
                foodItem.DisplayItem(i)
            choices = list(map(int, input('Please your food items(eg: 1,2)').split(',')))
            cart = Cart(foodItems,choices)
            cart.ProcessOrder(foodItems)

        else:
            values=self.__FoodManager.ShowItem()
            for i,foodItem in enumerate(values,1):
                foodItem.DisplayItem(i)

    def SearchRestaurant(self):
        resName = input('Enter the Restaurant name:')
        res = self.__FoodManager.FindRestaurant(resName)
        if res is not None:
            print('Restaurant Found..')
            print(f'Name:{res.name} - Rating:{res.rating}')
            self.ShowFoodMenus(res.FoodMenus)
        else:
            print(f'No restaurant found')

    def SearchFoodItems(self):
        foodName=input('Enter the Food Name')
        pass


    def Logout(self):
        print('Thankyou Visit again')
        exit()

    def ShowFoodMenus(self, FoodMenus):
        print('List of menus available')
        for iterate,menu in enumerate(FoodMenus,1):
            menu.DisplayItem(iterate)
        choice=int(input('Please chose your menu'))
        foodItems=FoodMenus[choice-1].FoodItems
        self.ShowFoodItems(foodItems)

    def start(self):
        while True:
            for option in self.__options:
                print(f'{option}: {MainMenu.__options[option]}')
            try:
                choice = int(input('Enter your choice(number): '))
                value=MainMenu.__options[choice].replace(" ","")
                # print(value)
                getattr(self,value)()
            except (ValueError,KeyError):
                print('Invalid input.., please enter the valid choice')