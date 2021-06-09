from classes.post import Post
from classes.User import User
class PremiumUser(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.type = 'premium'

    def make_post(self, post_obj):
        super().make_post(post_obj)
    
    def print_posts(self):
        super().print_posts()
    
