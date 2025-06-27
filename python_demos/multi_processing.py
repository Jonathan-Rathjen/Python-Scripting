import itertools
import time
from multiprocessing import Pool, cpu_count

index = list("1234567890qwertyuiopasdfghjklzxcvbnm")
passwd = input("Enter an alphanumeric password (6 characters max): ")

def check_password(guess):
    return guess if guess == passwd else None

def guess_generator(length):
    for tup in itertools.product(index, repeat=length):
        yield ''.join(tup)

def run_brute_force(length):
    with Pool(cpu_count()) as pool:
        for result in pool.imap_unordered(check_password, guess_generator(length), chunksize=1000):
            if result:
                pool.terminate()
                return result
    return None

# Start brute force
if __name__ == '__main__':
    start_time = time.time()

    for length in range(1, 7):
        print(f"Trying passwords of length {length}...")
        result = run_brute_force(length)
        if result:
            elapsed = time.time() - start_time
            print(f"Password found: {result}")
            print(f"Time taken: {elapsed:.2f} seconds")
            break
    else:
        elapsed = time.time() - start_time
        print("Password not found.")
        print(f"Time taken: {elapsed:.2f} seconds")
