class Post:
    def __init__(self, post):
        self.post = post.json()

    def get_id(self):
        return self.post['response']['post_id']