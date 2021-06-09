from classes.User import User
from classes.PremiumUser import PremiumUser
from classes.FreeUser import FreeUser
class App:
    def __init__(self):
        self.users = []
    
    def add_user(self, user_obj):
        user_dict = {
            'name': user_obj.name,
            'email': user_obj.email
        }
        if user_obj.type == 'premium':
            self.users.append(PremiumUser(**user_dict))
        else:
            self.users.append(FreeUser(**user_dict))
        
    
    def print_users(self):
        for user in self.users:
            print(f'{user.name}: {user.email}')