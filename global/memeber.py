class Member:
    def __init__(self, name, last_name, borrowed_books=None):
        self.name = name
        self.last_name = last_name
        self.borrowed_books = borrowed_books if borrowed_books is not None else []

    
    def get_member_name(self):
            return self.name
    
    def get_last_name(self):
         return self.last_name
        


