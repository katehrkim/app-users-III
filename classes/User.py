from classes.post import Post
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.posts = []
    
    def make_post(self, post_obj):
        post_dict = {
            'title': post_obj.title,
            'content': post_obj.content
        }
        self.posts.append(Post(**post_dict))

    def print_posts(self):
        for post in self.posts:
            print(f'{post.title}: {post.content}')
    
