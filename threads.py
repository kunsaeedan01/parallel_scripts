import threading
import time

def compute_square(number):
    result = number * number
    print(f"Thread {threading.current_thread().name}: {number}^2 = {result}")

def threaded_computation(numbers):
    threads = []

    for num in numbers:
        thread = threading.Thread(target=compute_square, args=(num,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_time = time.time()

    numbers_to_square = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Perform parallel computation using threads
    threaded_computation(numbers_to_square)

    end_time = time.time()
