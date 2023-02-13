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
            "issue_date": "", 
            "Status":"Available"}})
            Id = Id + 1

    def display_books(self):
        print("------------------------List of Books---------------------")
        print("Books ID", "\t", "Title")
        print("----------------------------------------------------------")

        for key, value in self.books_dict.items():
            print(key, "\t\t", value.get("books_title"), "- [", value.get("Status"),"]")

    def Issue_books(self):
        books_id = input ("Enter the book's ID: ")
        current_date = datetime.datetime.now().strftime ("%Y-%m_%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]["Status"] == "Available":
                print(f"This book is already issued to {self.books_dict[books_id]['lender_name']} \
                    on {self.books_dict[books_id]['issue_date']}")
                return self.Issue_books()
            elif self.books_dict[books_id]['Status'] == "Available":
                name = input ("Enter your name: ")
                self.books_dict[books_id]['lender_name'] = name
                self.books_dict[books_id]['issue_date'] = current_date
                self.books_dict[books_id]['Status'] = "Already Issued"
                print ("Books Issued Successfully! \n")

        else:
            print("Book ID not found!")
            return self.Issue_books()

l = LMS("List_of_books.txt", "Python's Library")
print(l.display_books())