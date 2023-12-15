import requests
import time

url = "https://jsonplaceholder.typicode.com/posts"

headers = {}


num_requests = 5


start_time = time.time()


responses = []
for _ in range(num_requests):
    response = requests.get(url, headers=headers)
    responses.append(response.json())

end_time = time.time()

# Print the results and time taken
print("Results:", responses)
print(f"Time taken for {num_requests} sequential requests: {end_time - start_time} seconds")