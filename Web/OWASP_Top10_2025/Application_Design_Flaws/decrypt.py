from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Values from decrypt.js
key = b"my-secret-key-16"
ciphertext = (
    "Nzd42HZGgUIUlpILZRv0jeIXp1WtCErwR+j/w/lnKbmug31opX0BWy+pwK92rkhj"
    "wdf94mgHfLtF26X6B3pe2fhHXzIGnnvVruH7683KwvzZ6+QKybFWaedAEtknYkhe"
)

# Decode Base64
encrypted = b64decode(ciphertext)

# AES-128 ECB
cipher = AES.new(key, AES.MODE_ECB)

# Decrypt
plaintext = cipher.decrypt(encrypted)

# Remove PKCS#7 padding if present
try:
    plaintext = unpad(plaintext, AES.block_size)
except ValueError:
    pass

print("Decrypted data:")
print(plaintext.decode(errors="ignore"))
