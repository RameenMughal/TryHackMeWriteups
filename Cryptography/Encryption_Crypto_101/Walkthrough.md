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

Again, this blog post explains this much better than I can. [How Does HTTPS Actually Work - Robert Heaton](https://robertheaton.com/2014/03/27/how-does-https-actually-work/)

You can get your own HTTPS certificates for domains you own using Let’s Encrypt for free. If you run a website, it’s worth setting it up.

---

### Answer the questions below

What can you use to verify that a file has not been modified and is the authentic file as the author intended?

Digital Signature

## SSH Authentication

### Encryption and SSH authentication

By default, SSH is authenticated using usernames and passwords in the same way that you would log in to the physical machine.

At some point, you’re almost certain to hit a machine that has SSH configured with key authentication instead. This uses public and private keys to prove that the client is a valid and authorised user on the server. By default, SSH keys are RSA keys. You can choose which algorithm to generate, and/or add a passphrase to encrypt the SSH key. `ssh-keygen` is the program used to generate pairs of keys most of the time.

---

### SSH Private Keys

You should treat your private SSH keys like passwords. Don’t share them, they’re called private keys for a reason. If someone has your private key, they can use it to log in to servers that will accept it unless the key is encrypted.

It’s very important to mention that the passphrase to decrypt the key isn’t used to identify you to the server at all, all it does is decrypt the SSH key. The passphrase is never transmitted, and never leaves your system.

Using tools like John the Ripper, you can attack an encrypted SSH key to attempt to find the passphrase, which highlights the importance of using a secure passphrase and keeping your private key private.

When generating an SSH key to log in to a remote machine, you should generate the keys on your machine and then copy the public key over as this means the private key never exists on the lab machine. 

---

### How do I use these keys?

The `~/.ssh` folder is the default place to store these keys for OpenSSH. The `authorized_keys` file in this directory holds public keys that are allowed to access the server if key authentication is enabled. By default on many distros, key authentication is enabled as it is more secure than using a password to authenticate. Normally for the root user, only key authentication is enabled.

In order to use a private SSH key, the permissions must be set up correctly otherwise your SSH client will ignore the file with a warning. Only the owner should be able to read or write to the private key (600 or stricter). `ssh -i keyNameGoesHere user@host` is how you specify a key for the standard Linux OpenSSH client.

---

### Using SSH keys to get a better shell

SSH keys are a good way to get a more stable shell after getting a reverse shell. If the user is allowed to log in through SSH, you can use SSH keys to connect to the machine properly. This gives you a better shell without problems like `Ctrl+C` breaking the connection or Tab completion not working. Leaving an SSH key in `authorized_keys` can also let you log back into the machine later, which can act as a backdoor.

---

### Answer the questions below

1. I recommend giving this a go yourself. Deploy a VM, like [Linux Fundamentals 2](https://tryhackme.com/room/linuxfundamentalspart2) and try to add an SSH key and log in with the private key.

This is a premium room so skipping this question.

2. Download the SSH Private Key attached to this room.

Click `Download Tasks File`

3. What algorithm does the key use?

RSA, because the file name consist of `rsa` indicating the algorithm.

4. Crack the password with John The Ripper and rockyou, what's the passphrase for the key?

`delicious`

First convert the RSA file into hash format that the John the Ripper understands to bruteforce the passphrase: `ssh2john ID_RSA_FILE > hash.txt`

<img width="285" height="20" alt="image" src="https://github.com/user-attachments/assets/9e068550-0fe0-488d-b686-3903f43a7d87" />

`ssh2john` takes your SSH private key (`id_rsa`) and converts it into a hash format that John the Ripper understands. It does not crack the password yet.

Then brute force the passphrase: `john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt`

<img width="375" height="50" alt="image" src="https://github.com/user-attachments/assets/f4c6a2e2-279a-46f7-896e-723c44a38a1e" />

Display the cracked passphrase: `john --show hash.txt`

<img width="196" height="50" alt="image" src="https://github.com/user-attachments/assets/dcfdcc91-9a78-43a5-b3cb-d747e5969058" />

## Explaining Diffie Hellman Key Exchange

### What is Key Exchange?

Key exchange allows 2 people/parties to establish a set of common cryptographic keys without an observer being able to get these keys. Generally, to establish common symmetric keys.

---

### How does Diffie Hellman Key Exchange work?

Alice and Bob want to talk securely. They want to establish a common key, so they can use symmetric cryptography, but they don’t want to use key exchange with asymmetric cryptography. This is where DH Key Exchange comes in.

Alice and Bob both have secrets that they generate, let’s call these A and B. They also have some common material that’s public, let’s call this C.

We need to make some assumptions. Firstly, whenever we combine secrets/material it’s impossible or very very difficult to separate. Secondly, the order that they're combined in doesn’t matter.

Alice and Bob will combine their secrets with the common material, and form AC and BC. They will then send these to each other, and combine that with their secrets to form two identical keys, both ABC. Now they can use this key to communicate.

---

### Extra Resources

An excellent video if you want a visual explanation is available here. [Secret Key Exchange - Computerphile - YouTube](https://www.youtube.com/watch?v=NmM9HA2MQGI)

DH Key Exchange is often used alongside RSA public key cryptography, to prove the identity of the person you’re talking to with digital signing. This prevents someone from attacking the connection with a man-in-the-middle attack by pretending to be Bob.

## PGP, GPG and AES

### What is PGP?

PGP stands for Pretty Good Privacy. It’s a software that implements encryption for encrypting files, performing digital signing and more.

---

### What is GPG?

[GnuPG or GPG](https://gnupg.org/) is an Open Source implementation of PGP from the GNU project. You may need to use GPG to decrypt files in CTFs. With PGP/GPG, private keys can be protected with passphrases in a similar way to SSH private keys. If the key is passphrase protected, you can attempt to crack this passphrase using John The Ripper and gpg2john. The key provided in this task is not protected with a passphrase.

The man page for GPG can be found online here [gpg manpage](https://www.gnupg.org/gph/de/manual/r1023.html).

GNU is the name of a large free and open-source software project. GNU originally stood for: GNU's Not Unix

It is a project that creates free software and tools, many of which are commonly used on Linux systems.

So this sentence means the project that develops and maintains GnuPG along with many other free software tools.

---

### What about AES?

AES, sometimes called Rijndael after its creators, stands for Advanced Encryption Standard. It was a replacement for DES which had short keys and other cryptographic flaws.

AES and DES both operate on blocks of data (a block is a fixed size series of bits).

AES is complicated to explain, If you’d like to learn how it works, here’s an excellent video from Computerphile [AES Explained](https://www.youtube.com/watch?v=O4xNJsjtN6E)

---

### Answer the questions below

You have the private key, and a file encrypted with the public key. Decrypt the file. What's the secret word?

`Pineapple`

Import the private key: `gpg --import tryhackme.key`

<img width="376" height="100" alt="image" src="https://github.com/user-attachments/assets/729ca9b1-5741-4dfe-b028-5ba9b347da51" />

Because your private key needs to be available to GPG before GPG can use it for decryption. You are basically telling GPG: "Add this private key to your GPG key collection so you can use it."

Then decrypt the GPG File: `gpg --decrypt message.gpg`

<img width="406" height="57" alt="image" src="https://github.com/user-attachments/assets/fb744af1-0366-48fd-8c12-9046f85d056d" />













