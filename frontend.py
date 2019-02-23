
from tkinter import *
from backend import Database

db = Database("books.db") # create an object

class Window(object) :

    def __init__(self, window):

        self.window = window

        self.window.wm_title("Bookstore")


        l1 = Label(window, text = "Title")
        l1.grid(row = 0, column = 0)

        l2 = Label(window, text = "Author")
        l2.grid(row = 0, column = 2)

        l3 = Label(window, text = "Year")
        l3.grid(row = 1, column = 0)

        l4 = Label(window, text = "ISBN")
        l4.grid(row = 1, column = 2)

        self.title_text = StringVar()
        self.e1 = Entry(window, textvariable = self.title_text )
        self.e1.grid(row = 0, column = 1)

        self.author_text = StringVar()
        self.e2 = Entry(window, textvariable = self.author_text )
        self.e2.grid(row = 0, column = 3)

        self.year_text = StringVar()
        self.e3 = Entry(window, textvariable = self.year_text )
        self.e3.grid(row = 1, column = 1)

        self.isbn_text = StringVar()
        self.e4 = Entry(window, textvariable = self.isbn_text )
        self.e4.grid(row = 1, column = 3)

        self.list1 = Listbox(window, height = 6, width = 35)
        self.list1.grid(row=2, column=0, rowspan= 6, columnspan = 2)
        # rowspan and columnspan lets us expand the listbox

        scrollbar1 = Scrollbar(window)
        # to scroll the list in the list box
        scrollbar1.grid(row=2,column = 2, rowspan = 6)
        # create a scroll scrollbar

        # tell the list about the scroll bar
        # the magic method is the configure() method
        self.list1.configure(yscrollcommand = scrollbar1.set)

        # tell the scrollbar about the list too
        scrollbar1.configure(command = self.list1.yview)

        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)
        #binding method to listbox widget
        # two argument : event type and function you want to bind it
        # get_selected_row returns the selected row from the list box

        b1 = Button(window, text = "View all",
                    width = 12, command = self.view_command)
        b1.grid(row = 2, column = 3)

        b2 = Button(window, text = "Search Entry",
                        width = 12, command= self.search_command)
        b2.grid(row = 3, column = 3)

        b3 = Button(window, text = "Add Entry",
                        width = 12, command = self.add_command)
        b3.grid(row = 4, column = 3)

        b4 = Button(window, text = "Update Selected"
                    , width = 12, command = self.update_command)
        b4.grid(row = 5, column = 3)

        b5 = Button(window, text = "Delete Selected",
            width = 12, command = self.delete_command)
        b5.grid(row = 6, column = 3)

        b6 = Button(window, text = "Close", width = 12, command = window.destroy)
        b6.grid(row = 7, column = 3)

    def view_command():
        self.list1.delete(0,END) # delete the list box from start to end
        for row in db.view():
            # view function in db return list of all tupules in the table
            self.list1.insert(END,row) # put new row at the end of listbox

    def search_command():
        self.list1.delete(0,END)
        for row in db.search(self.title_text.get(),self.author_text.get(),
                                    self.year_text.get(),self.isbn_text.get()):
            self.list1.insert(END,row)

    def add_command():
        db.insert(self.title_text.get(),self.author_text.get(),
                        self.year_text.get(),self.isbn_text.get())
        self.list1.delete(0,END)
        self.list1.insert(END,(self.title_text.get(),self.author_text.get()
                            ,self.year_text.get(),self.isbn_text.get()))

    def get_selected_row(event):
        try:
            # event parameter holds information about parameter i.e. event
            global selected_tupule
            index =self.list1.curselection()[0]
            self.selected_tupule = self.list1.get(index)

            self.e1.delete(0,END)
            self.e1.insert(END, self.selected_tupule[1]) # id has index 0, title has index 1
            # e1 is for title so index 1 of selected_tupule

            self.e2.delete(0,END)
            self.e2.insert(END,self.selected_tupule[2]) #author

            self.e3.delete(0,END)
            self.e3.insert(END,self.selected_tupule[3]) #Year

            self.e4.delete(0,END)
            self.e4.insert(END, self.selected_tupule[4]) #isbn

        except IndexError:
            pass

    def delete_command():
        try:
            db.delete(self.selected_tupule[0])
            view_command()
        except NameError:
            pass

    def update_command():
        db.update(self.selected_tupule[0],self.title_text.get(),self.author_text.get()
                            ,self.year_text.get(),self.isbn_text.get())
        # selected_tupule[0] represents id, which we are not changing
        # we obtains the input from the text field using the variables we have
        # used to represent these text fields such as title_text
        print(self.selected_tupule[0],self.title_text.get(),self.author_text.get()
                            ,self.year_text.get(),self.isbn_text.get())

window = Tk()
Window(window)
window.mainloop()
