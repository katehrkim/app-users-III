from classes.post import Post
from classes.User import User
class FreeUser(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.type = 'free'
        self.limit = 2
    
    def make_post(self, post_obj):
        if self.limit > 0:
            super().make_post(post_obj)
            self.limit -= 1
        else:
            print('No more posts allowed!')
        
    def print_posts(self):
        super().print_posts()