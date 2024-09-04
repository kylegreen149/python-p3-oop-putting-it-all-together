#!/usr/bin/env python3

class Book:
    def __init__(self, title = None, page_count = None):
        self.title = title
        self.page_count = page_count

    def get_title(self):
        return self._title

    def set_title(self, new_title):
        if isinstance(new_title, str):
            print(new_title)
            self._title = new_title
        else:
            print("Enter a new title")

    title = property(get_title, set_title)


    def get_page(self):
        return self._page_count

    def set_page(self, new_page_count):
        if isinstance(new_page_count, int) and (new_page_count >= 0):
            # print("Flipping the page...wow, you read fast!")
            # new_page_count = new_page_count + 1
            self._page_count = new_page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        self._page_count + 1

    page_count = property(get_page, set_page, turn_page)

b1 = Book("Harry Potter", 30)
        