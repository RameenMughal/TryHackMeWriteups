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

<img width="284" height="86" alt="image" src="https://github.com/user-attachments/assets/873dcba4-b256-4973-9ffc-f3d089ffe6d9" />

Save the file and type `http://random.thm:8090/case/` in the browser to access the website.

<img width="619" height="312" alt="image" src="https://github.com/user-attachments/assets/aa1a312c-3fc1-4329-851a-62d414a1d784" />

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

## Weak or Insufficient Entropy

This technique will cover a scenario where random number generation suffers from poor or insufficient entropy. As discussed earlier, entropy refers to the unpredictability or randomness in a system, often derived from sources like environmental factors (e.g., hardware noise or user interactions). When these entropy sources are weak or insufficient, the generated random values are not truly random and become vulnerable to attacks.

For example, if an encryption key is generated using low-entropy data, such as a `timestamp`, an attacker could use this predictable information to reduce the complexity of finding the key. Similarly, poor entropy sources, like `system clocks` or `predictable user inputs`, can lead to weak randomness in applications.

---

### Practical Scenario

In this scenario, an attacker can exploit the predictability of the entropy source to determine the values produced by the random number generator. We will see how weak entropy in token generation leads to security vulnerabilities. We will be using a vulnerable web app hosted on `http://random.thm:8090/case/`. There is also a mail server configured on `http://random.thm:8090/mail/` where the user will receive emails to reset passwords or log in with a magic link.

<img width="611" height="311" alt="image" src="https://github.com/user-attachments/assets/a87726c8-38b4-48ff-8f78-deffc23fbbed" />

The website provides a login feature and an option for users who have forgotten their password to request a reset link. 

In this case, the user with username `victim` has forgotten their password, and our goal is to understand how password reset tokens are generated and then use the knowledge to achieve account takeover for other users. 

Follow the instructions below to observe the problem first and understand why this approach is insecure.

- Start by visiting the site at `http://random.thm:8090/case/forget_password.php`. Enter the username `victim` in the textbox and click on `Send Reset Link`.
- Next, you will see a message indicating that an email containing a password reset link has been sent.

<img width="663" height="239" alt="image" src="https://github.com/user-attachments/assets/a57e903e-5924-4d80-8676-80367021c681" />

- Let’s break down the server-side logic that produced this token. Below is the code responsible for generating the reset token:

```
$stmt = $db->prepare("SELECT * FROM users WHERE username = :username");

        $stmt->execute([':username' => $user_id]);

        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        if ($user) {

	    $token = $user_id . time();
            $update = $db->prepare("UPDATE users SET reset_token = :token WHERE username = :username");
```

This code first looks for a user in the database whose username matches `$user_id`. It uses a prepared SQL statement to safely search for the username, then gets the user's information using `fetch()`. If the user exists (`if ($user)`), it creates a reset token by joining the username (`$user_id`) with the current time (`time()`). Finally, it prepares an UPDATE query to store this token in the `reset_token` field for that user's account. In simple terms: it finds the user, creates a reset token, and prepares to save that token in the user's database record.

This token is a simple concatenation of the username (in this case, `victim`) and the current timestamp produced by the `time()` function.

- Open the mailbox by logging in with the email `victim@mail.random.thm` and password `Testing@123`. You will see the password reset email like this:

<img width="860" height="155" alt="image" src="https://github.com/user-attachments/assets/124081a7-581c-4093-8330-8882f0f2bb94" />

On the surface, this may seem like a convenient way to generate unique tokens for each password reset request. However, it introduces significant security weaknesses.

---

### Exploitation

- An attacker can exploit the weak entropy in the reset token by visiting the following reset link: `http://random.thm:8090/case/reset_password.php?token={Username}{timestamp_of_token_generation}`.
- Since the token is generated by concatenating the username with the result of the `time()` function, the attacker knows that the `time()` value represents the timestamp when the reset link was created. With this knowledge, the attacker can perform brute force attacks by guessing nearby timestamps, either manually by trying timestamps a few seconds before and after the reset request or through automation using a script.
- Below is a Python script that accepts command-line arguments for the username and timestamp and brute-forces the reset token by attempting timestamps within 5 minutes before the provided timestamp. This website UNIX Timestamp](https://www.unixtimestamp.com/) can be used to get the current UNIX timestamp.
- You can change the time range used to test possible tokens. The value `-300` means 300 seconds (5 minutes) before the current time. If you change it to `-600`, the range becomes 600 seconds (10 minutes). So, a larger negative value means the program checks a longer period of time in the past.

The Python Script is named as `exploit_token.py`

- Once you have created and saved the Python code in the AttackBox, navigate to the web app with the forget password feature to reset the link for the user victim. Once the reset link is generated, visit the website [UNIX Timestamp](https://www.unixtimestamp.com/) to note down the current timestamp, let's say (1786443623).

In the AttackBox, open the terminal and enter the following command to identify the exact token sent to the victim user: `python3 exploit_token.py victim TIMESTAMP`

**Note**: While completing the exercise, make sure to refresh the Unix Time Stamp page to get the latest timestamp.

<img width="256" height="158" alt="image" src="https://github.com/user-attachments/assets/cc4aa461-0099-453b-acd8-0d36bd3be9a0" />

- Once you identify the correct token, you can simply visit the URL `http://random.thm:8090/case/reset_password.php?token=victim{timestamp_of_token_generation}` and update the password.

<img width="595" height="189" alt="image" src="https://github.com/user-attachments/assets/bb2911f5-6df1-4d42-9c5d-42700776abea" />

**Why the Token is Weak**
- **Weak Entropy in Token Generation**: In this case, the system relies on low-entropy sources (username and timestamp), which makes the token predictable. High-entropy tokens are typically generated using secure random number generators (e.g., `random_bytes()`) that produce values with a high degree of unpredictability. Using predictable sources like `time()` does not provide sufficient entropy, making it easy for an attacker to narrow down possible token values. Even though the timestamp changes every second, this predictable increment does not contribute to strong entropy. An attacker could run a brute-force attack using known timestamps within a specific time window (such as within a minute or two from when the token was generated).
- **Small Search Space**: The second major weakness comes from the limited search space. A search space refers to the total number of possible values a token could take. A larger search space makes it exponentially harder for attackers to guess or brute-force the correct token. However, in this case, because the `time(`) function updates every second, the search space for brute-forcing the token is very small. An attacker could simply guess all possible timestamps within a short time range, say within the last 5 or 10 minutes.

---

### Answer the questions below

1. What is the flag value after logging in as the victim user?

Reseting Password as `Testing123` and then loggin in as `victim`:

<img width="1725" height="325" alt="image" src="https://github.com/user-attachments/assets/ed516030-a6fa-4b6e-9dbe-5a0c1d8d8894" />

2. What is the flag value after logging in as the master user?

Doing the same steps as `victim`, first create a reset link for `master` at `http://random.thm:8090/case/forget_password.php` and then copy the UNIX Timestamp.

Run the Python script as `python3 exploit_token master TIMESTAMP`

Reset the password and then loggin in as `master`

3. What is the PHP function used to create the token variable in the code above?

`time()`














