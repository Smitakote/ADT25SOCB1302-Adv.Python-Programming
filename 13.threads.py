import threading
import time

# Task 1: Print numbers
def print_numbers():
    for i in range(1, 6):
        print("Number:", i)
        time.sleep(1)

# Task 2: Print letters
def print_letters():
    for letter in 'ABCDE':
        print("Letter:", letter)
        time.sleep(1)

# Task 3: Print messages
def print_messages():
    for i in range(1, 6):
        print("Message:", i)
        time.sleep(1)

# Creating multiple threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)
t3 = threading.Thread(target=print_messages)

# Starting threads
t1.start()
t2.start()
t3.start()

# Waiting for all threads to complete
t1.join()
t2.join()
t3.join()

print("All tasks completed.")