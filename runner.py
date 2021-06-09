# Import and create your users here
from classes.app import App
from classes.User import User
from classes.FreeUser import FreeUser
from classes.PremiumUser import PremiumUser

my_app = App()
kate = FreeUser('kate', 'kimkat@umich.edu')
my_app.add_user(kate)
my_app.print_users
koyote = PremiumUser('koyote', 'koyote@gmail.com')
my_app.add_user(koyote)
my_app.print_users