#Rui Jiang
#75278441
#I did all the work myself. 

from random import randint

def print_instructions():
    '''Prints the rules of the game.
    '''
    print("Let's play pig! Here are the rules:")
    print("-You can the computer will take turns rolling a six-sided die as many times as you want, or unilt you roll a 6")
    print("-Each number you roll, except a 6, will be added to your score for that turm; but if you roll a 6, your score for that turn will be zero. And your turn will be ended.")
    print("-At the end of each turn, the score for that turn is added to your total score. The first player to reach or exceed 50 wins.")
    print("-If you and the cimputer are tied with 50 or more, you'll each get another turn until the tie is broken.")
    print("-The computer will go first! Ready to play? ")

def computer_move(computer_score, human_score):
    '''Has the computer roll some number of times, displays the result of each roll, and
    returns the result (either 0 or the total value of the rolls).
    Uses the given arguments to play more intelligently.
    '''

    # TODO Insert your code here
    roll_computer_total = 0; #counter for total computer score for this around

    if computer_score < human_score: #if the computer is behind the human, then it will take more risk for more reward. Computer will roll 4 times (hopefully not hitting any 6)
        for i in range(0,4):
            roll_computer = roll() #set the random rolled number for a fixed value
            if roll_computer == 6: #if it's 6, then run the special output
                print("The computer rolled a", roll_computer) #print the output
                roll_computer_total = 0; #hitting 6, resulting 0 score for this round
                break
            else:
                print("The computer rolled a", roll_computer)#print the output
                roll_computer_total = roll_computer_total + roll_computer; #adding the total score for this round
    else: #when computer is ahead of the game. Then just roll twice to play safe!
        for i in range(0,2):
            roll_computer = roll()
            if roll_computer == 6:
                print("The computer rolled a", roll_computer, ".")
                roll_computer_total = 0; #hitting 6, resulting 0 score for this round and stop the game immediately
                break
            else:
                print("The computer rolled a", roll_computer,".") #otherwise, show the results and add the rolled number to the total
                roll_computer_total = roll_computer_total + roll_computer;
    
    return roll_computer_total; #return total scores the computer got for this round

def human_move(computer_score, human_score):
    '''Repeatedly asks whether the user wants to roll again and displays the result of each roll.

    - If the user chooses to roll again, and DOES NOT roll a 6, this function adds the roll
    to the total of the rolls made during this move.
    - If the user chooses to roll again, and DOES roll a 6, the function returns 0.
    - If the user chooses not to roll again, the function returns the total of the rolls made during this move.
    '''

    # TODO Insert your code here
    roll_human_total = 0; #initialize the total score for this round to 0

    playerSelection = input("Ready to roll? Enter y/n: ") #get user input 

    while (playerSelection != 'Y' and playerSelection != 'y' and playerSelection !='N' and playerSelection !='n'): #input validation with while-loop
        playerSelection = input ("Invalid selection! Please enter y/n: ") 
        
    if playerSelection == 'y' or playerSelection =='Y':
        human_roll = roll()
        if human_roll == 6: #if it's 6, then the score for that round is 0, and do NOT allow the player to roll again 
                print("You rolled a", human_roll,".")
                roll_human_total = 0
        else:
                print("You rolled a", human_roll,".") #if it's not 6, count the score to total and give the player chance asking if he/she wants to roll again
                roll_human_total = roll_human_total + human_roll;

                while (ask_yes_or_no(input ("Roll again? (y/n): "))):# then ask if human player wants to play more

                    roll_human = roll(); #set the random rolled number for a fixed value
                    if roll_human == 6: #if it's 6, score for the whole game for this round will be set to 0 and stop this round immediately
                        print("You rolled a", roll_human,".")
                        roll_human_total = 0
                        break
     
                    else:
                        print("You rolled a", roll_human,".")#print output
                        roll_human_total = roll_human_total + roll_human; #add the total score for this round


    return roll_human_total; #return the total score for this round


def is_game_over(computer_score, human_score):
    '''Returns True if either player has 50 or more, and the players are not tied,
    otherwise it returns False.
    '''

    # TODO Insert your code here
    if computer_score >=50 or human_score >=50: #game will be over once the score hit or over 50
        
        if computer_score != human_score : #also when it's not a tie, then one party will win. otherwise, keep playing, until they are not having the same score
            return True
        else:
            return False    
    else:
        return False

def roll():
    '''Returns a random number in the range 1 to 6, inclusive.
    '''

    # TODO Insert your code here
    return randint (1, 6) #generate a random int number range from 1 to 6, inclusive.

def ask_yes_or_no(prompt):
    '''Prints the given prompt as a question to the user, for example, "Roll again? (y/n) ".

    - If the user responds with a string whose first character is 'y' or 'Y', returns True.
    - If the user responds with a string whose first character is 'n' or 'N', returns False.
    - Any other response causes the question to be repeated until the user provides an acceptable response.
    '''
    # TODO Insert your code here


    while (prompt != 'Y' and prompt != 'y' and prompt !='N' and prompt !='n'): #input validation with while-loop
        prompt = input ("Invalid selection! Please enter y/n: ")

    if prompt == 'Y' or prompt == 'y': #if it's Y or y, then return true
        return True
    elif prompt == 'N' or prompt == 'n': #if it's N or n, then return false
        return False

def show_current_status(computer_score, human_score):
    '''Tells the user both her current score and the computer's score, and how far
    behind (or ahead) she is, or if there is a tie.
    '''

    # TODO Insert your code here
    if computer_score < human_score: # when human ahead, print the corresponding message
        print("The computer's score is", computer_score, "and your score is", human_score, ". (You are", human_score-computer_score, " points ahead of the computer.)")
    elif computer_score > human_score:# when computer ahead, print the corresponding message
        print("The computer's score is", computer_score, "and your score is", human_score, ". (You are", computer_score - human_score, " points behind the computer.)")
    else: # when it's a tie
        print("The computer's score is", computer_score, "and your score is", human_score, ". (It's a tie!)")

def show_final_results(computer_score, human_score):
    '''Tells the user whether she won or lost, and by how much.
    '''

    # TODO Insert your code here
    if computer_score > human_score: 

        print("You have lost! You are", computer_score - human_score, "points behind.") #if computer score is higher than human score, then computer win and human lost. 

    else:
        print("You have won! You are", human_score - computer_score, "points ahead.") #if human score is more, then human won, computer lost


def startAgain():
    '''Ask player if he/she wants to play again
    '''
    prompt = input("Would you like to play another game? y/n: ")

    while (prompt != 'Y' and prompt != 'y' and prompt !='N' and prompt !='n'): #input validation with while-loop
        prompt = input ("Invalid selection! Please enter y/n: ")
    
    if prompt == 'Y' or prompt == 'y': #if it's Y or y, then return true
        return True
    elif prompt == 'N' or prompt == 'n': #if it's N or n, then return false
        return False


def main():
    print_instructions()
    input('Press any key to start!')
    game_running = True
    while game_running:

        #set initial scores
        human_score = 0
        computer_score = 0

        # TODO Insert the rest of code here

        while is_game_over(computer_score, human_score)==False: #while the game is not over, keep running the functions below
          
            #Computer part:
            computer_score = computer_score + computer_move(computer_score,human_score) #let computer go first
            show_current_status(computer_score, human_score) #then show the current status

            #human part:
            human_score = human_score + human_move(computer_score, human_score) #then human move, and count the total human score
            show_current_status(computer_score, human_score) #then show the current status


        show_final_results(computer_score, human_score) #show final results
        game_running = startAgain() #ask if another game is wanted 

   
if __name__ == '__main__':
    main()
