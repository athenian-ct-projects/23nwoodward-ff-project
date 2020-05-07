
# This game is for Risky Buisness Day by NW '23
# Make sure to get enough money to stay in business, but enough sugar to keep up tour energy thrughout the day!

cost = float(input("How much are you selling your item/experience for today?"))
money = cost*3
if cost > 0: 
    print("great, let's get started! You start with &" + money + ".")
input1 = int(input("Do you want to (1) help start setting up the business, or (2) scope out other businesses? pick 1 or 2. "))
if input1 == 1:
    money = money + cost 
    input11 = int(input("Congrats, "))
