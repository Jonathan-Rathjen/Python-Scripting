import itertools
import time  

index = list("1234567890qwertyuiopasdfghjklzxcvbnm")
passwd = input("Please input an alpha-numeric password that is six characters or less: ")
found = False

start_time = time.time()  

for i in range(1, 9):
    for j in itertools.product(index, repeat=i):
        guess = ''.join(j)
        print(guess)
        if guess == passwd:
            end_time = time.time()  
            print("Password found:", guess)
            print("Time taken: {:.2f} seconds".format(end_time - start_time))
            found = True
            break
    if found:
        break

if not found:
    end_time = time.time()
    print("Password not found.")
    print("Time taken: {:.2f} seconds".format(end_time - start_time))