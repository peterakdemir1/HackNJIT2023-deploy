class Image:
    def __init__(self, username: str, img_bson: bytes):
        self.username = username
        self.img_bson = img_bson