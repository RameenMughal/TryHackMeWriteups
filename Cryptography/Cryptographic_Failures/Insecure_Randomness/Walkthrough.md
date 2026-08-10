# Insecure Randomness

Room: [Insecure Randomness](https://tryhackme.com/room/insecurerandomness)

Prerequisites: [OWASP Top 10 - 2025 Module](https://tryhackme.com/module/owasp-top-10-2025)

<img width="947" height="209" alt="image" src="https://github.com/user-attachments/assets/f4d67f18-970e-43d4-9935-888e6f03bc27" />

## Introduction

Insecure randomness occurs when web applications use predictable or poorly generated random values, making them vulnerable to attacks. While randomness is essential for securing tokens, session IDs, and cryptographic keys, insecure implementation can allow attackers to exploit these predictable values to bypass authentication, hijack sessions, or even decrypt sensitive data.

In this room, we will explore techniques to identify and exploit vulnerabilities caused by insecure randomness. This will provide you with the knowledge to assess and enhance the security of web applications by ensuring proper random number generation practices. 

---

### Connecting to the Machine

You can start the lab machine by clicking the "Start Lab Machine" button attached to this task. You may access the VM using the AttackBox or your VPN connection. 

I will be using my Kali Linux to connect to the TryHackMe Server by command: `sudo openvpn FILENAME`

You can check how to connect through OpenVPN by this room: [OpenVPN](https://tryhackme.com/room/openvpn)

You can access the web app by visiting the URL h`ttp://random.thm:8090/case/` but first, you must add the hostname in your OS or AttackBox.

First open the file to add hostname by `sudo nano /etc/hosts`

Then copy paste the `MACHINE_IP random.thm` into the file.

Save the file and type `http://random.thm:8090/case/` in the browser to access the website.

## Few Important Concepts

### Randomness

Randomness refers to the lack of pattern or predictability in data, making it an essential component in secure systems.Image of three colorful dice showing different numbers. In cryptography, true randomness ensures an attacker cannot predict values such as keys, tokens, and nonces. We will explore how randomness is generated and the distinction between True Random Number Generators (TRNG) and Pseudorandom Number Generators (PRNG).

---

### Entropy

Entropy represents the amount of randomness or unpredictability in a system and is often used to assess the security of cryptographic keys, tokens, or random values. Higher entropy indicates greater uncertainty, making it more difficult for attackers to predict or guess the values, which is essential for secure cryptographic operations. Low entropy can lead to weak security, increasing the risk of attacks like brute-forcing or token prediction. 

---

### Cryptographic Keys

Cryptographic keys are secret values used in algorithms to encrypt and decrypt data, ensuring confidentiality, integrity, and authentication. They are critical components in symmetric and asymmetric encryption methods and must be securely generated and managed to prevent unauthorised access. The strength of a cryptographic key depends on its length and randomness. 

---

### Session Tokens and Unique Identifiers

Session tokens and unique identifiers are used to maintain user sessions and track interactions in web applications. They must be securely generated with sufficient randomness and uniqueness to prevent token prediction and session hijacking. Proper management and protection of these tokens are essential to ensure secure user authentication and authorisation.

---

### Seeding

Seeding refers to providing an initial value, known as a seed, to a secure cryptographic function to generate a sequence of random-looking numbers. While these secure functions produce numbers that appear random, the sequence is entirely determined by the seed, meaning the same seed will always result in the same sequence.

---

### Answer the questions below

1. What measures the amount of randomness or unpredictability in a system?

Entropy

2. Is it a good practice to keep the same seed value for all cryptographic functions? (yea/nay)

nay

## Types of Random Number Generators

### True Random Number Generator (TRNG)

TRNGs generate randomness by relying on unpredictable physical phenomena like thermal noise or radioactive decay. Since these generators stem from natural events, they produce inherently random values. TRNGs are commonly used in highly sensitive cryptographic operations, such as generating the keys for algorithms like RSA or ECC. These keys are then used in tasks like encryption, digital signatures, and certificate creation, where unpredictability is crucial for security. However, TRNGs require specialised hardware and can be slower than other RNGs, making them less suitable for tasks requiring rapid number generation.

RSA is a method for encrypting data using two keys: one to lock (encrypt) and another to unlock (decrypt) it, relying on the difficulty of factoring large number.

Elliptic Curve Cryptography (ECC) is a way to encrypt data using smaller keys while still providing strong security. It is based on the math of elliptic curves.

<img width="1140" height="340" alt="image" src="https://github.com/user-attachments/assets/c44933d5-b3f5-49a3-9397-3c1a2f399623" />

As shown in the above figure, the basic workflow includes capturing a seeding value from a natural, unpredictable physical source. This value is then fed into hardware that performs a non-deterministic transformation to generate a sequence of truly random, unpredictable numbers. The output of TRNGs cannot be predicted or reproduced, making them ideal for high-security cryptographic operations.

---

### Pseudorandom Number Generator (PRNG)

PRNGs, unlike TRNGs, generate random numbers algorithmically based on an initial seed value. While they may appear random, they are deterministic, meaning the same seed will always produce the same sequence of numbers. PRNGs are faster and more efficient than TRNGs and are suitable for applications that quickly need large quantities of random numbers, like simulations or gaming. However, since they are algorithmic, predictability becomes a risk if an attacker can deduce the seed or its generation method.

#### Types of PRNGs

We will examine the two primary types of PRNGs, statistical and cryptographic PRNGs, focusing on their differences and specific applications.

**1. Statistical PRNG**

Statistical PRNGs are designed to produce numbers that pass statistical randomness tests, meaning the numbers appear random and lack obvious patterns. These generators are widely used in non-security applications such as simulations, statistical sampling, and gaming, where randomness is required but not in a security-critical context. However, statistical PRNGs are deterministic by nature, meaning the same seed value will always produce the same sequence of numbers. This predictability makes them unsuitable for cryptographic tasks where unpredictability is paramount. 

**2. Cryptographically Secure PRNG (CSPRNG)**

A CSPRNG is a type of PRNG made for security purposes. It generates random numbers that are very difficult to predict or guess.

Unlike normal PRNGs, CSPRNGs are designed so that even if someone knows some of the generated numbers or part of the system’s internal information, they still cannot easily figure out the next numbers.

CSPRNGs are important in security applications such as:
- Creating encryption keys
- Generating secure session tokens
- Producing random numbers for security protocols

They must follow strict security requirements to make sure their output cannot be predicted. Although CSPRNGs can be slower than normal PRNGs because they use extra security measures, they are very important for keeping cryptographic systems secure.

---

### Answer the questions below

You prepare a game involving immediate interaction and random event simulation but with no critical security requirements. Which type of RNG would be most appropriate for this purpose? Write the correct option only.
a) TRNG
b) Statistical PRNG
c) We should not use randomness in games
d) None of the above

b




