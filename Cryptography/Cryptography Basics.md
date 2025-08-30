# Cryptography Basics

<img width="908" height="173" alt="image" src="https://github.com/user-attachments/assets/5c0e7b69-7529-442a-9b0d-48f7b25ebd81" />

## Introduction

Cryptography lays the foundation for our digital world. While networking protocols have made it possible for devices spread across the globe to communicate, cryptography has made it possible to trust this communication.

## Importance of Cryptography

Cryptography’s ultimate purpose is to ensure secure communication in the presence of adversaries. The term secure includes confidentiality and integrity of the communicated data. 

Cryptography can be defined as the practice and study of techniques for secure communication and data protection where we expect the presence of adversaries and third parties. 

In other words, these adversaries should not be able to disclose or alter the contents of the messages.

Cryptography is used to protect confidentiality, integrity, and authenticity. In this age, you use cryptography daily, and you’re almost certainly reading this over an encrypted connection.

Some types of sensitive information need special rules to keep them safe, and these rules often use cryptography. For example, companies that deal with credit cards must follow PCI DSS, which requires encrypting the data when stored and when sent. In healthcare, laws like HIPAA in the USA, GDPR in the EU, and the UK’s DPA also require protecting medical records. These rules show that even if people don’t see it, cryptography is an important part of keeping data secure.

### Answer the questions below

What is the standard required for handling credit card information?

PCI DSS

## Plaintext to Ciphertext

We begin with the plaintext that we want to encrypt. The plaintext is the readable data; it can be anything from a simple “hello”, a cat photo, credit card information, or medical health records. From a cryptography perspective, these are all “plaintext” messages waiting to be encrypted. 

The plaintext is passed through the encryption function along with a proper key; the encryption function returns a ciphertext. The encryption function is part of the cipher; a cipher is an algorithm to convert a plaintext into a ciphertext and vice versa.

To recover the plaintext, we must pass the ciphertext along with the proper key via the decryption function, which would give us the original plaintext.

The terms are listed below:
- **Plaintext** is the original, readable message or data before it’s encrypted. 
- **Ciphertext** is the scrambled, unreadable version of the message after encryption. Ideally, we cannot get any information about the original plaintext except its approximate size.
- **Cipher** is an algorithm or method to convert plaintext into ciphertext and back again. A cipher is usually developed by a mathematician.
- **Key** is a string of bits the cipher uses to encrypt or decrypt data. In general, the used cipher is public knowledge; however, the key must remain secret unless it is the public key in asymmetric encryption. 
- **Encryption** is the process of converting plaintext into ciphertext using a cipher and a key. Unlike the key, the choice of the cipher is disclosed.
- **Decryption** is the reverse process of encryption, converting ciphertext back into plaintext using a cipher and a key. Although the cipher would be public knowledge, recovering the plaintext without knowledge of the key should be impossible (infeasible).

### Answer the questions below

1. What do you call the encrypted plaintext?

Ciphertext

2. What do you call the process that returns the plaintext?

Decryption

## Historical Ciphers

Cryptography’s history is long and dates back to ancient Egypt in 1900 BCE. However, one of the simplest historical ciphers is the Caesar Cipher from the first century BCE. The idea is simple: shift each letter by a certain number to encrypt the message.

Consider the following example:
- Plaintext: `TRYHACKME`
- Key: 3 (Assume it is a right shift of 3.)
- Cipher: Caesar Cipher

We can easily figure out that T becomes W, R becomes U, Y becomes B, and so on. As you noticed, once we reach Z, we start all over. Consequently, we get the ciphertext of `WUBKDFNPH`.

<img width="1120" height="480" alt="image" src="https://github.com/user-attachments/assets/e8c80c98-093b-44cc-a8b7-5c7e5d479cfd" />

To decrypt, we need the following information:
- Ciphertext: `WUBKDFNPH`
- Key: 3
- Cipher: Caesar Cipher

<img width="1120" height="480" alt="image" src="https://github.com/user-attachments/assets/157056ff-c09d-42b1-b4db-c7a2a8320a62" />

For encryption, we shift to the right by three; for decryption, we shift to the left by three and recover the original plaintext, as illustrated in the image above. 

However, if someone gives you a ciphertext and tells you that it was encrypted using Caesar Cipher, recovering the original text would be a trivial task as there are only 25 possible keys. The English alphabet is 26 letters, and shifting by 26 will keep the letter unchanged; hence, 25 valid keys for encryption with Caesar Cipher. 

The figure below shows how decryption will succeed by attempting all the possible keys; in this case, we recovered the original message with Key = 5. Consequently, by today’s standards, where the cipher is publicly known, Caesar Cipher is considered insecure.

<img width="1800" height="660" alt="image" src="https://github.com/user-attachments/assets/a636e525-b1f0-4d11-8c5c-1857ab81c102" />

You would come across many more historical ciphers in movies and cryptography books. Examples include:
- The Vigenère cipher from the 16th century
- The Enigma machine from World War II
- The one-time pad from the Cold War

### Answer the questions below

Knowing that `XRPCTCRGNEI` was encrypted using Caesar Cipher, what is the original plaintext?

By using CyberChef, using ROT13 feature which is same as Ceasar Cipher and checking the Amount (key) by 1 till 25.

I get the plaintext when Amount is 11.

<img width="463" height="271" alt="image" src="https://github.com/user-attachments/assets/19603fd6-0708-4e01-ab7d-1358641565a6" />

## Types of Encryption

The two main categories of encryption are **symmetric** and **asymmetric**.

### Symmetric Encryption

Symmetric encryption, also known as symmetric cryptography, uses the same key to encrypt and decrypt the data, as shown in the figure below. Keeping the key secret is a must; it is also called **private key cryptography**. 

Furthermore, communicating the key to the intended parties can be challenging as it requires a secure communication channel. Maintaining the secrecy of the key can be a significant challenge, especially if there are many recipients. The problem becomes more severe in the presence of a powerful adversary; consider the threat of industrial espionage, for instance.

<img width="1840" height="1040" alt="image" src="https://github.com/user-attachments/assets/2a6220e3-3b7f-41e6-9d4f-ed8426082f2d" />

Consider the simple case where you created a password-protected document to share it with your colleague. You can easily email the encrypted document to your colleague, but most likely, you cannot email them the password. The reason is that anyone with access to their mailbox would access both the password-protected document and its password. Therefore, you need to think of a different way, i.e., channel, to share the password. Unless you think of a secure, accessible channel, one solution would be to meet in person and communicate the password to them.

Examples of symmetric encryption are **DES** (Data Encryption Standard), **3DES** (Triple DES) and **AES** (Advanced Encryption Standard).
- DES was adopted as a standard in 1977 and uses a 56-bit key. With the advancement in computing power, in 1999, a DES key was successfully broken in less than 24 hours, motivating the shift to 3DES.
- 3DES is DES applied three times; consequently, the key size is 168 bits, though the effective security is 112 bits. 3DES was more of an ad-hoc solution when DES was no longer considered secure. 3DES was deprecated in 2019 and should be replaced by AES; however, it may still be found in some legacy systems.
- AES was adopted as a standard in 2001. Its key size can be 128, 192, or 256 bits.

### Asymmetric Encryption

Unlike symmetric encryption, which uses the same key for encryption and decryption, asymmetric encryption uses a pair of keys, one to encrypt and the other to decrypt, as shown in the illustration below. To protect confidentiality, asymmetric encryption or **asymmetric cryptography** encrypts the data using the public key; hence, it is also called **public key cryptography**.

<img width="1840" height="1040" alt="image" src="https://github.com/user-attachments/assets/bb9b9416-c27e-4611-a2c4-0d023cc89599" />

Examples are RSA, Diffie-Hellman, and Elliptic Curve cryptography (ECC). 

The two keys involved in the process are referred to as a public key and a private key. Data encrypted with the public key can be decrypted with the private key. Your private key needs to be kept private, hence the name.

Asymmetric encryption tends to be slower, and many asymmetric encryption ciphers use larger keys than symmetric encryption. 

For example, RSA uses 2048-bit, 3072-bit, and 4096-bit keys; 2048-bit is the recommended minimum key size. Diffie-Hellman also has a recommended minimum key size of 2048 bits but uses 3072-bit and 4096-bit keys for enhanced security. On the other hand, ECC can achieve equivalent security with shorter keys. For example, with a 256-bit key, ECC provides a level of security comparable to a 3072-bit RSA key.

Asymmetric encryption is based on a particular group of mathematical problems that are easy to compute in one direction but extremely difficult to reverse. In this context, extremely difficult means practically infeasible. 

For example, we can rely on a mathematical problem that would take a very long time, for example, millions of years, to solve using today’s technology.

### Summary of New Terms

- **Symmetric encryption** is a method in which the same key is used for both encryption and decryption. Consequently, this key must remain secure and never be disclosed to anyone except the intended party.
- **Asymmetric encryption** is a method that uses two different keys: a public key for encryption and a private key for decryption.

### Answer the questions below

1. Should you trust DES? (Yea/Nay)

Nay

2. When was AES adopted as an encryption standard?

2001

## Basic Math

The building blocks of modern cryptography lie in mathematics. To demonstrate some basic algorithms, we will cover two mathematical operations that are used in various algorithms:
- XOR Operation
- Modulo Operation

### XOR Operation

XOR, short for “exclusive OR”, is a logical operation in binary arithmetic that plays a crucial role in various computing and cryptographic applications. 

In binary, XOR compares two bits and returns 1 if the bits are different and 0 if they are the same, as shown in the truth table below. This operation is often represented by the symbol ⊕ or ^.

| A | B | A ⊕ B |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   1   |
| 1 | 0 |   1   |
| 1 | 1 |   0   |

Let’s consider an example where we want to apply XOR to the binary numbers 1010 and 1100. 

In this case, we perform the operation bit by bit: 1 ⊕ 1 = 0, 0 ⊕ 1 = 1, 1 ⊕ 0 = 1, and 0 ⊕ 0 = 0, resulting in 0110.

XOR has several interesting properties that make it useful in cryptography and error detection. 

One key property is that applying XOR to a value with itself results in 0, and applying XOR to any value with 0 leaves it unchanged. This means A ⊕ A = 0, and A ⊕ 0 = A for any binary value A. 

Additionally, XOR is commutative, i.e., A ⊕ B = B ⊕ A. And it is associative, i.e., (A ⊕ B) ⊕ C = A ⊕ (B ⊕ C).

We will demonstrate how XOR can be used as a basic symmetric encryption algorithm. Consider the binary values P and K, where P is the plaintext, and K is the secret key. The ciphertext is C = P ⊕ K.

Now, if we know C and K, we can recover P. We start with C ⊕ K = (P ⊕ K) ⊕ K. But we know that (P ⊕ K) ⊕ K = P ⊕ (K ⊕ K) because XOR is associative. 

Furthermore, we know that K ⊕ K = 0; consequently, (P ⊕ K) ⊕ K -> P ⊕ (K ⊕ K) -> P ⊕ 0 = P. 

In other words, XOR served as a simple symmetric encryption algorithm. In practice, it is more complicated as we need a secret key as long as the plaintext.

### Modulo Operation

Another mathematical operation we often encounter in cryptography is the modulo operator, commonly written as % or as mod. The modulo operator, X%Y, is the remainder when X is divided by Y. 

In our daily life calculations, we focus more on the result of division than on the remainder. The remainder plays a significant role in cryptography.

Let’s consider a few examples.
- 25 % 5 = 0 because 25 divided by 5 is 5, with a remainder of 0, i.e., 25 = 5 × 5 + 0
- 23 % 6 = 5 because 23 divided by 6 is 3, with a remainder of 5, i.e., 23 = 3 × 6 + 5
- 23 % 7 = 2 because 23 divided by 7 is 3 with a remainder of 2, i.e., 23 = 3 × 7 + 2

An important thing to remember about modulo is that it’s not reversible. If we are given the equation x % 5 = 4, infinite values of x would satisfy this equation.

The modulo operation always returns a non-negative result less than the divisor. This means that for any integer a and positive integer n, the result of a % n will always be in the range 0 to n − 1.

### Answer the questions below

1. What’s 1001 ⊕ 1010?

0011

2. What’s 118613842 % 9091?

3565

3. What’s 60 % 12?

0
