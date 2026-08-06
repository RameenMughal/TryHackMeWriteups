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







