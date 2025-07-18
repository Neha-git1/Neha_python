import threading
import time

def print_numbers(thread_name):
    for i in range(1, 11):
        print(f"{thread_name} prints: {i}")
        time.sleep(2)

# Create two threads
t1 = threading.Thread(target=print_numbers, args=("Thread-1",))
t2 = threading.Thread(target=print_numbers, args=("Thread-2",))

# Start threads
t1.start()
t2.start()

# Wait for both threads to complete
# t1.join()
# t2.join()

print("Both threads finished.")
