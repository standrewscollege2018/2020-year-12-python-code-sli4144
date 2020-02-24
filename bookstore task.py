#list store all the book detail
books= [["In to the wild", "Jon Krakauer", 20.3], ["Castle", "Franz Kafka", 16.5],["The three body problem", "Liu Cixin", 50.25]]

# function 
# a loop go through the list and print out each item
def show_books():
    for book in range(0, len(books)):
        print (book+1, books[book])
#call function
show_books()

# add function
def add():
    # add a new book into the list
    newtitle = input("enter the title of the new book:")
    newauthor = input("enter the author of the new book:")
    newprice = float(input("enter the price of the new book:"))
    new_book = [newtitle, newauthor, newprice]
    books.append (new_book)
    
# delete function
def delete():
    # delete a book 
    book = int(input("enter the number of the book you want to delete:"))
    del books[book-1]

# update function
def update():
    #update a book detail
    update = int(input("enter the number of book you want to update:"))
    updatetitle = input("update the title:")
    updateauther = input("update the auther:")
    updateprice = float(input("update the price:"))
    update_book = [updatetitle, updateauther, updateprice]
    books[update-1] = update_book
#call function
show_books()



#create a list which store all the functions of the program that allows user to chose what they want to do with the books
#[chose+1]
programm_functions = [[1,"add a new book"], [2,"delet a book"], [3,"update a book"], [4,"quit"]]
for i in range (len(programm_functions)):
    print (programm_functions[i])

#ask the user and store as a variable
chose = int(input("enter the number of the funciton you chose"))
choice = chose + 1 
# add a new book
if choice == 1:
    add() 
    
# delet a book
elif choice == 2:
   delete()
# uplate a book
elif choice == 3:
   update()
# ends the program
elif choice == 4:
    ask == False
    print("see u")