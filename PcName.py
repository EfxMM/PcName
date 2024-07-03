import os
import requests

# Discord Webhook URL
webhook_url = ""


computer_name = os.environ['COMPUTERNAME']


payload = {
    "content": f"Computer name: {computer_name}"
}


response = requests.post(webhook_url, json=payload)


if response.status_code == 204:
    print("Computer name sent to Discord successfully!")
else:
    print("Error sending computer name to Discord:", response.text)
