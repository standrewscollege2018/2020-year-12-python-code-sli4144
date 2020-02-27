

#list store all the book detail
books= [["In to the wild", "Jon Krakauer", 20.3], ["Castle", "Franz Kafka", 16.5],["The three body problem", "Liu Cixin", 50.25]]

              # function 
# a loop go through the list and print out each item
def show_books():
    for book in range(0, len(books)):
        print (book+1, books[book])


# add function
def add():
    # try and expect error chatching
    # add a new book into the list
    newtitle = input("enter the title of the new book:")
    newauthor = input("enter the author of the new book:")
    # try and expect error chatching
    while True:
        try:    
            newprice = float(input("enter the price of the new book:"))
            break
        except:
            print("please enter a valid number")
    new_book = [newtitle, newauthor, newprice]
    books.append (new_book)
    
       
    
# delete function
def delete():
    # delete a book 
    # try and expect error chatching
    while True:
        try:    
            book = int(input("enter the number of the book you want to delete:"))
            break
        except:
            print("invalid number, try again")
    del books[book-1]
    
      

# update function
def update():
    #update a book detail
    while True:
        try:    
            update = int(input("enter the number of book you want to update:"))
            break
        except:
            print("invaild number")
    updatetitle = input("update the title:")
    updateauther = input("update the auther:")
    while True:
        try:    
            updateprice = float(input("update the price:"))
            break
        except:
            print("invaild number, try again")
    update_book = [updatetitle, updateauther, updateprice]
    books[update-1] = update_book
    
    



#while loop, start running the programming, allow user to quit the programming.
while True:
    
    #create a list which store all the functions of the program that allows user to chose what they want to do with the books
    # call each function in the corresponding list in list, print out the fist item which is the name of the functions, store the input into a variable, when variable equals something
    programm_functions = ["1.add a new book", "2.delete a book", "3.update a book", "4.quit", "5.check the list of book"]
    
    #for i in range (len(programm_functions)):
    for i in range (len(programm_functions)):
        print (programm_functions[i])
    # when is the condition between input is 1 to 5, is true
    cho = 0
    while cho >1 or cho < 6:
        try:    
            #ask the user and store as a variable
            choice = int(input("enter the number of the function you chose:"))
            break
        except ValueError:
            print("chose a vaild number")
      
    
    # add a new book
    if choice == 1:
      add()
        
    # delet a book
    if choice == 2:
       delete()
       
    # uplate a book
    if choice == 3:
      update()
       
    #print out the list of books
    if choice == 5:
        show_books()    
       
    # ends the program
    elif choice == 4:
       print("see u")
       break
        
        
    
        