#!/usr/bin/env python3
# from book import Book
class Shoe:
    def __init__(self,brand,size):
        self.brand = brand
        self.size = size
    
    @property
    def size(self):
        print("Get shoe size ...")
        return self._size

    @size.setter
    def size(self,size):
        if type(size) == int:
            self._size=size
        else:
            print("size must be an integer")

    def repair(self):
        print("shoe has been repaired")

    def cobble(self):
        print("Your shoe is as good as new!")
        setattr(self,"condition","New")
        return ("says that the shoe has been repaired.")

s=Shoe("Jordan",23)
setattr(s,"condition","New")