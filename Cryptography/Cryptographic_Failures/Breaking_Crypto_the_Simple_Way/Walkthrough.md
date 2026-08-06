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

