from Pyfood.Models.user import User

class Usermanager:
    __users=[]

    @classmethod
    def verification(cls,mail,number,password):
        # if len(str(number))==10:
        #     if len(password)>8:
        #         if '.com' in mail and '@' in mail:
        #             return True
        #         else:
        #             return 'mail'
        #     else:
        #         return 'pass'
        # else:
        #     return 'number'
        return True


    @classmethod
    # no need to create object for this method.
    # directly access by class name
    def AddUser(cls,userobj):
        if isinstance(userobj,User):
            cls.__users.append(userobj)
            print('You are Registered successfully')
        else:
            print('invalid user')

    @classmethod
    def FindUser(cls,username,userpassword):
        for user in cls.__users:
            if user.name==username and user.password==userpassword:
                return user
        else:
            return None