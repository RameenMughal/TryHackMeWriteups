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








