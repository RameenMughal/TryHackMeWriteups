# Cryptography Concepts

Room: [Cryptography Concepts](https://tryhackme.com/room/cryptographyconcepts)

Prerequisites Rooms:
- [CIA Triad](https://tryhackme.com/room/theciatriad)
- [Data Encoding](https://tryhackme.com/room/dataencoding)

<img width="1877" height="382" alt="image" src="https://github.com/user-attachments/assets/192f0d04-72ed-477b-adb2-b6825098fa15" />

## Introduction

### A Real-World Scenario

Imagine you're running a small medical clinic. You need to send patient records, including names, medical conditions, and treatment history, to specialists and insurance companies over the internet. The problem? Data doesn't travel directly from you to the recipient. It bounces through dozens of computers and routers along the way. Without protection, anyone with access to those systems could read, change, or block your data.

Cryptography solves this by using mathematical rules and secret keys to scramble information into gibberish that only authorised people can unscramble.

## Hiding Information - Symmetric Encryption

### Understanding the Basics

Before we jump into symmetric encryption, let's define the core terms we'll use throughout this room:
- **Plaintext** - A message you can read normally. Like `HELLO` or `Patient name: Alice Smith`.
- **Ciphertext** - A scrambled version that's not supposed to make sense. Like `KHOOR` or `Sdwlhqw qdph: Dolfh Vplwk`.
- **Key** - The secret ingredient that controls how scrambling and unscrambling work. Think of it as a password that the algorithm uses.
- **Algorithm** - The public recipe—the set of steps that explain how to use the key on the message. Everyone can know the algorithm. Security comes from keeping the key secret.

**Encryption process**: plaintext + encryption algorithm + key  → ciphertext

**Decryption process**: ciphertext + decryptiong algorithm + key   → plaintext

---

### The Lockbox Analogy

Think about a physical lockbox:
- The algorithm is how the lock works. Anyone can see you insert a key and turn it, hence it's not secret.
- The key is your specific metal key. Only people with that exact key can open your box.
- The plaintext is the letter inside the box.
- The ciphertext is that locked box travelling through the postal system.

