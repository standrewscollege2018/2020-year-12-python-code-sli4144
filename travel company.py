#list store the departure location
depart_loc = ["1. Auckland", "2. Wellington","3. Christchurch"]

#list store the destination
destin_loc = ["1.Sydney", "2.Tonga", "3.Shanghai", " 4.London"]

#list store the price of the destination
price = ["1.Sydney - $326", "2.Tonga - $378", "3.Shanghai - $1436", " 4.London - $2376 "]

#list store all the functionality of the programm
program_funct = ["1.departure location", "2.destination", "3. price of the destination", "4.book your flight", "5.exit"]





          # functions 
# funtion that show all the departure location
def show_dep():
    for x in range(len(depart_loc)):
        print (depart_loc[x])

# function that show all the destination 
def show_des():
    for i in range(len(destin_loc)):
        print (destin_loc[i])

# function that show price list
def show_price():
    for p in range(len(price)):
        print(price[p])
        
# book tickets function
def ticket_booking():
    departure = int(input("enter the index of your departure location:"))
    destination = int(input("enter the index of your detination:"))
    nights = int(input("how many nights are you planning to stay?"))
    print("Your flights are departure in", depart_loc[departure+1],", and your destination is", destin_loc[destination+1],"and you booked", nights,"nights.")
    ticket_detail = [departure, destinaiton,nights]
    
    
#cost calculation
def cal_cost():
    











print ("welcome to the programm, what can we help?")
print (program_funct)
do = int(input("enter the number of function helps you:")):
    if do == 
