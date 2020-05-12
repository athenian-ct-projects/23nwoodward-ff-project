
# This game is for Risky Buisness Day by NW '23
# Make sure to get enough money to stay in business, but enough sugar to keep up your energy throughout the day!
money = 0 
#this is a counter for the total amount of money. 
cost = float(input("How much are you selling your item/experience for today?"))
money = money + cost*3
if cost > 0: 
    print("great, let's get started! You start with $" + money + ".")
input = int(input("Do you want to (1) help start setting up the business, or (2) scope out other businesses? pick 1 or 2. "))
if input == 1: 
    money = money + cost 
    input1 = int(input("Congrats, you've made $" + cost + ". Your total money is $" + money + " Pick to either (1) save or (2) spend."))
    if input1 == 1:
        money = money + cost*2
        input11 = int(input("You sold two more, you now have $" + money + ". Pick either (1) save or (2) spend. "))
    if input1 == 2: 
        
if input1 == 2: 
    input21 = int(input("The buisness next door has ice cream sundaes. Pick to either (1) save or (2) spend. "))

