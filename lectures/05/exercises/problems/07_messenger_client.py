"""Problem 07 (part B): messenger sender client.

Task:
1. Split into pairs
2. Write an infinite loop reading message text from terminal
3. Send each message to partner API endpoint /messages
4. Show send status in terminal


Partner setup:
- Partner gives you ngrok public URL
- You set TARGET_BASE_URL to that URL
"""

import requests

TARGET_BASE_URL = "https://bb9e-91-126-71-186.ngrok-free.app"
SENDER_NAME = "daniel"


def main() -> None:
    # TODO: implement input loop and POST sending
    while True:
        text = input()
        message = {'sender': SENDER_NAME, 'text': text}
        response = requests.post(f"{TARGET_BASE_URL}/messages", json=message)
        print('status ', response.status_code)
        print(response.json())



if __name__ == "__main__":
    main()
