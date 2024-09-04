#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand = None, size = None):
        self.brand = brand
        self.size = size
        

    def get_brand(self):
        return self._brand

    def set_brand(self, new_brand):
        if isinstance(new_brand, str):
            print(new_brand)
            self._brand = new_brand
        else:
            print("Enter a new shoe brand")

    brand = property(get_brand, set_brand)

    def get_size(self):
        return self._size

    def set_size(self, new_size):
        if isinstance(new_size, int) and (new_size > 0):
            self._size = new_size
        else:
            print("size must be an integer")


    def cobble(self, condition = "New"):
        print("Your shoe is as good as new!")
        self.condition = condition

    size = property(get_size, set_size, cobble)
