import requests
import concurrent.futures
import time

url = "https://jsonplaceholder.typicode.com/posts"

headers = {
}

def make_request():
    response = requests.get(url, headers=headers)
    return response.json()


num_requests = 5

start_time = time.time()


with concurrent.futures.ThreadPoolExecutor() as executor:

    futures = [executor.submit(make_request) for _ in range(num_requests)]


    results = [future.result() for future in concurrent.futures.as_completed(futures)]

end_time = time.time()


print("Results:", results)
print(f"Time taken for {num_requests} parallel requests: {end_time - start_time} seconds")