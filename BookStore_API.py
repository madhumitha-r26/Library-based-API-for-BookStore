# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 21:37:17 2025

@author: Madhumitha
"""

class BookStore:
    def __init__(self):
        self.books = []
        
    def add_book(self, id, title, author, year, genre):
        new_book = {
            "id": id,
            "title": title,
            "author": author,
            "year": year,
            "genre": genre
        }
        self.books.append(new_book)
        return new_book
    
    def get_book_by_id(self, id):
        for book in self.books:
            if book['id'] == id:
                return book
        return None 

if __name__ == "__main__":
    bookstore = BookStore()
    b1 = bookstore.add_book(1, "great gats", "scott", 1925, "fiction")
    b2 = bookstore.add_book(2, "kill mockingbird", "harper lee", 1960, "fiction")
    print(bookstore.get_book_by_id(1)["title"])
