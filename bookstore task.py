#list store all the book detail
books= [["In to the wild", "Jon Krakauer", 20.3], ["Castle", "Franz Kafka", 16.5],["The three body problem", "Liu Cixin", 50.25]]

# function 
# a loop go through the list and print out each item
def all_books():
    for book in range(0, len(books)):
        print (book+1, books[book])
#call function
all_books()
# add a new book into the list
newtitle = input("enter the title of the new book:")
newauthor = input("enter the author of the new book:")
newprice = float(input("enter the price of the new book:"))
new_book = [newtitle, newauthor, newprice]
books.append (new_book)
#call function
all_books()