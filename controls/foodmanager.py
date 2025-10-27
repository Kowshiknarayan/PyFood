from Pyfood.Models.foodmenu import FoodMenu
from Pyfood.Models.fooditems import FoodItems
from Pyfood.Models.restaurant import Restaurant

class FoodManager:
    def __init__(self):
        self.Restaurants=self.__PrepareRestaurant()

    def __PrepareFoodItems(self):
        item1 = FoodItems('Veg Biriyani',4.1,170,'******')
        item2 = FoodItems('Panner Biriyani',4.5,210,'******')
        item3 = FoodItems('Mutton Biriyani', 3.4, 230, '******')
        item4 = FoodItems('Pork Biriyani', 4.2, 220, '******')
        item5 = FoodItems('Chicken Noodles', 3.7, 200, '******')
        return [item1,item2,item3,item4,item5]

    def __PrepareFoodMenus(self):
        foods=self.__PrepareFoodItems()
        menu1=FoodMenu('veg')
        menu1.FoodItems=[foods[0],foods[1]]
        menu2=FoodMenu('Non-veg')
        menu2.FoodItems=[foods[2],foods[3],foods[4]]
        menu3=FoodMenu('Chinese')
        menu3.FoodItems=[foods[4]]
        return [menu1,menu2,menu3]

    def __PrepareRestaurant(self):
        FoodMenus=self.__PrepareFoodMenus()
        res1 = Restaurant('A2B',5,'chennai',10)
        res1.FoodMenus=[FoodMenus[0]]
        res2 = Restaurant('Saravana Bhavan', 5, 'Bangalore', 10)
        res2.FoodMenus=[FoodMenus[0]]
        res3 = Restaurant('Bilal', 5, 'Hyderabad', 10)
        res3.FoodMenus=[FoodMenus[1],FoodMenus[2]]
        return [res1,res2,res3]

    def FindRestaurant(self,name):
        for res in self.Restaurants:
            if res.name in name:
                return res

    def ShowItem(self):
        items=self.__PrepareFoodItems()
        return items