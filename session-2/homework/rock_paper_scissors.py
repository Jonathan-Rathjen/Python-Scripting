from getpass import getpass
import time

player1 = getpass('Player One, will you play "rock", "paper", or "scissors": ')

if player1 == "rock" or player1 == "paper" or player1 == "scissors":
    print("Interesting choice!")
else:
    print("That is not a valid play, try again")
    quit()

player2 = getpass('Player Two, will you play "rock", "paper", or "scissors": ')

if player2 == "rock" or player2 == "paper" or player2 == "scissors":
    print("Let's see who won!")
else:
    print("That is not a valid play, try again")
    quit()

time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

if player1 == "paper" and player2 == "rock" or player1 == "scissors" and player2 == "paper" or player1 == "rock" and player2 =="scissors":
    print("Player One is the Winner!!!")
elif player1 == player2:
    print("It's a Tie!!!")
else:
    print("Player Two is the Winner!!!")