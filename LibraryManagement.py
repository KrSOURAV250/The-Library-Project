import customtkinter as ctk
import tkinter as tk
import time


class Library(ctk.CTk):
    def __init__(self, listOfBooks):
        super().__init__()
        self.bookList = listOfBooks
        self.availableBooks = listOfBooks[:]
        self.lendedBooks = {}
        self.dispFramePresent = False
        self.addBookFramePresent = False
        self.wlcmUpper = False
        self.returnBookFramePresent = False
        self.lendBookFramePresent = False
        self.loadInitialGUI()

    def insertBooksToDisplay(self, bl, fromLst):
        for i in fromLst:
            bl.insert("end", f"  {i}")

    def dispFrame(self):
        if self.wlcmUpper == False:
            for i in range(250, 19, -1):
                self.wlcm.pack(pady=i)
                time.sleep(0.0000001)
        self.dispframe = ctk.CTkFrame(self, width=700)
        self.dispframe.pack(expand=1)

    def dispFrame1(self):
        self.dispframe1 = ctk.CTkFrame(
            self.dispframe, fg_color="#5269b3", width=700)
        self.dispframe1.pack(side="left", padx=5, pady=5, expand=1)

    def dispFrame2(self):
        self.dispframe2 = ctk.CTkFrame(
            self.dispframe, fg_color="#5269b3", width=700)
        self.dispframe2.pack(side="right",  padx=5, pady=5, expand=1)

    def displayBooksGUI(self):
        self.dispFrame1()
        self.bL = ctk.CTkLabel(
            self.dispframe1, text="Book List", font=("lucida", 18, "bold"))
        self.bL.pack()
        self.bookLst = tk.Listbox(
            self.dispframe1, font=("arial", 15, "bold"), bg="black", fg="white")
        self.insertBooksToDisplay(self.bookLst, self.bookList)
        self.bookLst.pack(ipadx=250, padx=5, pady=5, expand=1)
        self.sbDispBook = ctk.CTkScrollbar(
            self.bookLst, command=self.bookLst.yview)
        self.sbDispBook.pack(side="right", fill="y")
        self.bookLst.configure(yscrollcommand=self.sbDispBook.set)

    def displayAvaliableBooksGUI(self):
        self.dispFrame2()
        self.bL = ctk.CTkLabel(
            self.dispframe2, text="Available Book List", font=("lucida", 18, "bold"))
        self.bL.pack()
        self.bookLstAvailable = tk.Listbox(
            self.dispframe2, font=("arial", 15, "bold"), bg="white", fg="black")
        self.insertBooksToDisplay(
            self.bookLstAvailable, self.availableBooks)
        self.bookLstAvailable.pack(ipadx=250, padx=5, pady=5, expand=1)
        self.sbDispBookAva = ctk.CTkScrollbar(
            self.bookLstAvailable, command=self.bookLstAvailable.yview)
        self.sbDispBookAva.pack(side="right", fill="y")
        self.bookLstAvailable.configure(
            yscrollcommand=self.sbDispBookAva.set)

    def displayBooks(self):
        if self.returnBookFramePresent == True:
            self.returnBookframe.destroy()
            self.returnBookFramePresent = False
            self.dispFrame()
            self.dispFramePresent = True

            self.displayBooksGUI()
            self.displayAvaliableBooksGUI()
        elif self.lendBookFramePresent == True:
            self.lendBookframe.destroy()
            self.lendBookFramePresent = False
            self.dispFrame()
            self.dispFramePresent = True

            self.displayBooksGUI()
            self.displayAvaliableBooksGUI()
        elif self.addBookFramePresent == True:
            self.addBookframe.destroy()
            self.addBookFramePresent = False
            self.dispFrame()
            self.dispFramePresent = True

            self.displayBooksGUI()
            self.displayAvaliableBooksGUI()
        elif self.dispFramePresent == False:
            self.dispFrame()
            self.dispFramePresent = True

            self.displayBooksGUI()
            self.displayAvaliableBooksGUI()

    def lendBookFrame(self):
        if self.wlcmUpper == False:
            for i in range(250, 19, -1):
                self.wlcm.pack(pady=i)
                time.sleep(0.0000001)
            self.wlcmUpper = True
        self.lendBookframe = ctk.CTkFrame(self, fg_color="#1e1e1e")
        self.lendBookframe.pack(ipadx=60, ipady=35, pady=60)

        self.entrBookPresent = False
        self.entrYourNamePresent = False
        self.warningMessagePresent = False

    def warningMessage(self):
        if self.warningMessagePresent == False:
            self.warning = ctk.CTkLabel(
                self.lendBookframe, text="", text_color="red")
            self.warning.pack(pady=(25, 0))
            self.warningMessagePresent = True

    def bookUpdate(self, i):
        self.lendedBooks.update({self.bName: self.yourName.get()})
        self.availableBooks.pop(i)
        self.warningMessage()
        self.warning.configure(
            text="This Book is Booked For You, Enjoy Your Reading.")
        self.yourName.destroy()
        self.nameSub.destroy()
        self.entrYourNamePresent = False

    def bookSubmited(self):
        self.bName = self.bookName.get()
        for i in self.lendedBooks:
            if self.bName.lower() == i.lower():
                self.warningMessage()
                self.warning.configure(
                    text=f"Sorry! This Book is Not Avilable.\nThe Owner of {self.bName} Book is {self.lendedBooks.get(i)} Now.\nSo, Please Try After Some Times.")
                break
        else:
            for i in range(len(self.availableBooks)):
                if f"{self.bName.lower()}\n" == self.availableBooks[i].lower():
                    if self.entrYourNamePresent == False:
                        if self.warningMessagePresent == False:
                            self.yourName = ctk.CTkEntry(
                                self.lendBookframe, placeholder_text="Enter your Name")
                            self.yourName.pack(pady=(25, 0))
                            self.entrYourNamePresent = True
                            self.nameSub = ctk.CTkButton(
                                self.lendBookframe, text="Submit Name", command=lambda: self.bookUpdate(i))
                            self.nameSub.pack(pady=(25, 0))
                        else:
                            self.warning.destroy()
                            self.warningMessagePresent = False
                            self.yourName = ctk.CTkEntry(
                                self.lendBookframe, placeholder_text="Enter your Name")
                            self.yourName.pack(pady=(25, 0))
                            self.entrYourNamePresent = True
                            self.nameSub = ctk.CTkButton(
                                self.lendBookframe, text="Submit Name", command=lambda: self.bookUpdate(i))
                            self.nameSub.pack(pady=(25, 0))
                    break
            else:
                self.warningMessage()
                self.warning.configure(
                    text="This Book is Not in Library Now, We Will Bring This Book For You Later.")

    def lendBook(self):
        if self.dispFramePresent == True:
            self.dispframe.destroy()
            self.dispFramePresent = False
            self.lendBookFrame()
            self.lendBookFramePresent = True
            self.bookName = ctk.CTkEntry(
                self.lendBookframe, placeholder_text="Enter Name of Book That You are Searching", width=500)
            self.bookName.pack(pady=(60, 0))
            self.bookSub = ctk.CTkButton(
                self.lendBookframe, text="Submit", command=self.bookSubmited)
            self.bookSub.pack(pady=(25, 0))
        elif self.addBookFramePresent == True:
            self.addBookframe.destroy()
            self.addBookFramePresent = False

            self.lendBookFrame()
            self.lendBookFramePresent = True
            self.bookName = ctk.CTkEntry(
                self.lendBookframe, placeholder_text="Enter Name of Book That You are Searching", width=500)
            self.bookName.pack(pady=(60, 0))
            self.bookSub = ctk.CTkButton(
                self.lendBookframe, text="Submit", command=self.bookSubmited)
            self.bookSub.pack(pady=(25, 0))
        elif self.returnBookFramePresent == True:
            self.returnBookframe.destroy()
            self.returnBookFramePresent = False

            self.lendBookFrame()
            self.lendBookFramePresent = True
            self.bookName = ctk.CTkEntry(
                self.lendBookframe, placeholder_text="Enter Name of Book That You are Searching", width=500)
            self.bookName.pack(pady=(60, 0))
            self.bookSub = ctk.CTkButton(
                self.lendBookframe, text="Submit", command=self.bookSubmited)
            self.bookSub.pack(pady=(25, 0))
        elif self.lendBookFramePresent == False:
            self.lendBookFrame()
            self.lendBookFramePresent = True
            self.bookName = ctk.CTkEntry(
                self.lendBookframe, placeholder_text="Enter Name of Book That You are Searching", width=500)
            self.bookName.pack(pady=(60, 0))
            self.bookSub = ctk.CTkButton(
                self.lendBookframe, text="Submit", command=self.bookSubmited)
            self.bookSub.pack(pady=(25, 0))

    def addBookFrame(self):
        self.addBookframe = ctk.CTkFrame(self, fg_color="#1e1e1e")
        self.addBookframe.pack(pady=60)

    def getInptBook(self):
        bookName = self.inputBook.get()
        for i in self.bookList:
            if i == bookName:
                self.bookAlrdyPresent.configure(
                    text="This Book is Already in Library")
                break
        else:
            self.bookList.append(bookName)
            self.availableBooks.append(bookName)
            self.bookAlrdyPresent.configure(
                text=f"Your Book {bookName} is Submitted SuccessFully.")

    def addBooks(self):
        if self.wlcmUpper == False:
            for i in range(250, 19, -1):
                self.wlcm.pack(pady=i)
                time.sleep(0.0000001)
            self.wlcmUpper = True
        if self.returnBookFramePresent == True:
            self.returnBookframe.destroy()
            self.returnBookFramePresent = False
            self.addBookFrame()
            self.inputBook = ctk.CTkEntry(
                self.addBookframe, placeholder_text="Enter The Book Name", width=600)
            self.inputBook.pack(pady=60, padx=60)
            self.bookSubmitBtn = ctk.CTkButton(
                self.addBookframe, text="Submit", command=self.getInptBook)
            self.bookSubmitBtn.pack(pady=30)
            self.bookAlrdyPresent = ctk.CTkLabel(
                self.addBookframe, text="", font=("mesquito", 20, "normal"), text_color="red")
            self.bookAlrdyPresent.pack(pady=(10, 60))
            self.addBookFramePresent = True
        elif self.lendBookFramePresent == True:
            self.lendBookframe.destroy()
            self.lendBookFramePresent = False
            self.addBookFrame()
            self.inputBook = ctk.CTkEntry(
                self.addBookframe, placeholder_text="Enter The Book Name", width=600)
            self.inputBook.pack(pady=60, padx=60)
            self.bookSubmitBtn = ctk.CTkButton(
                self.addBookframe, text="Submit", command=self.getInptBook)
            self.bookSubmitBtn.pack(pady=30)
            self.bookAlrdyPresent = ctk.CTkLabel(
                self.addBookframe, text="", font=("mesquito", 20, "normal"), text_color="red")
            self.bookAlrdyPresent.pack(pady=(10, 60))
            self.addBookFramePresent = True
        elif self.dispFramePresent == True:
            self.dispframe.destroy()
            self.dispFramePresent = False
            self.addBookFrame()
            self.inputBook = ctk.CTkEntry(
                self.addBookframe, placeholder_text="Enter The Book Name", width=600)
            self.inputBook.pack(pady=60, padx=60)
            self.bookSubmitBtn = ctk.CTkButton(
                self.addBookframe, text="Submit", command=self.getInptBook)
            self.bookSubmitBtn.pack(pady=30)
            self.bookAlrdyPresent = ctk.CTkLabel(
                self.addBookframe, text="", font=("mesquito", 20, "normal"), text_color="red")
            self.bookAlrdyPresent.pack(pady=(10, 60))
            self.addBookFramePresent = True
        elif self.addBookFramePresent == False:
            self.addBookFrame()
            self.inputBook = ctk.CTkEntry(
                self.addBookframe, placeholder_text="Enter The Book Name", width=600)
            self.inputBook.pack(pady=60, padx=60)
            self.bookSubmitBtn = ctk.CTkButton(
                self.addBookframe, text="Submit", command=self.getInptBook)
            self.bookSubmitBtn.pack(pady=30)
            self.bookAlrdyPresent = ctk.CTkLabel(
                self.addBookframe, text="", font=("mesquito", 20, "normal"), text_color="red")
            self.bookAlrdyPresent.pack(pady=(10, 60))
            self.addBookFramePresent = True

    def returnBookk(self):
        self.bookNameR = self.entrReturnBookName.get()
        for i in self.lendedBooks:
            if self.bookNameR.lower() == i.lower():
                self.lendedBooks.pop(i)
                if self.returnBookWarning == False:
                    self.bookReturned = ctk.CTkLabel(
                        self.returnBookframe, text="Your Book is Returned SuccessFully.", text_color="red")
                    self.bookReturned.pack()
                    self.returnBookWarning = True
                else:
                    self.bookReturned.configure(
                        text="Your Book is Returned SuccessFully.")
                self.availableBooks.append(self.bookNameR)
                break
        else:
            if self.returnBookWarning == False:
                self.bookReturned = ctk.CTkLabel(
                    self.returnBookframe, text="Enter Valid Book Name", text_color="red")
                self.bookReturned.pack()
                self.returnBookWarning = True

            else:
                self.bookReturned.configure(
                    text="Enter Valid Book Name")

    def returnBookFrame(self):
        self.returnBookframe = ctk.CTkFrame(self, fg_color="#1e1e1e")
        self.returnBookframe.pack(ipadx=60, ipady=60, pady=60)
        self.returnBookWarning = False

    def retrnBook(self):
        if self.wlcmUpper == False:
            for i in range(250, 19, -1):
                self.wlcm.pack(pady=i)
                time.sleep(0.0000001)
            self.wlcmUpper = True
        if self.addBookFramePresent == True:
            self.addBookframe.destroy()
            self.addBookFramePresent = False

            self.returnBookFrame()
            self.returnBookFramePresent = True
            self.entrReturnBookName = ctk.CTkEntry(
                self.returnBookframe, placeholder_text="Enter Name of Book That You Want To Return", width=500)
            self.entrReturnBookName.pack(pady=(60, 25))
            self.returnBookSub = ctk.CTkButton(
                self.returnBookframe, text="Submit", command=self.returnBookk)
            self.returnBookSub.pack(pady=(0, 25))
        elif self.lendBookFramePresent == True:
            self.lendBookframe.destroy()
            self.lendBookFramePresent = False

            self.returnBookFrame()
            self.returnBookFramePresent = True
            self.entrReturnBookName = ctk.CTkEntry(
                self.returnBookframe, placeholder_text="Enter Name of Book That You Want To Return", width=500)
            self.entrReturnBookName.pack(pady=(60, 25))
            self.returnBookSub = ctk.CTkButton(
                self.returnBookframe, text="Submit", command=self.returnBookk)
            self.returnBookSub.pack(pady=(0, 25))
        elif self.dispFramePresent == True:
            self.dispframe.destroy()
            self.dispFramePresent = False

            self.returnBookFrame()
            self.returnBookFramePresent = True
            self.entrReturnBookName = ctk.CTkEntry(
                self.returnBookframe, placeholder_text="Enter Name of Book That You Want To Return", width=500)
            self.entrReturnBookName.pack(pady=(60, 25))
            self.returnBookSub = ctk.CTkButton(
                self.returnBookframe, text="Submit", command=self.returnBookk)
            self.returnBookSub.pack(pady=(0, 25))
        elif self.returnBookFramePresent == False:
            self.returnBookFrame()
            self.returnBookFramePresent = True
            self.entrReturnBookName = ctk.CTkEntry(
                self.returnBookframe, placeholder_text="Enter Name of Book That You Want To Return", width=500)
            self.entrReturnBookName.pack(pady=(60, 25))
            self.returnBookSub = ctk.CTkButton(
                self.returnBookframe, text="Submit", command=self.returnBookk)
            self.returnBookSub.pack(pady=(0, 25))

    def loadInitialGUI(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.geometry("1280x720+200+50")
        self.wm_iconbitmap("iconLibrary.ico")
        self.title("Library Management")
        self.bind("<Enter>", self.ed)

    def welcome(self):
        self.wlcm = ctk.CTkLabel(
            self, text="Welcome To The Library", font=("mesquito", 60, "bold"))
        self.wlcm.pack(pady=(250, 20))

    def displayFrame(self):
        self.btnFrame = ctk.CTkFrame(self, height=100)
        self.btnFrame.pack(padx=20, pady=20, fill="x",
                           side="bottom", ipadx=20, ipady=20)

    def initialFrame(self):
        self.btnFrame = ctk.CTkFrame(self, height=100)
        self.btnFrame.pack(padx=20, pady=20, fill="x",
                           side="bottom", ipadx=20, ipady=20)

    def ed(self, event):
        if len(self.lendedBooks) > 0:
            self.returnBook.configure(state="normal")
        else:
            self.returnBook.configure(state="disabled")

    def addButton(self):
        self.display = ctk.CTkButton(
            self.btnFrame, text="Display", command=self.displayBooks)
        self.display.pack(side="left", padx=10, pady=20, expand=1)
        self.addBook = ctk.CTkButton(
            self.btnFrame, text="Add Book", command=self.addBooks)
        self.addBook.pack(side="left", padx=10, pady=20, expand=1)
        self.lendBookk = ctk.CTkButton(
            self.btnFrame, text="Lend Book", command=self.lendBook)
        self.lendBookk.pack(side="left", padx=10, pady=20, expand=1)
        self.returnBook = ctk.CTkButton(
            self.btnFrame, text="Return Book", command=self.retrnBook)
        self.returnBook.pack(side="left", padx=10, pady=20, expand=1)


if __name__ == "__main__":
    with open("booksdata.txt") as f:
        books = f.readlines()
    l = Library(books)
    l.welcome()
    l.initialFrame()
    l.addButton()
    l.mainloop()
