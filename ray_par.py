import ray
import time

ray.init()

@ray.remote
def compute_square(number):
    result = number * number
    print(f"Task {ray.worker.global_worker.worker_id}: {number}^2 = {result}")
    return result

def parallel_computation(numbers):

    square_results = ray.get([compute_square.remote(num) for num in numbers])


    return square_results

if __name__ == "__main__":
    start_time = time.time()

    numbers_to_square = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result_list = parallel_computation(numbers_to_square)

    end_time = time.time()
    print(f"Total time taken with Ray: {end_time - start_time} seconds")

