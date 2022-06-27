class Photo:
    def __init__(self, post):
        self.post = post.json()

    def get_server(self):
        return self.post['server']

    def get_hash(self):
        return self.post['hash']

    def get_photo(self):
        return self.post['photo']

    def get_upload_url(self):
        return self.post['response']['upload_url']

    def get_save_photo_id(self):
        return self.post['response'][0]['id']
