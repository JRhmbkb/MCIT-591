#Rui Jiang
#75278441
#I did mostly all the work by myself. But I received some help for debugging from Donald Hughe

# import the random module
# use "winnings = random.randint(2, 10)" to generate a random int from 2 - 10 and store in a variable "winnings"
import random

# unit price of a lottery ticket
constant_lottery_unit_price = 2

# unit price of an apple
constant_apple_unit_price = .99

# unit price of a can of beans
constant_canned_beans_unit_price = 1.58

# unit price of a soda
constant_soda_unit_price = 1.23

# the user has initial $5 for shopping
money = 5

# the user has spent $0 initially
money_spent = 0

# the amounts of lottery tickets, apples, cans of beans, and sodas the user has purchased
numLottery, numApple, numBean, numSoda = 0, 0, 0, 0
winnings= 0;

print ("Welcome to the supermarket!  Here's what we have in stock:\n")
print ("- Lottery tickets cost $2 each")
print ("- Apple cost $0.99 each")
print ("- Cans of beans cost $1.58 each")
print ("- Sodas cost $1.23 each\n")

print ("You have $" + str(money) + " available")
choice = input ("First, do you want to buy a $2 lottery ticket for a chance at winning $2-$10? (y/n) ")

if choice == 'y' or choice =='Y': #let user choose to buy lottery or not
	numLottery = numLottery+1;
	money = money - constant_lottery_unit_price; #substract the payment for lottery
	win_rate = random.randint (0, 2) #generate the chances of 0, 1, 2
	# print (win_rate), just for my own validation purpose
	if win_rate == 2: #randomly set 2 as winning, 33% winning chance
		winnings = random.randint (2, 10) #generate much money it won
		money = money + winnings #add the money won to the total
		print ("Congrats! You won $" + str(winnings))
	else: #anything else, 0 or 1, will be considered as lossing
		print ("Sorry! You did not win the lottery.")
else:
	print("No lottery tickets were purchased!")

#Display the money that user has again! And round it to 2 decimal place
money = round(money, 2)
print("\nYou have $" + str(money) + " available")
#Now lets move on to the apple section
choice = input ("Do you want to buy apple(s)?(y/n) ")

if choice == 'y' or choice == 'Y': #if user chose Y or y
	try:
		numApple = input ("How many apple(s) do you want to buy?\n")
		numApple = int (numApple) #cast into int
		costApple = numApple * constant_apple_unit_price #do the calculation to get total cost of apple if the user decided purchase
		print ("\nThe user wants to buy " + str(numApple) + " apple(s). This will cost $" + str(costApple)) #output
		if costApple <= money:
			money = money - costApple;
			print ("The user has enough money. " + str(numApple) + " apple(s) purchased.")
		else:
			print("Not enough money! No apples purchased.")
			numApple = 0;
	except ValueError:
		print("Invalid input. Input cannot be cast into an integer!")

else:
	print ("No apples were purchased!")

#======================================================
#Display the money that user has again! And round it to 2 decimal place
money = round(money, 2)
print("\nYou have $" + str(money) + " available")
#Now move on to the bean section

choice = input ("Do you want to buy can(s) of beans?(y/n) ")

if choice == 'y' or choice == 'Y': #if user chose Y or y
	try:
		numBean = input ("How many can(s) of beans do you want to buy?\n")
		numBean = int (numBean) #cast into int
		costBean = numBean * constant_canned_beans_unit_price #do the calculation to get total cost of cans of beans if the user decided purchase
		print ("\nThe user wants to buy " + str(numBean) + " can(s) of beans. This will cost $" + str(costBean)) #output
		if costBean <= money:
			money = money - costApple;
			print ("The user has enough money. " + str(numBean) + " can(s) of beans purchased.")
		else:
			print("Not enough money! No cans of beans purchased.")
			numBean = 0;
	except ValueError:
		print("Invalid input. Input cannot be cast into an integer!")

else:
	print ("No cans of beans were purchased!")

#=========================================
#Display the money that user has again! And round it to 2 decimal place 
money = round(money, 2)
print("\nYou have $" + str(money) + " available")
#Now move on to the soda section

choice = input ("Do you want to buy soda(s)?(y/n) ")

if choice == 'y' or choice == 'Y': #if user chose Y or y
	try:
		numSoda = input ("How many soda(s) do you want to buy?\n")
		numSoda = int (numSoda) #cast into int
		costSoda = numSoda * constant_soda_unit_price #do the calculation to get total cost of soda(s) if the user decided purchase
		print ("\nThe user wants to buy " + str(numSoda) + " soda(s). This will cost $" + str(costSoda)) #output
		if costSoda <= money:
			money = money - costSoda;
			print ("The user has enough money. " + str(numSoda) + " soda(s) purchased.")
		else:
			print("Not enough money! No soda(s) purchased.")
			numSoda = 0;
	except ValueError:
		print("Invalid input. Input cannot be cast into an integer!")

else:
	print ("No soda(s) were purchased!")

#=======================
#print out the final invoice
money = round (money, 2);
print("\nMoney left: $" + str(money))
print("Lottery ticket(s) purchased: " + str(numLottery))
print("Lottery winnings: $" + str(winnings)) 
print("Apple(s) purchased: " + str(numApple))
print("Can(s) of beans purchased: " + str(numBean))
print("Soda(s) purchased: " + str(numSoda))
print("Good bye!")




