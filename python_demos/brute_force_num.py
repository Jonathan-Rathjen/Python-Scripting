passwd = int(input("Please provide a number password to crack: "))
guess = 0
while guess != passwd:
    print(guess)
    guess=(guess + 1)

print("Your password was",guess)