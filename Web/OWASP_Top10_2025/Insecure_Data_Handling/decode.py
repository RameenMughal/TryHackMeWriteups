import base64
import string

cipher = base64.b64decode("BiA8RSIrPhE4JjFULzA1VC9lP145ZS1eJiorQyQyeVA/ZWoRGwh3EQgqN1cuNzxfKCB5QyQqNBEJaw==")

chars = string.ascii_letters + string.digits

for c in chars:
    key = ("KEY" + c).encode()
    plain = bytes(cipher[i] ^ key[i % 4] for i in range(len(cipher)))
    try:
        text = plain.decode()
        if all(32 <= ord(ch) < 127 or ch in "\n\r\t" for ch in text):
            print(key.decode(), "->", text[:80])
    except:
        pass
