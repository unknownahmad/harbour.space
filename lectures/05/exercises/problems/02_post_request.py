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
    # TODO: send POST request with json=payload
    # TODO: print response details
    payload={
        "title": "My First Post",
        "body": "This is a test payload for Harbour.Space.",
        "userId": 1
    }
    response=requests.post(URL,json=payload)
    response.raise_for_status()
    print(response.status_code)
    print(response.text)
    print(response.json())
    


if __name__ == "__main__":
    main()
