# This game is for Risky Buisness Day by NW '23
# Make sure to get enough money to stay in business, but enough sugar to keep up your energy throughout the day!
money = 0 
#this is a counter for the total amount of money
def sales(): 
    for x in range(4):
        print(x) 
#this is my for loop and function  
cost = float(input("How much are you selling your item/experience for today?"))
money = money + cost*3
#these are my two main variables for the game
if cost > 0: 
    print("great, let's get started! You start with $" + str(money) + ".")
    #the amount of moeny someone starts with, earns, or loses is all based on the cost of their item/experience
input0 = int(input("Do you want to (1) help start setting up the business, or (2) scope out other businesses? pick 1 or 2. "))
if input0 == 1: 
    #all the inputs are labeled witht he numbers of previous descisions made
    money = money + cost 
    input1 = int(input("Congrats, you've made $" + str(cost) + ". Your total money is $" + str(money) + " Pick to either (1) save or (2) spend."))
    if input1 == 1:
        money = money + cost*2
        input11 = int(input("You sold two more, you now have $" + str(money) + ". Pick either (1) save or (2) spend. "))
        if input11 == 1:
            money = money + cost
            input111 = int(input("you made another $" + str(cost) + "dollars. You now have $" + str(money) + "pick either (1) save or (2) spend. "))
            if input111 == 1:
                #first possible game ending (print statements signal finish possibilities)
                print("GAME OVER! you don't have enough sugar to continue. You ended with $" + str(money))
            if input111 == 2: 
                money = money - cost*0.8
                input1112 = int(input("You can now pick between (1) an ice cream sundae or (2) a root beer float both for $" + str(cost*0.8)))
                if input1112 == 1:
                    #second possible game ending 
                    print("oh no, while you went to get ice cream, your partners sold out. YOu no longer have a source of income. GAME OVER.")
                if input1112 == 2: 
                    #third possible game ending 
                    print("You completed risky buisness day!!! You finished with $" + str(money))
        elif input11 == 2: 
            input112 = int(input("You have to pay $" + str(cost*1.5) + " for either a (1) brownie or (2) milkshake. "))
            if input112 >=1:
                money = money - cost*1.5 - cost*2.5 
                #fourth possible game ending
                print(" Sorry, you have to pay taxes now! :( You have to pay $" + str(cost*2.5) + " for taxes. now your total amount of money is now $" +str(cost) + ".")
    elif input1 == 2: 
        money = money - cost*1.2
        inputi = int(input("You bought yourself a nice chocolate chip cookie for $" + str(cost*1.2) + "press 1 to continue"))
        if inputi == 1:
            input12 = int(input("time to pay taxes!!! You have to pay " + str(cost*2) + ". Your total money is now $" + str(money) + ". Would you like to (1) save or (2) spend. "))
            if input12 == 1:
                money = money + cost*2
                input121 = int(input("you sold 2 more items/experiences. Your total money is now $"+ str(money)+ ". Pick to either (1) spend or (2) sell. "))
                if input121 == 1:
                    #fifth possible game ending 
                    print("Ted has specially selected you to become a tax collecter. You no longer get to sell. Game Over")
                if input121 == 2: 
                    #sixth possible game ending 
                    print("Oh no bad weather, you have to end the focus day here. GAME OVER Your total money was $"+ str(money))
            if input12 == 2: 
                #seventh possible game ending 
                print("You payed $" + str(cost*2) + " for an orange soda and now you've run out of money. GAME OVER")
        
elif input0 == 2: 
    input2 = int(input("The buisness next door has ice cream sundaes. Pick to either (1) hold off or (2) buy one. "))
    if input2 == 1:
        money = money - cost*2
        input21 = int(input("You now have to pay $" + str(cost*2) + " for a (1) glass of lemonade  or (2) a cupcake."))
        if input21 == 1:
            #eighth possible game ending 
            print("Oh no! Your friends couldn't manage the business while you were gone and you went bankrupt! GAME OVER")
        if input21 == 2: 
            money = money -cost*2
            #ninth possible game ending 
            print("You now have to pay taxes! You have to pay $" + str(cost*2) + ". After paying you have $" + str(money) + " Game Over")
    if input2 == 2: 
        money = money - cost*1.5 - cost
        #tenth possible game ending 
        print("You bought a ice cream sandwich for $" + str(cost*1.5) + ". You had to pay taxes of $" + str(cost))
        input22 = int(input("Your total amount of money left is now $" + str(money) + ". Would you like to (1) save or (2) spend"))
        if input22 == 1:
            money = money + cost
            input221 = int(input("You sold another item/experience. You now have $" + str(money)+ ". It has started to rain. Do you want to risk it and (1) keep selling or play it safe and (2) go inside."))
            if input221 == 1: 
                money = money + cost*3 
                sales()
                # this is where i call my function, listing the amount of sales made
                input2211 = int(input("The rain subsided and you made three more sales. Do you want to (1) keep the money you have now and finish the game or (2) keep selling on the risk the rain could come back. "))
                if input2211 == 1:
                    #eleventh possible game ending 
                    print("Congratulations you finished the game. You end with $" + str(money) + ".")
                if input2211 == 2: 
                    import random
                    num = random.randint(1,3)
                    x = 0 
                    while x < 2: 
                        x=x+1
                        guess = int(input("Guess a number either 1 or 2. If you get it right, you succeed, if not, you fail. "))
                        if guess == num:
                            money = money + cost*3
                            #12th possible game ending
                            print("Yay, you finished just before the rainstorm and earned $" + str(cost*3) + ". You ended the game with $" + str(money))
                            break
                        if guess != num: 
                            money = money - cost*4
                            #13th possible game ending 
                            print("You got caught in the rainstorm and everything you had for sale was struck by lightening. You lost a bunch of money and ended with $" + str(money))
                            break
                        # this is where my while loop and breaks were used as a guessing risk factor
            if input221 == 2:  
                #14th possible game ending          
                print("The rain subsided but you were stuck inside and couldn't make anymore sales. Your finishing money total is $" + str(money))
        if input22 == 2: 
            #15th possible game ending 
            print("You have no more money. GAME OVER.")



