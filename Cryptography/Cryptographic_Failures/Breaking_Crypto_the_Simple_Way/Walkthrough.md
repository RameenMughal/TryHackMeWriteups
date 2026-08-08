# Breaking Crypto the Simple Way

Room: [Breaking Crypto the Simple Way](https://tryhackme.com/room/breakingcryptothesimpleway)

Prerequisites:
1. [Cryptography Module](https://tryhackme.com/module/cryptography)
2. [Cryptography-101 Module](https://tryhackme.com/module/cryptography-101)

<img width="945" height="202" alt="image" src="https://github.com/user-attachments/assets/761da9ec-67cb-4e26-9851-b836e61dd990" />

## Introduction

Cryptography is designed to protect sensitive data, but it's only effective when implemented correctly. Even small mistakes in how cryptographic systems are set up can open the door for attackers. These mistakes are surprisingly common and often become "quick wins" during penetration testing or real-world attacks.

For example, using a weak encryption key or a predictable random number generator can make encryption easier to break. Similarly, exposing secrets like API keys in client-side code gives attackers everything they need to bypass cryptographic protections.

---

### Prerequisites

Before starting this room, you should have a basic understanding of the following concepts:
1. How cryptographic concepts like encryption, decryption, and hashing work.
2. Tools like Hashcat or John the Ripper are used to crack passwords and keys.
3. HTTP request and response basics, along with some experience using the command line.
4. Completion of [Cryptography](https://tryhackme.com/module/cryptography) and [Cryptography-101](https://tryhackme.com/module/cryptography-101) modules.

---

### Starting the Machine

Deploy the target VM attached to this task by pressing the green Start Lab Machine button. After obtaining the machine's generated IP address, you can either use the AttackBox or your own VM connected to TryHackMe's VPN.

I am using my Kali Linux Machine, so we will connect to the TryHackMe through OpenVPN by command: `sudo openvpn FILENAME`

You can check the room [OpenVPN](https://tryhackme.com/room/openvpn) to know how to connect through this.

To add the hostname `bcts.thm`, first open the file by `sudo nano /etc/hosts`

Copy paste the hostname and IP address like this `10.49.129.162 bcts.thm`

<img width="281" height="80" alt="image" src="https://github.com/user-attachments/assets/e29c2789-205e-4aa6-b16d-8661605e8116" />

Save the file and then access the website `http://bcts.thm/`

<img width="611" height="182" alt="image" src="https://github.com/user-attachments/assets/b8a7514a-3822-4ee2-83b7-bfe405e1de5e" />

## Brute-forcing Keys

Cryptography relies on the premise that keys used in encryption are computationally infeasible to guess. A "strong" key is one that provides a high level of entropy (unpredictability) and sufficient length to make brute-force attacks impractical. For example, a 128-bit key has 2^128 possible combinations, which would take centuries to brute-force using modern hardware.

---

### Characteristics of Strong Keys:

- **Length**: Longer keys significantly increase the computational effort required to brute-force them.
- **Entropy**: Keys must be truly random, not derived from predictable inputs like timestamps or user data.
- **Uniqueness**: Keys must be unique across different encryptions or systems to prevent correlation attacks.

A correlation attack is an attack where someone compares encrypted data from different messages or systems to find patterns and learn information. The same encryption key should not be reused in different places, because an attacker might compare the ciphertexts and discover relationships between the plaintexts.

When these principles are violated, keys become vulnerable to brute-force or mathematical attacks.

---

### Math of RSA

RSA encryption, named after its inventors Rivest, Shamir, and Adleman, is based on the difficulty of factoring large numbers.

A public key consists of:
- `n = p×q`: The product of two large prime numbers, (`p`) and (`q`).
- `e`: A small public exponent (commonly (`e = 65537`)).

The private key is derived from:
- `ϕ(n) = (p−1) × (q−1)`, where `ϕ` is Euler's totient function.
- `d`: The modular inverse of `e`, `e modulo 𝜙 ( 𝑛 ) ϕ(n)`, satisfying `𝑒 × 𝑑 ≡ 1 ( mod 𝜙 ( 𝑛 ) ) e × d ≡ 1 (mod ϕ(n))`.

The statement is: `e × d ≡ 1 (modϕ(n))`

This means: When you multiply `e` and `d`, and divide the result by `φ(n)`, the remainder must be 1.

So, `d` is the modular inverse of `e`.

**What does modulo mean?**: Suppose `ϕ(n) = 20` and `e = 3`

We need to find a number d such that `3 × d ≡ 1 (mod20)`

This means: Find a number `d` so that multiplying it by 3 leaves a remainder of 1 when divided by 20.

Let's try values.

3 × 1 = 3     → remainder 3
3 × 2 = 6     → remainder 6
3 × 3 = 9     → remainder 9
3 × 4 = 12    → remainder 12
3 × 5 = 15    → remainder 15
3 × 6 = 18    → remainder 18
3 × 7 = 21    → remainder 1 ✅

Because `21 ÷ 20 = 1` remainder 1

So, `d = 7`

Confirming: `3 × 7 = 21` and `21 mod 20 = 1`

So, `3 × 7 ≡ 1 (mod20)`

Therefore, `e = 3`, `d = 7`

Here, 7 is the modular inverse of 3 modulo 20.

The value `d` is chosen so that it undoes what `e` does.

Encryption: Message -> Use e -> Ciphertext -> Use d -> Original Message

The security of RSA depends on the difficulty of factoring (n) into its prime components (p) and (q). However, if (p) or (q) is poorly generated or shared across keys, this foundational assumption breaks down.

---

### How Factorisation Time Increases Exponentially

As prime numbers grow larger, factorisation time increases exponentially, making brute-force factorisation infeasible for properly generated RSA keys.

---

### What is "P's and Q's"?

The paper [Minding your p’s and q’s](https://www.cl.cam.ac.uk/archive/rja14/Papers/psandqs.pdf)  "P's and Q's" by Ross Anderson and Serge Vaudenay explores how poor randomness in RSA key generation can lead to severe vulnerabilities. It outlines key weaknesses that attackers can exploit:

**Predictable Primes**: If `p` or `q` are generated using a weak random number generator (e.g., seeded with system time), an attacker can recreate the key generation process and derive the primes.

**Shared Primes Across Keys**: When multiple RSA keys share a common prime `p`, the attacker can use the greatest common divisor (GCD) method to factor `n1 ​= p × q1​` and `n2 ​= p × q2​`, breaking both keys.

Suppose, by accident, both users use the same prime `p = 11`.

```
Key 1:
p = 11
q₁ = 13

n₁ = 11 × 13 = 143
```

```
Key 2:
p = 11
q₂ = 17

n₂ = 11 × 17 = 187
```

The attacker only sees the public keys: `n₁ = 143` and `n₂ = 187`

They don't know `p`, `q₁`, or `q₂`.

The attacker calculates: `GCD(143, 187)`

Let's factor them `143 = 11 × 13` and `187 = 11 × 17`

The greatest common divisor is `GCD(143, 187) = 11`

The attacker has now discovered the shared prime!

Once the attacker knows `p = 11`, they can easily find the other primes.

For Key 1: `q₁ = 143 ÷ 11 = 13`

For Key 2: `q₂ = 187 ÷ 11 = 17`

Now the attacker knows:

```
Key 1:
p = 11
q₁ = 13
```
```
Key 2:
p = 11
q₂ = 17
```

Since RSA security depends on keeping p and q secret, both keys are now broken.

**Small Differences Between Primes**: If `p` and `q` are too close in value, efficient algorithms such as [Fermat's factorisation](https://en.wikipedia.org/wiki/Fermat%27s_factorization_method) method can quickly factor `n`.

Suppose `p = 97` and `q = 101`

Notice: `101 - 97 = 4`

They are very close.

Now, `n = 97 × 101 = 9797`

An attacker sees only `n = 9797`

Because 97 and 101 are close together, Fermat's Factorization can quickly discover: `9797 = 97 × 101`

Once the attacker knows `p` and `q`, they can calculate the private key and decrypt messages.

Fermat's idea is: Instead of guessing factors directly, it tries to write n as the difference of two squares: `n = a² − b²`

which can be rewritten as: `n = (a+b)(a−b)`

If `p` and `q` are close together, then:
- `a` is found very quickly.
- `b` is very small.
- So factoring `n` becomes easy.

For the example above find the smallest integer a such that `a² ≥ n`

The square root of `9797` is about: `√9797 ≈ 98.98`

So we start with: `a = 99` because `99² = 9801`

Compute `b² = a² − n`

```
b² = 99² - 9797
    = 9801 - 9797
    = 4
```

Now check if 4 is a perfect square. `√4 = 2` Yes!

So, `b = 2`

Fermat's formula says `n = (a+b)(a−b)`

Substitute the values:

```
a = 99
b = 2
p = a - b = 99 - 2 = 97
q = a + b = 99 + 2 = 101
9797 = 97 × 101
```

The attacker has successfully factored `n`.

**Mathematical Exploits Using GCD**:
The GCD of two public keys that share a prime can be computed in polynomial time: `GCD(n1​,n2​) = p`

Polynomial time means that the time an algorithm takes to finish grows reasonably as the input size grows. In computer science, these algorithms are considered efficient.

Suppose: 

```
n₁ = 143 = 11 × 13
n₂ = 187 = 11 × 17
```

The attacker computes: `GCD(143, 187)`

The Euclidean Algorithm (used to compute GCD) is a polynomial-time algorithm.

Let's see it:

```
187 ÷ 143 = 1 remainder 44
143 ÷ 44 = 3 remainder 11
44 ÷ 11 = 4 remainder 0
```

When the remainder becomes 0, the last non-zero remainder is the GCD.

`GCD(143,187) = 11`

This calculation takes only a few steps, even for very large numbers (2048-bit RSA keys).

These vulnerabilities highlight the critical importance of randomness and diversity in prime generation for RSA security.

---

### Exercise

Using the `c`, `n`, and `e`, which are crucial components of the RSA encryption process. The RSA algorithm also utilises two large prime numbers, `p` and `q`. Can you uncover the hidden text behind it? Follow along to build a script that will uncover the hidden text.

```
Public Key: n = 43941819371451617899582143885098799360907134939870946637129466519309346255747  
Exponent: e = 65537  
Ciphertext: c = 9002431156311360251224219512084136121048022631163334079215596223698721862766
```

Your task is to recover the plaintext by factoring `n` and deriving the private key. The challenge assumes `n` is a product of two weakly generated primes `p` and `q`.

#### Factoring

Since `n` is the product of two large primes (`p` and `q`), factorisation is the first step. Modern factoring tools, like [MSIEVE](https://github.com/radii/msieve) or [YAFU](https://github.com/bbuhrow/yafu), can be used for this purpose. However, for educational purposes, you can use Python and a library like `sympy`.

A Python library `sympy` for symbolic mathematics. It can perform algebra, number theory, prime testing, factorization, GCD, modular inverses, and much more.

Use the following Python code I saved as `factor.py` to find the final flag.

The script will compute:

```
p = 205237461320000835821812139013267110933
q = 214102333408513040694153189550512987959
```

Alternatively, you can use [FactorDB](https://factordb.com/) and search for the prime numbers of the `n`. For example:

<img width="959" height="261" alt="image" src="https://github.com/user-attachments/assets/ea6e86ba-c4ff-4b59-b462-895d44d00890" />

#### Compute phi

Using the two primes, calculate phi(n), where:

```
phi_n = (p - 1) * (q - 1)
print("Phi(n) =", phi_n)
```

#### Finding the Private Key

The private key exponent (d) is the modular inverse of (e) modulo (ϕ(n)):

Use Python to calculate (d):

```
from sympy import factorint
from Crypto.Util.number import inverse, long_to_bytes

e = 65537
d = inverse(e, phi_n)
print("Private key (d):", d)
```

#### Decrypting the Ciphertext

Now that you have (d), decrypt the given ciphertext (c):

Use Python to compute the plaintext:

```
c = 9002431156311360251224219512084136121048022631163334079215596223698721862766

plaintext = pow(c, d, n)
flag = long_to_bytes(plaintext)
print(flag.decode())
print("Decrypted Plaintext:", flag)
```

---

### Key Takeaways from Broadcast RSA
- Avoid small public exponents like `e = 3`; instead, use larger values like `e = 65537`.
- Ensure encrypted messages are padded with random data (e.g., PKCS#1 or OAEP) to prevent mathematical attacks.
- Use different plaintexts for different recipients to avoid the conditions that make CRT attacks possible.

---

### Answer the questions below

What is the flag?

<img width="870" height="208" alt="image" src="https://github.com/user-attachments/assets/68259bc4-2ffc-434a-b92c-b4eb0ac68d05" />

## Breaking Hashes

Hashing is a cryptographic process that transforms an input (e.g., a password or a message) into a fixed-size string, often called a hash. The transformation is one-way, meaning it’s not feasible to reverse the hash to recover the original input. Hashing is used for:
- **Password Storage**: Instead of storing plaintext passwords, systems store their hashes. During login, the input password is hashed and compared to the stored hash.
- **Data Integrity**: Hashes verify that data has not been altered during transmission.
- **Message Authentication (HMAC)**: Hashes combined with a secret key verify that a message hasn’t been tampered with.

HMAC (Hash-based Message Authentication Code) combines a secret key with a hash function to verify that a message has not been altered and comes from someone who knows the secret key. If the message is modified, the HMAC value changes, allowing the receiver to detect tampering. It provides integrity and authentication, but does not encrypt the message.

---

### Common Vulnerabilities in Hashing

**Weak Hash Algorithms**: Older algorithms like MD5 and SHA-1 are considered insecure due to their susceptibility to collisions (two inputs producing the same hash). Attackers can exploit these collisions to make malicious data appear legitimate.

**Lack of Salting**: When the same input consistently produces the same hash, attackers can use precomputed databases (rainbow tables) to reverse the hash to its original value. Salting—adding a unique, random value to each input before hashing—prevents this.

**Insecure HMACs**: Hash-based Message Authentication Codes (HMACs) rely on a hash function combined with a secret key to ensure message authenticity. Weaknesses arise when:
- The hash function is insecure.
- The key is short, predictable, or reused.

---

### SHA-256 Isn’t Ideal for Password Hashing

SHA-256 is a fast and efficient hash function used for data integrity and digital signatures, but it is not suitable for password hashing because attackers can test billions of hashes per second using modern GPUs. Instead, password hashing schemes like Argon2, bcrypt, and PBKDF2 are designed to be slow and computationally expensive, making brute-force attacks much harder. They also allow developers to increase the cost factor over time as hardware becomes more powerful.

The cost factor (also called the work factor) controls how much time and computing power is needed to hash a password.
- A low cost factor → hashing is faster, but attackers can try more password guesses per second.
- A high cost factor → hashing is slower, making brute-force attacks much harder.

To put this into perspective, here’s a rough comparison of how many hashes per second different algorithms can process using GPU acceleration:

<img width="897" height="251" alt="image" src="https://github.com/user-attachments/assets/1b99b585-87f6-4594-9307-c032b7ca7c09" />

If an attacker is trying to brute-force a password, SHA-256 allows them to test billions of possibilities per second, while bcrypt and Argon2 intentionally slow them down to just a few thousand or even hundreds per second. This makes an enormous difference in security.

While SHA-256 can be used for password hashing if you add a salt and manually iterate the hashing process many times, this is still a weaker approach than using a proper password hashing function. Argon2, bcrypt, and PBKDF2 include built-in protections against brute-force attacks, making them far better suited for storing passwords securely.

---

### Choosing the Right Hashing Function

To clarify when to use different hash functions, here’s a comparison:

<img width="902" height="205" alt="image" src="https://github.com/user-attachments/assets/50f2c83e-7c86-44c1-942f-3dd249808dbb" />

Data Integrity checks whether data has changed and uses only a hash function. Anyone can calculate the hash.

While, Message Authentication checks whether data has changed and verifies who sent it and Uses a hash function plus a secret key. Only someone with the secret key can generate the correct HMAC.

Many developers assume that hashing alone is enough to secure passwords, but the reality is that the right tool needs to be used for the right job. Using SHA-256 to hash passwords is like using a padlock on a bank vault—it provides some protection, but it’s not nearly strong enough to stop a determined attacker.

---

### Challenge

HMAC (Hash-based Message Authentication Code) is a cryptographic method used to verify the integrity and authenticity of a message. It combines a cryptographic hash function (in this case, SHA-1) with a secret key. If an attacker can determine the secret key, they can forge valid HMACs and manipulate messages.

In this challenge, you are given a message along with its HMAC-SHA1 digest. However, the secret key used for signing is weak. Your objective is to recover the key.

A digest is simply the output (result) of a hash function. It is also called a hash value or hash.

Below is the message and the SHA1 digest of that message.

```
Message: CanYouGuessMySecret
SHA1-Digest: 1484c3a5d65a55d70984b4d10b1884bda8876c1d
```

---

### Solution

Hashcat is a powerful tool for cracking hashes and HMAC keys. Since we know the format is HMAC-SHA1 , we will use mode 150 . Mode 150 targets HMAC-SHA1 based on this [documentation](https://hashcat.net/wiki/doku.php?id=example_hashes).

Save the hash and message into a file: `echo -n "1484c3a5d65a55d70984b4d10b1884bda8876c1d:CanYouGuessMySecret" > digest.txt`

Run Hashcat with the RockYou wordlist: `hashcat -a 0 -m 150 digest.txt /usr/share/wordlists/rockyou.txt`

Below is the expected output:

```
hashcat (v7.1.2) starting

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
====================================================================================================================================================
* Device #01: cpu-haswell-AMD Ryzen 5 7430U with Radeon Graphics, 1456/2912 MB (512 MB allocatable), 4MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256
Minimum salt length supported by kernel: 0
Maximum salt length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory allocated for this attack: 513 MB (2204 MB free)

Dictionary cache built:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 1 sec

1484c3a5d65a55d70984b4d10b1884bda8876c1d:CanYouGuessMySecret:XXXXXXXX
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 150 (HMAC-SHA1 (key = $pass))
Hash.Target......: 1484c3a5d65a55d70984b4d10b1884bda8876c1d:CanYouGues...Secret
Time.Started.....: Fri Aug  7 12:48:55 2026 (1 sec)
Time.Estimated...: Fri Aug  7 12:48:56 2026 (0 secs)
Kernel.Feature...: Pure Kernel (password length 0-256 bytes)
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#01........:    81466 H/s (0.47ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 4096/14344385 (0.03%)
Rejected.........: 0/4096 (0.00%)
Restore.Point....: 0/14344385 (0.00%)
Restore.Sub.#01..: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#01...: 123456 -> oooooo
Hardware.Mon.#01.: Util: 22%

Started: Fri Aug  7 12:48:25 2026
Stopped: Fri Aug  7 12:48:57 2026
```

---

### Answer the questions below

What is the secret used to encrypt the message?

<img width="828" height="382" alt="image" src="https://github.com/user-attachments/assets/28f80f0b-6109-42fc-bd8a-ac88b2d10123" />

## Exposing Keys

### Risks of Exposing Cryptographic Keys in Client-Side Code

Exposing cryptographic keys in client-side code is a common yet critical mistake. When keys are included in code that runs in the user's browser (e.g., JavaScript), anyone with access to the application can retrieve and misuse those keys. This defeats the purpose of encryption and authentication, as the attacker gains direct access to the mechanism meant to protect the data.

Key risks include:
- **Unauthorised Access**: Exposed keys can be used to decrypt sensitive data or interact with backend APIs as an authenticated user.
- **Data Tampering**: An attacker can use the keys to generate signed payloads or modify encrypted messages, bypassing integrity checks.
- **API Abuse**: Hardcoded API keys may allow attackers to access privileged API endpoints without authorisation.

---

### Common Scenarios of Key Exposure

- **Hardcoded API Keys in JavaScript**: Developers often embed API keys in front-end code for convenience, forgetting that anyone can view this code using browser developer tools.
- **Encryption Keys in Client-Side Frameworks**: Encryption keys are sometimes included in front-end libraries or scripts to encrypt/decrypt data locally. These keys can be easily extracted and used maliciously.
- **Unsecured Configuration Files**: Configuration files embedded in web applications may contain sensitive credentials or keys in plain text.

---

### Exercise

Navigate to `http://bcts.thm/labs/lab3`.

<img width="447" height="131" alt="image" src="https://github.com/user-attachments/assets/ceba2b09-ecf1-45ba-85d8-3c84d06e9239" />

Open your developer tools (F12) or right click to choose Inspect (Q), navigate to the network tab, and try submitting a message.

<img width="858" height="229" alt="image" src="https://github.com/user-attachments/assets/4f0e6065-15ea-4854-a967-5d8ad108e8e1" />

As you can see in the image above, the submitted data is encrypted using the data parameter as shown in the request.

Checking the source code of the web page will show that the application uses JavaScript to encrypt the submitted message before submitting it to `process.php`.

<img width="1778" height="1584" alt="image" src="https://github.com/user-attachments/assets/888068bd-0a8c-48f6-8144-f587a88b04cd" />

Takes the message you type, locks/encrypts it using AES with a fixed secret key, adds a random value (IV) to make the encryption safer, converts the encrypted message into Base64, and sends both the encrypted message and IV to process.php for processing.

Since the encryption key used to encrypt the message is hardcoded in the JavaScript code, it is possible for an attacker to create a script that will brute force for the correct message using the hardcoded encryptionKey value.

To simplify this, a wordlist containing the possible message is available on the server at `http://bcts.thm/labs/lab3/wordlist.txt`.

However, directly brute-forcing the application will not work since the request is encrypted, so we must automate this using Python.

Below is the sample Python script named as `brute_keys.py` that uses the available wordlist.txt in the server.

**Note**: If you're using your own machine, you must install `pycryptodome` using pip for the script to work.

**Explanation of script** 

`encrypt_message(message, iv)`:
- Encrypts a given message using AES-CBC mode.
- Pads the message to ensure its length is a multiple of the AES block size (16 bytes).
- Encrypts the padded message using AES with the provided IV.
- Converts the ciphertext and IV to Base64 format before returning.

`send_payload(ciphertext, iv)`:
- Sends the encrypted message and IV as a JSON payload to the target server.
- Returns the server's response.

`bruteforce()`:
- Reads the wordlist from wordlist.txt.
- Iterates over each word in the list:
- Generates a random IV (16 bytes).
- Encrypts the word using AES-CBC.
- Sends the encrypted message to the server.
- Check if the response contains "Access granted!" (indicating success).

Once the script successfully brute forces the correct message, the application will return the flag.

First download the `wordlist.txt` from this command: `wget http://bcts.thm/labs/lab3/wordlist.txt`

<img width="823" height="121" alt="image" src="https://github.com/user-attachments/assets/d5c2ce1a-12fe-40aa-bd47-12a0e8fa8635" />

Then run the script: `python3 brute_key.py`

<img width="293" height="230" alt="image" src="https://github.com/user-attachments/assets/272aa9b1-a9cf-4179-b0f8-0baf15c55e00" />

---

### Key Takeaways

- **Never Hardcode Keys**: Avoid embedding sensitive keys in client-side code or configuration files that are accessible to users.
- **Use Secure Key Management**: Store keys in secure environments, such as server-side applications or dedicated key management services (e.g., AWS KMS, Azure Key Vault).
- **Implement Backend Encryption**: Perform sensitive operations, like encryption and decryption, on the server side to prevent exposure of critical secrets.
- **Educate Developers**: Many developers make this mistake unknowingly. Awareness and secure coding practices can prevent these vulnerabilities.

---

### Answer the questions below

What is the flag?

<img width="798" height="201" alt="image" src="https://github.com/user-attachments/assets/9b9ddb94-119f-46e1-bc4c-6b37e91045eb" />

<img width="664" height="175" alt="image" src="https://github.com/user-attachments/assets/8c392337-f571-4dd0-9304-fcc9a67088b9" />

## Bit Flipping Attacks

### What is Unauthenticated Encryption?

Unauthenticated encryption refers to encryption that does not include a mechanism to verify the integrity or authenticity of the ciphertext. This means that an attacker can modify encrypted data that is in transit, and the system will still accept and process it without detecting any tampering.

When the application decrypts tampered ciphertext without verifying its integrity, an attacker can manipulate the plaintext in predictable ways. This is the root cause of bit-flipping attacks.

A classic example is AES in CBC (Cipher Block Chaining) mode without an authentication tag. AES-CBC encrypts data securely but does not ensure integrity. If an attacker can modify the ciphertext, they can manipulate certain bits of the decrypted plaintext without breaking the encryption.

This leads to bit-flipping attacks, where an attacker changes ciphertext in a way that results in controlled modifications in the plaintext.

---

### Bit Flipping Attacks

Bit flipping attacks target systems that use unauthenticated encryption, allowing an attacker to modify ciphertext so that the decrypted plaintext is manipulated in predictable ways. This type of attack is particularly dangerous when systems assume that encrypted data is inherently safe to trust without verifying its integrity.

AES-CBC can be vulnerable to bit-flipping attacks if there is no MAC (Message Authentication Code) to check whether the ciphertext was changed.

Think of it like this:
- AES-CBC encrypts data in blocks.
- Each plaintext block is connected to the previous ciphertext block.
- If an attacker changes some bits in a ciphertext block, those changes can cause controlled changes in the decrypted plaintext.
- Without a MAC, the system may not notice that the ciphertext was modified.

For example, consider an encrypted payload: `{"role":"0"}`

If this ciphertext is tampered with, the role could be escalated to "1". Without integrity protection, the system would accept the manipulated plaintext as legitimate.

Suppose the original decrypted message is: `role=user`

An attacker modifies the ciphertext so that it decrypts to: `role=admin`

The attacker doesn't need to know the encryption key. They are manipulating the ciphertext so that the decrypted result changes.

A MAC helps prevent this because the attacker cannot modify the ciphertext and produce a valid MAC without knowing the secret key.

---

### Exercise

Navigate to `http://bcts.thm/labs/lab4/`.

<img width="446" height="149" alt="image" src="https://github.com/user-attachments/assets/7703be75-3259-4ac4-94eb-9b50685829ef" />

The application accepts any credential as shown below:

```
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['username'], $_POST['password'])) {
    $username = htmlspecialchars($_POST['username']);
    $password = htmlspecialchars($_POST['password']);

    $message = "username={$username}";
    $role = "0";
    $token = encrypt_data($message, $key, $iv);
    $token2 = encrypt_data($role, $key, $iv);

    setcookie("auth_token", $token, time() + 3600, "/");
    setcookie("role", $token2, time() + 3600, "/");
    header("Location: dashboard.php");
    exit();
}
```

This PHP code handles a POST login request. It takes the submitted username and password, cleans them using `htmlspecialchars()`, and creates a message containing the username, such as `username=user`. It then sets the user's role to `0` and encrypts both the username message and role using `encrypt_data()` with the same key and IV. These encrypted values are stored as cookies called `auth_token` and role, each valid for one hour. Finally, the user is redirected to `dashboard.php`.

IV (Initialization Vector) is a random or unpredictable value used along with an encryption key when encrypting data. It prevents the same plaintext from producing the same ciphertext every time.

As we can see in the code above, the cookie named `role` uses an encrypted version of the text `0`.

<img width="536" height="223" alt="image" src="https://github.com/user-attachments/assets/fcdb7284-1c61-402f-8ae4-c6739a36c558" />

Below is a sample script `flipbit.py` that will flip the `role=0` to `role=1`.

**Explanation of Script**

**Hex Decoding**:

```
try:
    cipher_bytes = bytearray(unhexlify(original_token))
except ValueError:
    print("Invalid token format! Make sure it's a valid hex string.")
    exit(1)
```

- Converts the hex-encoded token into a bytearray for modification.
- If the token is not in a valid hex format, an error is printed, and the script exits.

**AES Block Size and Initialization Vector (IV)**

```
block_size = 16
```

- AES uses a 16-byte block size.
- The first 16 bytes of the encrypted token represent the IV in AES-CBC mode.

**Bit-Flipping Attack**

```
guest_offset = 0

xor_diff = [
    0x01,  # '0' -> '1'
]
```

- Bit-flipping works by modifying the IV to change the decrypted plaintext.
- `guest_offset = 0` means the modification starts at byte 0 of the IV.
- The script applies an XOR operation (`^=`) to change a specific byte in the IV.
- In this case, it changes '0' to '1' in the decrypted text.

**Applying the Bit Flip**

```
for i, diff in enumerate(xor_diff):
    print(f"[DEBUG] Modifying byte at offset {guest_offset + i}: {hex(cipher_bytes[guest_offset + i])} XOR {hex(diff)}")
    cipher_bytes[guest_offset + i] ^= diff
```

- Iterates over `xor_diff` and modifies the corresponding bytes in the IV.
- Uses XOR (`^=`) to modify the first byte of the IV.

First copy the role token from the Developer Tools and then run the script `flipbit.py`.

<img width="617" height="116" alt="image" src="https://github.com/user-attachments/assets/c03f3e28-2ec3-47d3-b6d1-c965ea8e15af" />

Using the modified cookie, change the existing value by double clicking of the cookie role and refresh the page.

---

### Answer the questions below

What is the flag?

<img width="1068" height="468" alt="image" src="https://github.com/user-attachments/assets/bdc9305d-4119-4111-bb56-724d9fee038a" />










