class InventoryTemplate(object):
    def __init__(self, arg1, arg2):
        self.title = arg1
        self.description = arg2

    def __str__(self):
        # some generic method
        pass

    def __eq__(self):
        pass


class Book(InventoryTemplate):
    def __init__(self, arg1, arg2, arg3, arg4):
        # call parent's constructor, pass in 2 arguments
        super(Book, self).__init__(arg1=arg1, arg2=arg2)
        # notice the rest 2 arguments are passed to current object, not parent
        self.format = arg3
        self.author = arg4

    def __str__(self):
        # override parent's __str()__ method
        book_line = "{title} by {author}".format(
            title=self.title,
            author=self.author
        )

        return book_line
