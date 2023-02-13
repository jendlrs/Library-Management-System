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
        self.books_dict = {} #This dictionary will contain books title, lender name, issue date, and book status
        Id = 101 #Starting ID

        #read the text file
        with open (self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            self.books_dict.update({str(Id):{ #Updating Dictionary
            "books_title":line.replace("\n", ""), 
            "lender_name": "",
            "Issue_date": "", 
            "Status":"Available"}})
            Id = Id + 1

    def display_books(self):
        print("------------------------List of Books---------------------")
        print("Books ID", "\t", "Title")
        print("----------------------------------------------------------")

        for key, value in self.books_dict.items():
            print(key, "\t\t", value.get("books_title"), "- [", value.get("Status"),"]")

l = LMS("List_of_books.txt", "Python's Library")
print(l.display_books())