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

Plaintext: `TRYHACKME`
Key: 3 (Assume it is a right shift of 3.)
Cipher: Caesar Cipher

We can easily figure out that T becomes W, R becomes U, Y becomes B, and so on. As you noticed, once we reach Z, we start all over. Consequently, we get the ciphertext of `WUBKDFNPH`.


