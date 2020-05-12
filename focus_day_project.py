
# This game is for Risky Buisness Day by NW '23
# Make sure to get enough money to stay in business, but enough sugar to keep up your energy throughout the day!
money = 0 
#this is a counter for the total amount of money. 
cost = float(input("How much are you selling your item/experience for today?"))
money = money + cost*3
if cost > 0: 
    print("great, let's get started! You start with $" + str(money) + ".")
input0 = int(input("Do you want to (1) help start setting up the business, or (2) scope out other businesses? pick 1 or 2. "))
if input0 == 1: 
    money = money + cost 
    input1 = int(input("Congrats, you've made $" + str(cost) + ". Your total money is $" + str(money) + " Pick to either (1) save or (2) spend."))
    if input1 == 1:
        money = money + cost*2
        input11 = int(input("You sold two more, you now have $" + str(money) + ". Pick either (1) save or (2) spend. "))
        if input11 == 1:
            money = money + cost
            input111 = int(input("you made another $" + str(cost) + "dollars. You now have $" + str(money) + "pick either (1) save or (2) spend. "))
            if input111 == 1:
                print("GAME OVER! you don't have enough sugar to continue. You ended with $" + str(money))
            if input111 == 2: 
                money = money - cost*0.8
                input1112 = int(input("You can now pick between (1) an ice cream sundae or (2) a root beer float both for $" + str(cost*0.8)))
        elif input11 == 2: 
            input112 = int(input("You have to pay $" + str(cost*1.5) + " for either a (1) brownie or (2) milkshake. "))
            if input112 >=1:
                money = money - cost*1.5 - cost*2.5 
                print(" Sorry, you have to pay taxes now! :( You have to pay $" + str(cost*2.5) + " for taxes. now your total amount of money is now $" +str(cost) + ".")
    elif input1 == 2: 
        money = money - cost*1.2
        inputi = int(input(("You bought yourself a nice chocolate chip cookie for $" + str(cost*1.2) + "press 1 to continue"))
        if inputi == 1:
            input12 = int(input("time to pay taxes!!! You have to pay " + str(cost*2) + "your total money is now $" + str(money) + ". Would you like to (1) save or (2) spend. "))

        
elif input0 == 2: 
    input2 = int(input("The buisness next door has ice cream sundaes. Pick to either (1) hold off or (2) buy one. "))
    if input2 == 1:
        print("hi")
    elif input2 == 2: 
        print("hi")

