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

<img width="269" height="166" alt="image" src="https://github.com/user-attachments/assets/0735c8f4-653c-4496-9adf-3e8446cd2422" />

Reset the password `http://random.thm:8090/case/reset_password.php?token=master{timestamp_of_token_generation}` and then loggin in as `master`

<img width="1717" height="249" alt="image" src="https://github.com/user-attachments/assets/a20110b3-774b-41b3-9346-263a27f3184f" />

3. What is the PHP function used to create the token variable in the code above?

`time()`

## Predictable Seed in PRNGs

In this task, the focus shifts to cases where a predictable seed is used to initialise PRNGs. If the seed is weak or predictable, an attacker can reproduce the entire sequence of random numbers, leading to severe vulnerabilities in systems that rely on these random values.

An example of the impact of predictable seeding is in `CAPTCHA` systems, where the random value determining the CAPTCHA challenge will be generated to detect a bot activity. If the seed used to initialise the PRNG is predictable, an attacker could predict the CAPTCHA values ahead of time, allowing them to bypass the CAPTCHA and access restricted areas of the application without solving it.

This issue also manifests in systems like lottery or game applications, where PRNGs determine the outcome of random draws. When these generators are seeded with predictable values, such as timestamps, attackers can manipulate the system by predicting the outcome, ensuring they win consistently. By exploiting the predictable PRNG seed, the attacker can reverse-engineer or replicate the same random sequence, breaking the system's fairness.

---

### Practical Scenario

In this scenario, we will explore how using predictable seeds to generate tokens in a magic link login system can lead to account takeover. 

The token inside this link is created using PHP's `mt_rand()` function. The problem is that `mt_rand()` is not designed for security when used to create login tokens. In this case, the system uses predictable information, such as the CRC32 value of the user's email, together with a constant value to create the seed. If an attacker can figure out how the seed is created, they may be able to predict the token that the website will generate. If they can predict a valid token for another user, they could potentially log in as that user and take over the account.

CRC32 stands for Cyclic Redundancy Check 32-bit. It is a function that takes some data, such as an email address, and produces a 32-bit number called a checksum.

The important thing is that CRC32 is not encryption. It is mainly used to detect whether data has been changed or corrupted.

**Analysis of Magic Link Feature**

- Start by navigating the web application at `http://random.thm:8090/case/` and click `Login with Magic Link`.

<img width="612" height="268" alt="image" src="https://github.com/user-attachments/assets/b6d30d5d-8d92-4132-ae87-1bd565047202" />

- The website allows users to log in through a magic link sent to their email. For this demonstration, use the email: `magic@mail.random.thm`. Enter this email address into the provided input field and click `Send Magic Link`.

<img width="700" height="183" alt="image" src="https://github.com/user-attachments/assets/dd4b701f-fbce-413c-970d-66c6e8f1f793" />

The magic link contains a token allowing users to log in without entering a password.

- Open the mailbox by logging in with the email `magic@mail.random.thm` and password `Testing@123`. You will see the Login with Magic Link email like this:

<img width="862" height="158" alt="image" src="https://github.com/user-attachments/assets/cd9c69fe-0ae6-40c1-a51f-12bfe514252d" />

- In the victim's inbox, you will see the magic link email. The magic link will look like this: `http://random.thm:8090/case/magic_link_login.php?token=MTEzNTUwODU0MQ==`
- The token (`MTEzNTUwODU0MQ==`) is a base64-encoded version of a random number generated using PHP’s `mt_rand()` function.

**Analysis of Server Side Code**

Now that we have captured the magic link token from the victim’s email, it's essential to understand how this token was generated on the server. The server uses the PHP’s mt_rand() function to generate a random number that forms the basis of the token. Below is the server-side code that generates the token:

```
mt_srand(CONSTANT_VALUE + crc32($email));

$random_number = mt_rand();
$token = base64_encode($random_number);
```

This code generates a token in a few steps:
- `mt_srand(CONSTANT_VALUE + crc32($email));`: This sets the starting seed for the random number generator. The seed is made from a constant value plus the CRC32 value of the user's email.
- `$random_number = mt_rand();`: `mt_rand()` generates a random-looking number based on that seed.
- `$token = base64_encode($random_number);`The generated number is converted into Base64 format so it can be used as a token.

So, simply: Email → CRC32 → Seed → `mt_rand()` → Random Number → Base64 → Token

The security problem is that the seed depends partly on the email, which is usually predictable. Therefore, if someone can determine the seed, they may be able to reproduce the same `mt_rand()` output and predict the token.

**Decoding the Token**

To proceed with the attack, we need to decode the Base64 token and retrieve the original random number generated by the server. This number is the direct output of PHP’s `mt_rand()` function, which was seeded with a predictable value. You can use an online tool like [Base64 Decode](https://www.base64decode.org/) to quickly decode the token. Simply paste the Base64-encoded token (`MTEzNTUwODU0MQ==`) into the input field, and the decoded output will be displayed.

Once we have decoded the Base64 string, we are left with the original random number generated by `mt_rand()`, which, in our case, is `1135508541`. This number is crucial for the next step in the attack, as it is the output of a PRNG that was seeded using a dynamic value.

---

### Exploitation

The primary tool we’ll use to exploit this vulnerability is [`php_mt_seed`](https://www.openwall.com/php_mt_seed/). This tool is specifically designed to crack the seed of PHP’s `mt_rand()` function based on the outputs of the random number generator. Once you provide `php_mt_seed` with a `mt_rand()` output, it calculates possible seed values that could have produced that output. 

You can learn detailed technical explanations and maths about the tool here [Breaking PHP's `mt_rand()` Function](https://blog.lexfo.fr/php-mt-rand-prediction.html).

You can download the tool of latest version here in the main page [Download php_mt_seed](https://www.openwall.com/php_mt_seed/)

The next step with the tool setup is to crack the seed based on the decoded random number from the token. We know that the decoded random number from the base64 token was `1135508541`. This number is the direct output of `mt_rand()`. To find the seed, run the following command in the AttackBox, which takes a little over 5 minutes to show the result (You can skip it as well):

<img width="320" height="164" alt="image" src="https://github.com/user-attachments/assets/0a7926e0-2b7b-4cb6-b412-5454da06c239" />

`php_mt_seed` will output a list of possible seeds that could have generated the random number `1135508541`. This may take up to a few minutes, depending on the range of possible seeds. When using `php_mt_seed`, the tool generates multiple possible seeds because different seeds can produce the same initial random number. This happens due to the way `mt_rand()` is initialised. To accurately identify the correct seed, each one must be tested in the environment individually. In our case, the random number `1135508541` was generated through the seed `970732804`.

Once you have identified the correct seed, you can identify the constant value that the server used to prepare the seed. All you need to do is subtract the CRC32 value of `magic@mail.random.thm` from the identified seed. You can use this [CyberChef](https://gchq.github.io/CyberChef/) to get the exact value.

<img width="551" height="296" alt="image" src="https://github.com/user-attachments/assets/10e5753c-ca01-451a-bf8f-da6303f59a12" />

First put "CRC Checksum" and choose the Algorithm "CRC-32", Then choose "From Base" and select Radix 16 value.

After getting the CRC32 value `970731467`, if we subtract it from the identified seed value `970732804`, we will get the constant value, which is `1337` in this case. 

An attacker only needs the target’s email address to log in as someone else. Once they have the email, the attacker can calculate the CRC32 of the email, add `1337` to it, and use the resulting seed with `mt_srand()`. This allows the attacker to predict the exact token generated for the target, enabling them to bypass authentication and log in as that user without knowing the password. 

In the AttackBox copy and paste the following PHP code to a file called `magic_link_login.php` and then use the command `php -S 0.0.0.0:8181` to utilise PHP's built-in web server for us to access the script. The script will generate 10 tokens based on a seed comprising a constant value and an email address. The script will accept the constant value and email as input and generate the corresponding tokens. 

<img width="457" height="24" alt="image" src="https://github.com/user-attachments/assets/0fe018a9-24d4-42a1-9d82-c0024a36ae25" />

Then navigate to your own localhost to get the Tokens `http://127.0.0.1:8181/magic_link_login.php?email=magic@mail.random.thm&constant=1337`

<img width="530" height="175" alt="image" src="https://github.com/user-attachments/assets/e07b86b0-6ee8-4641-b5b9-36e9bc4868e6" />

<img width="597" height="95" alt="image" src="https://github.com/user-attachments/assets/eb613c8d-b6aa-442a-8989-59ad5a3399ff" />

Now that you have the predicted token, you can log in as the target user. Simply visit the magic link URL `http://random.thm:8090/case/magic_link_login.php?token={predicted_token}` with the predicted token to log in without knowing the password.

---

### Answer the questions below

1. What is the flag value after logging in as magic@mail.random.thm?

<img width="1710" height="256" alt="image" src="https://github.com/user-attachments/assets/3ddacbbd-abd2-444f-aae4-b9362c733bec" />

2. What is the flag value after logging in as hr@mail.random.thm?

Going to the `Login with Magic Link` page then enter `hr@mail.random.thm` to send the magic link to this email.

Login the mail page `http://random.thm:8090/mail/` by entering `hr@mail.random.thm` and `Testing@123` as email and password, you will see the email of Magic Link:

<img width="862" height="154" alt="image" src="https://github.com/user-attachments/assets/cf61f765-c78a-40e7-8f0c-b6509c3a1db8" />

Decoding this base64 `MjU1MjEwNzUx` with [Base64 Decode](https://www.base64decode.org/) which gives us `255210751` which is the output of the PRNG seeded with the dynamic value, we need to find the dynamic value.

Using the `php_mt_seed` command to get the possible seed values that got the value `255210751`

Command: `./php_mt_seed 255210751`

<img width="322" height="206" alt="image" src="https://github.com/user-attachments/assets/3e7de729-fa83-4e2d-9238-33c7ade01be7" />

To identify the correct seed, we will first calculate the CRC32 value of email `hr@mail.random.thm` from [CyberChef](https://gchq.github.io/CyberChef/) which is `3226467716`:

<img width="770" height="279" alt="image" src="https://github.com/user-attachments/assets/d2a4d2ab-0d32-41c7-adc6-6828d6666a4e" />

Now we will compare these both values to identify the correct seed.

As we know that the application uses `mt_srand(CONSTANT_VALUE + crc32($email));` meaning `seed = constant + CRC32(email)` but we don't know the constant yet so we can move the equation like `constant = seed - CRC32(email)` to calculate the constant.

Following is the table where Candidate seed is minused with the CRC32 value of email:

| Candidate seed | Calculated constant |
| -------------: | ------------------: |
|      570783581 |         -2655686135 |
|     1664709063 |         -1561758653 |
|     3104005235 |          -122622481 |
| **3226469053** |            **1337** |

The `1337` matches like the constant of above question so this is most likely the correct constant.

So correct seed is `3226469053`

Run the `magic_link_login.php` by command `php -S 0.0.0.0:8181` then check in the browser `http://127.0.0.1:8181/magic_link_login.php?email=hr@mail.random.thm&constant=1337`

<img width="488" height="167" alt="image" src="https://github.com/user-attachments/assets/5a79dede-cb63-42fc-83ef-04cc6bba1dc4" />

Then access the dashbaord by `http://random.thm:8090/case/magic_link_login.php?token={predicted_token}`

<img width="1717" height="247" alt="image" src="https://github.com/user-attachments/assets/780ca4b4-0663-4908-9047-428940e645f8" />

**Note**: If it says Invalid Magic Link then send the Magic Link again.

4. What is the PHP function used to seed the RNG in the code above?

`mt_srand`

---

## Mitigation Measures

When discussing best practices for identifying and mitigating insecure randomness, it's important to address both pentesters and secure coders, as their perspectives and responsibilities differ. Here's a breakdown of the best practices for each:

### Pentesters

- **Identify Weak Randomness in Code**: During code reviews or application assessments, look for the use of weak random number generators like `mt_rand()` or `rand()`, especially when they generate security-sensitive values like session tokens or password reset links.
- **Reverse Engineer Predictable Tokens**: Attempt to exploit predictable randomness by reverse-engineering the seed used in PRNGs. Tools like `php_mt_seed` can help pentesters demonstrate how predictable tokens (e.g., magic links) can be recreated. Test for weak or predictable seeds like timestamps, IP addresses, or user-specific values.
- **Test Token Exhaustion**: If Cryptographically Secure Pseudorandom Number Generators (CSPRNGs) are not used, run brute-force or replay attacks against generated tokens, session IDs, or other randomness-dependent features. Ensure that tokens are not guessable or predictable.

---

### Secure Code Developers

- **Use Cryptographically Secure PRNGs**: Always use CSPRNGs, such as `random_bytes()` or `openssl_random_pseudo_bytes()` in PHP or `java.security.SecureRandom` in Java. These CSPRNGs are designed to generate unpredictable values suitable for security-critical applications like session tokens, API keys, or password reset tokens. 
- **Avoid Predictable Seed Values**: Never use predictable values like the current `timestamp`, `IP address`, or `process ID` for seeding random number generators. These values can be easily guessed or reverse-engineered by attackers. Instead, use entropy from cryptographic sources or system-provided randomness (e.g., `/dev/urandom` in Linux).
- **Regenerate Randomness for Every Critical Operation**: Avoid reusing random values or seeds across multiple requests or users. Regenerate fresh randomness for each operation that requires secure tokens, such as session management, password resets, or magic links.
- **Use Strong Algorithms for Key Generation**: When generating cryptographic keys, always use secure key generation functions that derive keys from strong sources of entropy. For example, in PHP, you can use `openssl_pkey_new()` for RSA key generation, which relies on secure randomness.

---

### Answer the questions below

Which of the following can be considered as a weak seed value? Write the correct letter only.

a) Timestamp

b) IP Address

c) 6-digit constant value

d) All of the above

d
