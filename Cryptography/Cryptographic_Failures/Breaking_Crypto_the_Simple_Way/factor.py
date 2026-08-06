from Crypto.Util.number import inverse, long_to_bytes

# Given RSA parameters
p = 205237461320000835821812139013267110933
q = 214102333408513040694153189550512987959
e = 65537

# Ciphertext
c = 9002431156311360251224219512084136121048022631163334079215596223698721862766

# Compute modulus
n = p * q

# Compute Euler's Totient
phi_n = (p - 1) * (q - 1)

# Compute private key
d = inverse(e, phi_n)

# Decrypt ciphertext
plaintext = pow(c, d, n)

# Convert integer to bytes
flag = long_to_bytes(plaintext)

# Print results
print("=" * 50)
print(f"n       = {n}")
print(f"phi(n)  = {phi_n}")
print(f"d       = {d}")
print("=" * 50)

try:
    print("Decoded Message:", flag.decode())
except UnicodeDecodeError:
    print("Message is not valid UTF-8.")

print("Raw Bytes:", flag)
print("Plaintext Integer:", plaintext)