# function display all students in the list
def display_all_students():
    for i in range(0, len(names)):
        print(i+1,names[i])    
    




#manaage student info about L1 ncea credits
#store student detail
names = ["Amy","Andy","Ann","Bob","John"]
# another list which store the credits of the corresponding student
credits = [35,89,74,110,29]

#display all the names in the list using a for loop
#for i in range(0, len(names)):
    #print(i+1,names[i])
# call the function
display_all_students()

# function that able to add student into the name list
name = input("add a student:")
names.append (name)
#call function
display_all_students


# function that able to delete student
name = input("enter a index of student to delete")
del (student(name))
# call function
display_all_students()


#change the detail of the student
#get details of which student to change and what the updated name is
name = input("enter the name of the student you want to change:")
new_name = input("enter the new name of the student:")
nane = new_name
# call function
display_all_students()

