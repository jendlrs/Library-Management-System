#Library Management System

#Importing Libraries
import datetime
import os
import time
import sys
from time import sleep
import colorama
from colorama import Fore, Back, Style
#os.getcwd()

class LMS:
    """
    This class is used to keep records of books library.
    It has total six modules: 'Display Books', 'Issue Books', 'Add Books', 'Return Books',
    'list_of_books' should be txt file. 'library_name' should be string.
    """

    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
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
            Id += 1

    def display_books(self):
        time.sleep(1)
        print(Fore.MAGENTA)
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄" , (Fore.WHITE) + "\033[1mLIST OF BOOKS\033[0m",  (Fore.MAGENTA) +"▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(Style.RESET_ALL)
        print("\t\t\t\033[1mBOOKS ID\033[0m", "\t\t\t\t", "\033[1mTITLE\033[0m")
        print(Fore.MAGENTA)
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(Style.RESET_ALL)
        time.sleep (1)
        # Extract book titles and IDs from self.books_dict
        book_titles = [value["books_title"] for key, value in self.books_dict.items()]
        book_ids = list(self.books_dict.keys())

        # Sort the book titles using insertion sort
        for i in range(1, len(book_titles)):
            j = i - 1
            key = book_titles[i]
            key_id = book_ids[i]
            while j >= 0 and book_titles[j] > key:
                book_titles[j + 1] = book_titles[j]
                book_ids[j + 1] = book_ids[j]
                j -= 1
            book_titles[j + 1] = key
            book_ids[j + 1] = key_id

    # Print the sorted book titles and IDs
        for i in range(len(book_titles)):
            print("\t\t\t", book_ids[i], "\t\t\t", book_titles[i], "- >", (Fore.BLUE) + self.books_dict[book_ids[i]]["Status"],(Style.RESET_ALL)+ "")
        print(Fore.MAGENTA)
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        time.sleep(2)
    
    def Issue_books(self):
        books_id = input ("\nEnter the book's ID: ")
        current_date = datetime.datetime.now().strftime ("%Y-%m_%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]["Status"] == "Available":
                print(f"This book is already issued to {self.books_dict[books_id]['lender_name']} on {self.books_dict[books_id]['issue_date']}")
                return self.Issue_books()
            elif self.books_dict[books_id]['Status'] == "Available":
                name = input ("\nEnter your name: ")
                self.books_dict[books_id]['lender_name'] = name
                self.books_dict[books_id]['issue_date'] = current_date
                self.books_dict[books_id]['Status'] = "Already Issued"

                text = ("\nProcessing your request ....\n")
                animate(text)

                time.sleep(1)
                print ("\n\033[1mBooks Issued Successfully!\033[0m")
                print(Fore.MAGENTA)
                print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")

        else:
            print("\033[1mBook ID not found!\033[0m")
            return self.Issue_books()

    def add_books(self):
        new_books = input("\nEnter the title of the book: ")
        if new_books == "":
            return self.add_books()
        elif len(new_books) > 25:
            print("The book's title is too long! Title length should be 20 chars")
            return self.add_books()
        else:
            with open(self.list_of_books, "a") as bk:
                bk.writelines(f"\n{new_books}\n")
                self.books_dict.update({str(int(max(self.books_dict))+1):{
                'books_title':new_books, 
                'lender_name':"", 
                'issue_date':"", 
                'Status':"Available"}})

                text = ("\nAdding the books to the system ....\n")
                animate(text)

                time.sleep(1)
                print (f"\nThe book '\033[1m{new_books}\033[0m' has been added successfully!")
                print(Fore.MAGENTA)
                print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")

    def return_books(self):
        books_id = input ("\nEnter the book's ID: ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["Status"] == "Available":
                print("This book is already available in library. Please check your book ID.")
                return self.return_books()
            elif not self.books_dict[books_id]["Status"] == "Available":
                self.books_dict[books_id]['lender_name'] = ""
                self.books_dict[books_id]['Issue_date'] = ""
                self.books_dict[books_id]['Status'] = "Available"
            
                text = ("\nProcessing your request ....\n")
                animate(text)

                time.sleep(1)
                print("\n\033[1mSuccessfully Returned!\033[0m")
                print(Fore.MAGENTA)
                print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")

        else:
            print("Book ID is not found")

    def search_books(self, book_title):
        # Remove leading and trailing white spaces and convert to lowercase
        book_title = book_title.strip().lower()
    
        # Extract book titles and IDs from self.books_dict
        book_titles = [value["books_title"].strip().lower() for key, value in self.books_dict.items()]
        book_ids = list(self.books_dict.keys())
    
        # Sort the book titles and IDs together
        book_titles, book_ids = zip(*sorted(zip(book_titles, book_ids))) #zip takes iterable or containers and return a single iterator
    
        # Perform binary search for the book title
        low = 0
        high = len(book_titles) - 1

        text = ("\nSearching the Library ....")
        animate(text)

        time.sleep(2)
        while low <= high:
            mid = (low + high) // 2
            bt = book_titles[mid].replace('"', '')
            if bt == book_title:
                print(f"\n\nBook '\033[1m{book_title}\033[0m' was found in the Library. Press D to Display the books.")
                print(Fore.MAGENTA)
                print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
                return book_ids[mid]
            elif book_titles[mid] < book_title:
                low = mid + 1
            else:
                high = mid - 1
    
        print(f"\nBook '\033[1m{book_title}\033[0m' was not found in the Library.")
        return None

#To add typewriter effect
def animate(text):
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep (0.03)


try:
    myLMS = LMS("list_of_books.txt", "Python's")
    press_key_dict = {"D": "Display Books",
                    "I":"Issue Books",
                    "A": "Add Books", 
                    "R": "Return Books",
                    "S": "Search Books",
                    "Q": "Quit"}    
    key_press = False
    while not (key_press == "q"):
        time.sleep(0.5)
        print(Fore.MAGENTA)
        print(f"\n▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄"+(Fore.WHITE)+f" Welcome To \033[1m{myLMS.library_name} Library Management System \033[0m" + (Fore.MAGENTA)+"▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n")
        print(Style.RESET_ALL)
        for key, value in press_key_dict.items():
            print("                                           Press", (Fore.BLUE)+ key, (Style.RESET_ALL)+ "To", (Fore.BLUE)+value, (Style.RESET_ALL) + "                                             ")
        print(Fore.MAGENTA)
        print("\n▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(Style.RESET_ALL)
        time.sleep(0.5)
        key_press = input ("\n\033[1mPRESS KEY: \033[0m").lower()
        if key_press == "i":
            text = ("\nCurrent Selection: Issue Books\n")
            animate(text)
            myLMS.Issue_books()
        elif key_press == 'd':
            time.sleep(1)
            text = ("\nCurrent Selection: Display Books\n")
            animate(text)
            myLMS.display_books()
        elif key_press == 'a':
            text = ("\nCurrent Selection: Add Books\n")
            animate(text)
            myLMS.add_books()
        elif key_press == 'r':
            text = ("\nCurrent Selection: Return Books\n")
            animate(text)
            myLMS.return_books()
        elif key_press == 's':
            text = ("\nCurrent Selection: Search Books\n")
            animate(text)
            searchBook = input("\nEnter the the title of the book to search: ")
            myLMS.search_books(searchBook)
        elif key_press == 'q':
            print("\nThank you for using the Library!\n")
            break
        else:
            continue    

except Exception as e:
    print("Something went wrong. Please check your input")
