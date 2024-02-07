from model.user import User


class Post:

    def __int__(self, body: str, author: User):
        self.body = body
        self.author = author
