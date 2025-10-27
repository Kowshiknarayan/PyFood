from Pyfood.Models.user import User
from Pyfood.Models.usermanager import Usermanager
from controls.foodmanager import FoodManager
from controls.mainmenu import MainMenu

class LoginSystem:
    @classmethod
    def Login(cls):
        user_name=input('Enter user name')
        user_password=input('Enter the password')
        verified_user = Usermanager.FindUser(user_name,user_password)
        if verified_user is not None:
            print(f'Welcome: {user_name}')
            menu = MainMenu()
            menu.start()
        else:
            print('Invalid Username/password')

    def Register(self):
        user_name=input('Enter user name')
        user_mail=input('Enter mail Id')
        user_number=int(input("Enter the mobile number"))
        user_password=input('Enter the password')
        register_validation = Usermanager.verification(user_mail,user_number,user_password)
        if register_validation == True:
            userObj = User(user_name,user_mail, user_number, user_password)
            Usermanager.AddUser(userObj)
        elif register_validation == 'pass':
            print('enter password with minimum eight character')
        elif register_validation == 'mail':
            print('Enter valid mail id')
        elif register_validation == 'number':
            print('Enter valid 10 digit mobile number')
        # create object for each user


    def Guest(self):
        print('Thanks for GuestLogin')

    def Exit(self):
        print('Thankyou')
        exit()

    def Validation(self,option):

        try:
            getattr(self,option)()
        except ValueError:
            print('Invalid choice entered')

class FoodApp:
    # LoginOption is class member
    LoginOption={1:'Login',2:'Register',3:'Guest',4:'Exit'}
    @staticmethod
    def Init():
        print('\t Welcome to Pyfood Ordering App')
        loginObj=LoginSystem() #for accessing LoginSystem
        # if we need to access class member use it with class_name.variable

        menu = MainMenu()
        menu.start()


        # while True:
        #     for option in FoodApp.LoginOption:
        #         print(f'{option}:{FoodApp.LoginOption[option]}')
        #     try:
        #         userOption = int(input('Enter your choice: '))
        #         loginObj.Validation(FoodApp.LoginOption[userOption])
        #     except (KeyError,ValueError):
        #         print('Invalid input.. please enter valid choice')