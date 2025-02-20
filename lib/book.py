#!/usr/bin/env python3

class Book:
    def __init__(self,title,page_count):
        self.title=title
        self.page_count=page_count
    
    @property
    def page_count(self):
        # print("Fetching page count....")
        return self._page_count
        # self._title

    @page_count.setter
    def page_count(self,page_count):
        if type(page_count) == int:
            # self._title=title
            self._page_count=page_count
            
        else:
            print("page_count must be an integer")
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

b = Book('The River and the Source',321) 
b.page_count
b.title
    # page_count(page_count)
# Book.page_count()
# hubo=Book(title,page_count)