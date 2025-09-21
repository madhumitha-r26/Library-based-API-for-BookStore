# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 21:38:09 2025

@author: Madhumitha
"""

from BookStore_API import BookStore

class LibraryManager:
    def __init__(self, bookstore):
        self.bookstore = bookstore
        
    def add_book_to_store(self, id, title, author, year, genre):
        new_book = self.bookstore.add_book(id, title, author, year, genre)
        
if __name__ == "__main__":
    bookstore = BookStore()
    manager = LibraryManager(bookstore)
    manager.add_book_to_store(1, "great gats", "scott", 1925, "fiction")        
    print(bookstore.get_book_by_id(1)["title"])

