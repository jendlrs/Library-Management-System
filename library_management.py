#Library Management System

#Importing Libraries
import datetime
import os
#os.getcwd()

class LMS:
    """ This class is used to keep record of books library
    It has total four module: "Display book, "Issue Books", "Return Books", "Add Books" """

    def __init__(self, list_of_books, library_name):
        self.list_of_books = "list_of_books.txt"
        self.library_name = library_name
        self.books_dict = {} #This will contain books title, lender name, issue date, and book status
        Id = 101 #Starting ID

        #read the text file
        with open (self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            print (line)

print (LMS("list-of_books.txt","Python's Library"))