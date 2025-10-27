class Cart:
    def __init__(self,items,choices):
        self.choices=choices
        self.itemss=self.__AddCart(items)

    def __AddCart(self,itemss):
        foodDict={}
        for choice in self.choices:

            if choice > len(itemss):
                raise KeyError

            if choice in foodDict:
                foodDict[choice]+=1
            else:
                foodDict[choice]=1
        print(foodDict)
        return foodDict

    def ProcessOrder(self,foodItems):
        TotalPrice=0
        for item in self.itemss:
            Price=self.itemss[item]*foodItems[item-1].price
            TotalPrice+=Price
            print(f'{foodItems[item-1].name} X {self.itemss[item]} = {Price}')
        print(f'Total is {TotalPrice}')