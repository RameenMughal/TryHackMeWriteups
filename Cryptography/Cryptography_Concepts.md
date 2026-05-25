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

Nobody tries to hide how locks work to make them secure. Security comes from keeping your key private and this same principle applies to cryptography. Algorithms are usually public and tested by experts worldwide. The security comes from keeping keys secret.

To put it more practically, Alice wants to send Bob a secret letter, but it must go through the public postal system, where anyone could open it and read it.

Here's what she does:
- She writes her message (the plaintext) on paper.
- She puts the letter in a sturdy lockbox.
- She locks it with a padlock using her key.
- She sends the locked box (the ciphertext) through the mail.

When Bob gets the box, he uses his copy of the same key to unlock it and read the message. Anyone who intercepts the box along the way sees a locked metal box. Without the key, it's useless. The message stays private.

That's symmetric encryption in a nutshell: one key locks the box, the same key unlocks it.

---

### Plaintext versus Ciphertext

Now, how does this look when dealing with text or data? Say Alice wants to send: `HELLO`

That's the plaintext—the readable message.

Alice uses an algorithm and a secret key to scramble it. After scrambling, it becomes: `KHOOR`

That's the ciphertext. To anyone without the key, `KHOOR` is meaningless. The key point: ciphertext should look like random nonsense to anyone who doesn't have the key.

Bob receives `KHOOR`, uses the same key and algorithm, and unscrambles it back to `HELLO`.

---

### The Caesar Cipher: Algorithm Plus Key

The Caesar cipher is named after Julius Caesar, who reportedly used this technique over 2000 years ago to send military messages. 

#### How It Works

The Caesar cipher shifts each letter in your message by a fixed number of positions in the alphabet. That fixed number is your key.

Let's say the key is 3:

- `A` shifts forward 3 spots to become `D`
- `B` becomes `E`
- `C` becomes `F` and so on.
- `X` becomes `A` (it wraps around to the start)
- `Y` becomes `B`
- `Z` becomes `C`

If Alice wants to encrypt `HELLO` with a key of 3:
- `H` → `K`
- `E` → `H`
- `L` → `O`
- `L` → `O`
- `O` → `R`
  
So `HELLO` becomes `KHOOR`.

To decrypt `KHOOR`, Bob shifts each letter backwards by 3:
- `K` → `H`
- `H` → `E`
- `O` → `L`
- `O` → `L`
- `R` → `O`

He gets `HELLO` again.

With the Caesar cipher:
- The algorithm (shift each letter by some number) is completely public. Everyone can know how it works.
- The key (the number 3 in our example) is what's secret. Only Alice and Bob know this number.

The Caesar cipher is not secure and is never used in real systems. It's way too easy to compromise and decrypt messages. 

Real algorithms like AES (Advanced Encryption Standard) are vastly more complex and secure. But they follow the same basic idea: algorithm + key + plaintext → ciphertext.

---

### Symmetric Encryption Explained

The Caesar cipher is an example of symmetric encryption. This means that:
- The same key encrypts (locks) and decrypts (unlocks) the message.
- Both sender and receiver need a copy of that key.
- The key has to stay secret from everyone else.

Some of the benefits of using symmetric encryption are:
- It's fast. Symmetric algorithms can churn through huge amounts of data really quickly.
- =It's efficient. Perfect for encrypting files, hard drives, and network traffic where speed matters.

However, there's a catch to this efficiency: How do Alice and Bob share that key safely in the first place?

If they send the key over the internet in plain view, an eavesdropper can grab it. Then that eavesdropper can decrypt every future message.

You might think, "Just encrypt the key!",  but then you'd need another key to encrypt that key, and then another key for that key, and you see the problem. Infinite regress.

This is called the key distribution problem, and it's the Achilles' heel of symmetric encryption when used alone.

---

### Answer the questions below

1. What's the flag you received after completing all levels of the Secret Message Rescue game?

<img width="948" height="336" alt="image" src="https://github.com/user-attachments/assets/78b31230-838b-4b2f-a5cc-aa11f7c68874" />

2. Using the Caesar cipher with a key of 5, what does `CYBER` become when encoded? (Uppercase, no spaces.)

`HDGJW`

3. Using the Caesar cipher, find the correct key and decode the following secret message: `FVZCYR PNRFNE PVCURE`.

`SIMPLE CAESAR CIPHER`

## Sharing Keys Safely: Asymmetric Encryption

### The Key Distribution Problem

In the last task, we saw how symmetric encryption works. Alice and Bob use the same key for both encryption and decryption. It's fast and efficient.

However, we also hit a wall: how do they share that key safely in the first place?

If they send it in plaintext, an attacker grabs it. If they encrypt the key, they need another key, which brings us right back to the same problem.

Enter asymmetric encryption.

---

### Two Keys Instead of One

Asymmetric encryption uses two mathematically linked keys:
- A **public key** that anyone can know and use.
- A **private key** that only one person keeps secret.

Here's the clever part:
- If you encrypt something with someone's public key, only their private key can decrypt it.
- If you encrypt something with your private key, anyone with your public key can decrypt it (this is primarily used for digital signatures).

The two keys are connected by some serious maths, but it would take an ordinary computer hundreds or even thousands of years to recover the private key from the public key. This computational difficulty is what makes asymmetric encryption secure.

When Alice wants to send Bob a secret:
- Alice finds Bob's public key. This isn't a secret—Bob can post it on his website or email it around.
- Alice writes her message, encrypts it with Bob's public key, and sends it.
- Only Bob can decrypt it because he is the only one with the private key.

Even if an attacker intercepts the encrypted message, they can't decrypt it without Bob's private key.

---

### Solving the Key Distribution Problem

With asymmetric encryption, Alice and Bob don't need to share a secret key beforehand. A simple flow of events can be as follows:
- Bob creates a public key and a private key on his computer. He keeps the private key to himself and shares the public key with the world.
- Alice grabs Bob's public key (maybe from his website or a key server).
- Alice encrypts her message using Bob's public key and sends it off.
- Bob receives it and decrypts it using his private key.

At no point did they need to exchange a key over the network secretly. The only key that travelled publicly was Bob's public key, which isn't secret by design. That's the solution to the key distribution problem.

### Real-world Use: HTTPS

The most common everyday use of asymmetric encryption is in HTTPS—the secure protocol you use whenever you see that padlock in your browser.

Here's what happens when you visit `https://google.com`:
- Your browser requests the website's public key.
- The website sends back its public key wrapped in a certificate.
- Your browser and the website use asymmetric encryption to agree on a shared secret (a symmetric key) without anyone else being able to see it.
- From there on, they switch to fast symmetric encryption using that shared secret for the rest of the session.

This combo is sometimes called a hybrid approach:
- Asymmetric encryption solves the problem of key distribution.
- Symmetric encryption handles the heavy lifting because it's way faster.

You might wonder: how does Alice know the public key really belongs to Bob, and not to an attacker pretending to be Bob? That's where certificates come in.

A certificate is a digital document that:
- Contains someone's public key.
- States who that key belongs to (like example.com).
- A trusted authority digitally signs it, called a Certificate Authority (CA).

If something's off—perhaps the certificate has expired or was signed by an untrusted authority—your browser displays a warning and may refuse to connect.

---

### Viewing a Certificate In Your Browser

You can peek at the certificate for any HTTPS site right now. These steps can guide you to view certificates:
- Visit any HTTPS site (try `https://www.tryhackme.com`).
- Click the padlock icon in the address bar.
- Look for something like "Certificate", "Connection is secure", or "View certificate".
- A window opens showing details like:
  - Issued to: The website's domain.
  - Issued by: The CA that signed it.
  - Valid from / Valid until: The certificate's expiration dates.

In practice, real systems use both:
- Asymmetric encryption initiates a connection and securely shares a symmetric key.
- Symmetric encryption takes over for the remainder of the session to efficiently handle data.

This is how HTTPS, VPNs, and encrypted messaging apps all operate.

---

### Answer the questions below

1. In asymmetric encryption, which key stays secret?

Private Key

2. With asymmetric encryption, Alice can encrypt a message using Bob's public key, and only Bob's private key can decrypt it. Yay or Nay?

Yay

3. What problem does asymmetric solve that symmetric cannot?

Key Distribution

4. After initial asymmetric exchange in HTTPS, what encryption type handles bulk data?

Symmetric

## Conclusion

### What We've Covered

In this room, we explored the basics of cryptography and its role in protecting confidentiality—one of the three pillars of the CIA Triad. We covered the core ideas:
- Plaintext is what you can read. Ciphertext is scrambled gibberish.
- A key is the secret that controls scrambling and unscrambling.
- An algorithm is the public method for using the key.

We looked at two flavours of encryption:
- Symmetric encryption uses a single key for both encryption and decryption. It's fast and efficient, but you need a secure way to share that key. We used the Caesar cipher to see how this works.
- Asymmetric encryption uses two linked keys: a public key that anyone can use and a private key that only one person keeps. This solves the key distribution problem and powers the initial handshake for HTTPS connections.

We also saw how real systems combine both types:
- Asymmetric encryption sets up a shared key at the start.
- Symmetric encryption handles the actual data because it's faster.

Cryptography is one of the most critical tools in a defender's arsenal. It protects confidentiality and integrity, and it's the backbone of almost every secure system you use online. But it's not magic. It's one layer in a much bigger security picture that includes:
- Strong password practices.
- Secure key storage.
- User awareness and training.
- Regular software updates.
- Monitoring and incident response.



