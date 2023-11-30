# define the book class
class Book:
    def __init__(self,title,author,page):
        self.title = title
        self.author = author
        self.page = page
    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, Page: {self.page}")

book1 = Book("Intro to python","Erric mathes",524)
book1.display()
