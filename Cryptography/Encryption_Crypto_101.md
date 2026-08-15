# Encryption - Crypto 101

Room: [Encryption - Crypto 101](https://tryhackme.com/room/encryptioncrypto101)

<img width="1891" height="400" alt="image" src="https://github.com/user-attachments/assets/151d743b-9543-4ffb-b54a-a061f4a13503" />

## Key Terms

**Ciphertext** - The result of encrypting a plaintext, encrypted data

**Cipher** - A method of encrypting or decrypting data. Modern ciphers are cryptographic, but there are many non cryptographic ciphers like Caesar.

**Plaintext** - Data before encryption, often text but not always. Could be a photograph or other file

**Encryption** - Transforming data into ciphertext, using a cipher.

**Encoding** - NOT a form of encryption, just a form of data representation like base64. Immediately reversible.

**Key** - Some information that is needed to correctly decrypt the ciphertext and obtain the plaintext.

**Passphrase** - Separate to the key, a passphrase is similar to a password and used to protect a key.

A passphrase is basically a type of password, but it is generally longer and word-based.

**Asymmetric encryption** - Uses different keys to encrypt and decrypt.

**Symmetric encryption** - Uses the same key to encrypt and decrypt

**Brute force** - Attacking cryptography by trying every different password or every different key

**Cryptanalysis** - Attacking cryptography by finding a weakness in the underlying maths

**Alice and Bob** - Used to represent 2 people who generally want to communicate. They’re named Alice and Bob because this gives them the initials A and B.

---

### Answer the questions below

Are SSH keys protected with a passphrase or a password?

Passphrase

## Why is Encryption Important?

Cryptography is used to protect confidentiality, ensure integrity, ensure authenticity.

When you connect to SSH, your client and the server establish an encrypted tunnel so that no one can snoop on your session.

Whenever sensitive user data needs to be stored, it should be encrypted. Standards like [PCI-DSS](https://listings.pcisecuritystandards.org/documents/PCI_DSS_for_Large_Organizations_v1.pdf) state that the data should be encrypted both at rest (in storage) AND while being transmitted. If you’re handling payment card details, you need to comply with these PCI regulations. Medical data has similar standards. With legislation like GDPR and California’s data protection, data breaches are extremely costly and dangerous to you as either a consumer or a business.

DO NOT encrypt passwords unless you’re doing something like a password manager. Passwords should not be stored in plaintext, and you should use hashing to manage them safely.

Because encryption is reversible, while password hashing is designed to be one-way.

---

### Answer the questions below

1. What does SSH stand for?

Secure Shell

2. How do webservers prove their identity?

Certificates

3. What is the main set of standards you need to comply with if you store or process payment card details?

PCI-DSS

## Crucial Crypto Maths

### Answer the questions below

1. What's 30 % 5?

0

2. What's 25 % 7

4

3. What's 118613842 % 9091

3565, Hint was to use Python

<img width="894" height="270" alt="image" src="https://github.com/user-attachments/assets/57a31168-4c7d-4398-8488-bc214f4b33a7" />

## Types of Encryption

The two main categories of Encryption are symmetric and asymmetric.

**Symmetric encryption** uses the same key to encrypt and decrypt the data. Examples of Symmetric encryption are DES (Broken) and AES. These algorithms tend to be faster than asymmetric cryptography, and use smaller keys (128 or 256 bit keys are common for AES, DES keys are 56 bits long).

**Asymmetric encryption** uses a pair of keys, one to encrypt and the other in the pair to decrypt. Examples are RSA and Elliptic Curve Cryptography. Normally these keys are referred to as a public key and a private key. Data encrypted with the private key can be decrypted with the public key, and vice versa. Your private key needs to be kept private, hence the name. Asymmetric encryption tends to be slower and uses larger keys, for example RSA typically uses 2048 to 4096 bit keys.

Suppose Alice wants to send Bob a secret message.

Bob has:
- Public key → everyone can have it
- Private key → only Bob has it

Alice does:

Message
   ↓
Encrypt with Bob's PUBLIC key
   ↓
Encrypted message
   ↓
Bob decrypts with his PRIVATE key
   ↓
Original message

So even though everyone can access Bob's public key, that's okay. Because the public key is used to encrypt, but only Bob's private key can decrypt.

RSA and Elliptic Curve cryptography are based around different mathematically difficult (intractable) problems, which give them their strength. 

---

### Answer the questions below

1. Should you trust DES? Yea/Nay

Nay

2. What was the result of the attempt to make DES more secure so that it could be used for longer?

Triple DES

3. Is it ok to share your public key? Yea/Nay

Yea

## RSA - Rivest Shamir Andleman

### The math(s) side

RSA is based on the mathematically difficult problem of working out the factors of a large number. It’s very quick to multiply two prime numbers together, say `17*23 = 391`, but it’s quite difficult to work out what two prime numbers multiply together to make `14351` (`113x127` for reference).

---

### The attacking side

The maths behind RSA seems to come up relatively often in CTFs, normally requiring you to calculate variables or break some encryption based on them. 

There are some excellent tools for defeating RSA challenges in CTFs, and my personal favorite is [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool) which has worked very well for me. I’ve also had some success with [rsatool](https://github.com/ius/rsatool).

The key variables that you need to know about for RSA in CTFs are p, q, m, n, e, d, and c.

“p” and “q” are large prime numbers, “n” is the product of p and q.

The public key is n and e, the private key is n and d.

“m” is used to represent the message (in plaintext) and “c” represents the ciphertext (encrypted text).

---

### CTFs involving RSA

Crypto CTF challenges often present you with a set of these values, and you need to break the encryption and decrypt a message to retrieve the flag.

There’s a lot more maths to RSA, and it gets quite complicated fairly quickly. If you want to learn the maths behind it, I recommend reading MuirlandOracle’s blog post here: [RSA Encryption - MuirlandOracle](https://muirlandoracle.co.uk/2020/01/29/rsa-encryption/).

---

### Answer the questions below

p = 4391, q = 6659. What is n?

29239669 as n = p x q

## Establishing Keys Using Asymmetric Cryptography

A very common use of asymmetric cryptography is exchanging keys for symmetric encryption.

Asymmetric encryption tends to be slower, so for things like HTTPS symmetric encryption is better.

But the question is, how do you agree a key with the server without transmitting the key for people snooping to see?

---

### Metaphor time

Imagine you have a secret code, and instructions for how to use the secret code. If you want to send your friend the instructions without anyone else being able to read it, what you could do is ask your friend for a lock.

Only they have the key for this lock, and we’ll assume you have an indestructible box that you can lock with it.

If you send the instructions in a locked box to your friend, they can unlock it once it reaches them and read the instructions.

After that, you can communicate in the secret code without risk of people snooping.

In this metaphor, the secret code represents a symmetric encryption key, the lock represents the server’s public key, and the key represents the server’s private key.

You’ve only used asymmetric cryptography once, so it’s fast, and you can now communicate privately with symmetric encryption.

---

### The Real World

In reality, you need a little more cryptography to verify the person you’re talking to is who they say they are, which is done using digital signatures and certificates. 

You can find a lot more detail on how HTTPS (one example where you need to exchange keys) really works from this excellent blog post [How Does HTTPS Actually Work - Robert Heaton](https://robertheaton.com/2014/03/27/how-does-https-actually-work/)

## Digital Signatures and Certificates

### What's a Digital Signature?

Digital signatures are a way to prove the authenticity of files, to prove who created or modified them. Using asymmetric cryptography, you produce a signature with your private key and it can be verified using your public key. As only you should have access to your private key, this proves you signed the file. 

The simplest form of digital signature would be encrypting the document with your private key, and then if someone wanted to verify this signature they would decrypt it with your public key and check if the files match.

### Certificates - Prove who you are!

Certificates are also a key use of public key cryptography, linked to digital signatures. A common place where they’re used is for HTTPS. How does your web browser know that the server you’re talking to is the real tryhackme.com?

The answer is certificates. The web server has a certificate that says it is the real tryhackme.com. The certificates have a chain of trust, starting with a root CA (certificate authority). Root CAs are automatically trusted by your device, OS, or browser from install. Certs below that are trusted because the Root CAs say they trust that organisation. Certificates below that are trusted because the organisation is trusted by the Root CA and so on. There are long chains of trust. 

Again, this blog post explains this much better than I can. [How Does HTTPS Actually Work](https://robertheaton.com/2014/03/27/how-does-https-actually-work/)

You can get your own HTTPS certificates for domains you own using Let’s Encrypt for free. If you run a website, it’s worth setting it up.

---

### Answer the questions below

What can you use to verify that a file has not been modified and is the authentic file as the author intended?

Digital Signature


