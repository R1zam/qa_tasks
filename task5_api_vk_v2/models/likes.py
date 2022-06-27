class Likes:
    def __init__(self, post):
        self.post = post.json()

    def get_likes_list(self):
        return self.post["response"]["items"]
