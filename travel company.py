#list store the departure location
#list in list , each list store the departure location and extra cost
depart_loc = [["1. Auckland", 0], ["2. Wellington", 50], ["3. Christchurch",75]]

#list store the price of the destination
destin_loc = [["1.Sydney", "Sydney - $326", 326], ["2.Tonga ", "Tonga  - $378", 378], ["3.Shanghai", "Shanghai - $1436", 1436], [" 4.London", "London - $2376 ", 2376]]

#list store all the functionality of the programm
program_funct = ["1.departure location", "2.destination", "3. price of the destination", "4.book your flight", "5.exit"]





          # functions 

#function that show all the functionaility of the programm 
def show_funct():
    for f in range (len(program_funct)):
        print (program_funct[f])    

# funtion that show all the departure location
def show_dep():
    for x in range(len(depart_loc)):
        print (depart_loc[x][0])

# function that show all the destination 
def show_des():
    for i in range(len(destin_loc)):
        print (destin_loc[i][0])

# function that show price list
def show_price():
    for p in range(len(destin_loc)):
        print(price[p][1])
        
# book tickets function
def ticket_booking():
    departure = int(input("enter the index of your departure location:"))
    destination = int(input("enter the index of your detination:"))
    nights = int(input("how many nights are you planning to stay?"))
    print("Your flight is depart in", depart_loc[departure-1][0],", and your destination is", destin_loc[destination-1][0],"and you booked", nights,"nights.")
    depart_loc[departure-1][1] = price_one 
    destin_loc[destinaiton-1][2] = price_two
    
    
#cost calculation
def cal_cost():
    if nights >= 3:
        total_cost = (price_one + price_two)*0.8 *1.15
        print("Your total cost is", total_cost,".")
     else:
        total_cost = (price_one + price_two)* 1.15
        print("Your total cost is", total_cost,".")
    
        
        

# while loop start the progamm
while True:
    print ("welcome to the programm, what can we help?")
    #print all the functionality
    show_funct()
    #user choose the function ,only true when input between 1 to 5
    ask = 0
    while ask > 0, and < 6 :
        try:
            do = int(input("enter the number of function helps you:")):
        if do == 1:
            show_dep()
        
        if do == 2:
            show_des()
            
        if do == 3:
            show_price()
        
        if do == 4:
            ticket_booking()
        
        elif do == 5:
            print("see u")
            break        
            
            
            
