# function display all students in the list
def display_all_students():
    for i in range(0, len(names)):
        print(i+1,names[i])    
    




#manaage student info about L1 ncea credits
#store student detail names and scores
names = [["Amy",35], ["Andy",89], ["Ann",70], ["Bob",23], ["John",67]]
# another list which store the credits of the corresponding student
#3credits = [35,89,74,110,29]

#display all the names in the list using a for loop
#for i in range(0, len(names)):
    #print(i+1,names[i])
# call the function
display_all_students()

# function that able to add student into the name list
name = input("add a student:")
credit = int(input("what is the number of the credit:"))
new_student = [name,credit]
names.append (new_student)
#call function
display_all_students()


# function that able to delete student
name = int(input("enter the number of the student you want to delete: "))
del names[name-1]
# call function
display_all_students()


#change the detail of the student
#get details of which student to change and what the updated name is
student_number = int(input("enter the number of the student you want to change:"))
new_name = input("enter the new name of the student:")

#change student details
names[student_number - 1] = new_name

# call function
display_all_students()

