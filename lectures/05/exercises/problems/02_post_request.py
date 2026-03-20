"""Problem 02: POST request to JSONPlaceholder.

Task:
1. Send POST to https://jsonplaceholder.typicode.com/posts
2. Send JSON payload with fields: title, body, userId
3. Print:
   - status code
   - raw body
   - parsed JSON
4. Confirm response includes your data + id

Note: JSONPlaceholder simulates writes; data is not truly persisted.
"""

import requests

URL = "https://jsonplaceholder.typicode.com/posts"


def main() -> None:
    # TODO: create payload dict
    payload = {"tittle": "fun", "body": "b", "userId": 1}
    # TODO: send POST request with json=payload
    response = requests.post(url=URL, data=payload)
    # TODO: print response details
    print(response.json())
    


if __name__ == "__main__":
    main()
