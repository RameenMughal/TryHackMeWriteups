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




