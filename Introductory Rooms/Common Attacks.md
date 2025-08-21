# Common Attacks

## Social Engineering

### What is Social Engineering?

Social Engineering is the term used to describe any cyberattack where a human (rather than a computer) is the target; for this reason, it is sometimes referred to as "People Hacking". 

For example, if an attacker wishes to obtain a victim's password, they could attempt to guess or brute-force the password — or they could simply ask you.

Social engineering attacks can become very complex and often result in an attacker gaining significant control over a target's life — both online and offline. Social engineering attacks are often multi-layered and escalate due to the snowball effect. 

For example, an attacker may start off by obtaining a small amount of publicly available information from a victim's social media presence, which they could then use to get more information from, say, your phone or broadband provider. The information obtained from the second stage could then be used to gain more useful information, then escalate step-by-step to something like the victim's bank account.

### Other Forms of Social Engineering

Charismatic hackers calling your phone company and taking possession of your account is one form of social engineering; however, there are many other types. 

Social engineering is a vast topic, encompassing any attack that relies on tricking humans into giving the attacker access, rather than attacking the technology directly. 

Whilst direct interaction with targets is the most common style of social engineering, other examples include dropping USB storage devices in public (e.g. in company car parks) in the hope that someone (often a company employee) will pick one up and plug it into a sensitive computer. In a similar vein, attackers may leave a "charging cable" plugged into a socket in a public place. In actuality, the cable contains malicious software such as keyloggers or tools to take control of the victim's device.

In short, the limits to social engineering are at the bounds of an attacker's imagination. A good social engineer can (and will) use a plethora of psychological tricks under any plausible context to "hack" their targets.

### Staying Safe from Social Engineering Attacks

In many ways, it is very tricky to stay safe from social engineering as it won't always be you who the attacker is talking to, but rather someone who can give them what they need without your consent (e.g. calling your bank whilst pretending to be you, so as to access your bank account). 

That said, there are still measures you can take to protect yourself from Social Engineering attacks:
- Always make sure to set up multiple forms of authentication, and ensure that providers respect these. For example, set difficult to guess — or otherwise incorrect — answers to security questions (making sure to store the answers somewhere safe!), and make sure that these questions are asked when you try to access accounts over the phone.
- Never plug external media (e.g. USBs/CDs/etc) into a computer that you care about or that is connected to any other devices. Ideally, don't plug the media in at all, and instead give it to your local police for safekeeping.
- Always insist on proof of identity when a stranger calls or messages you claiming to work for a company whose services you use. Where possible, confirm with a known phone number or email address that the call or message you received was legitimate (i.e. use a trusted method to get in contact with the company to confirm). Remember that no legitimate employee will ever ask for your password or other information that protects your account.

### Answer the questions below

What was the original target of Stuxnet?

The Iran Nuclear Programme

## Social Engineering: Phishing

### Overview

Phishing is one of the most common cyber attack types employed by scammers and bad actors, targeting individuals and businesses indiscriminately. 

In many cases, phishing is the initial attack vector used to gain access to a company's infrastructure before performing further attacks against the corporate network. 

### What is Phishing?

Phishing is a sub-section of social engineering. Whereas social engineering is a very general term used to describe any attack that takes advantage of a human rather than a computer system, phishing specifically describes attacks whereby a scammer or other attacker tricks a victim into opening a malicious webpage by sending them a text message, email, or another form of online correspondence. 

Traditionally, "phishing" simply referred to emails; however, in the days of instant messaging, text messages, and voice/video calling, the term has evolved to blanket these other categories. 

These other forms are sometimes referred to individually as "smishing" — phishing over SMS — and "vishing" — phishing over voice chat — respectively.

Phishing messages usually deploy psychological trickery (for example, inducing a false sense of urgency to make victims act rashly) and nearly always involve getting a victim to click on a link to a web application owned by the attacker. The victim is then often asked to enter sensitive information — for example, login details or credit card information — at which point the malicious site stores the information and the attack is complete. 

Alternatively, the victim may inadvertently install malware from the malicious page, thus giving an attacker an entry point into their device and network.

There are three primary types of phishing attacks:

| **Attack Type**   | **Definition (Summary)** |
|-------------------|---------------------------|
| **General Phishing** | Mass attack targeting large groups (e.g., PayPal or Amazon users). Often poorly crafted and easier to detect. |
| **Spearphishing**   | Targeted attack on specific individuals or groups (e.g., company employees). Better crafted and harder to spot. |
| **Whaling**         | Highly targeted attack on high-value individuals (e.g., executives). Extremely well crafted and very difficult to detect. |

Phishing attacks work best when the malicious web page mimics an existing (usually well-known) web page. For this reason, attackers/scammers will usually use one of many freely available tools to simply clone an existing page, which can then be edited at their leisure.

### Identifying Phishing Attacks

Many generic phishing attacks are relatively easy to spot; they frequently have poor grammar and often do not address their victims by name (instead leaving the greetings generic — e.g., "Dear customer"). That said, other instances can be extremely difficult to spot, with some attacks being thorough enough to fool cybersecurity professionals.

The domain name for the malicious site will usually be similar (but never identical) to the domain name used by the legitimate website. 

As a real-world example from 2021, a group of scammers sent out a mass phishing campaign over SMS, mimicking the British Royal Mail service and using the domain name `https://royalmai1.co.uk` (as opposed to `https://royalmail.co.uk`). By exchanging the final "L" for the number one, the scammers were able to successfully register a domain name that looked almost identical to the domain name of their cloned website; this is a very common tactic.

HTML emails can also be used to mask the real domain name in use. For example, the text in the email may be `https://amazon.co.uk`; however, the link actually goes to `https://am4zon.co.uk`. You can see this by hovering your mouse over the link in a desktop application — the real link should appear at the bottom of the screen as in this graphic:

<img width="778" height="318" alt="image" src="https://github.com/user-attachments/assets/f9cbf986-e3f1-4d0d-8d18-8e789ee79846" />

In a similar vein, the "From" email address in an email-based phishing campaign will often be suspicious. Many generic mass phishing campaigns will simply use Gmail addresses — not bothering to use a domain name associated with the company they are spoofing. This is a dead giveaway that the email is suspicious.

The best way to identify a phishing email is simply to keep your eyes open and look for anything suspicious — all but the best will have a mistake somewhere.

### Answer the questions below

What is the flag?

<img width="422" height="179" alt="image" src="https://github.com/user-attachments/assets/dd00fa6f-476b-4b35-93bf-9ca44f2fb75a" />

## Malware and Ransomware

### Overview

Malware (short for "malicious software") can be defined as any software designed to perform malicious actions on behalf of an attacker. There are many different kinds of malware: we will be focussing on generic malware and ransomware specifically in this task.

Once installed, attackers commonly use malware to steal information, cause damage, or execute arbitrary commands on the infected system. 

Malware is often used to perform a set of tasks referred to as "Command and Control" (or C2/C&C). C2 malware connects back to a waiting server and allows an attacker to control the infected system remotely, often incorporating many simple tasks such as keylogging as built-in parts of the malicious software.

### Ransomware

A specialised class of malware: ransomware is used to infect as many systems as possible, encrypting the data on the devices and holding it to ransom. If the victims pay the attackers within a set timeframe (usually via a cryptocurrency such as Bitcoin), the data is theoretically returned.

Ransomware usually spreads by exploiting known vulnerabilities in commonly installed software (e.g. the Microsoft Windows operating system); it can be extremely fast-spreading once an infection begins, and can demand millions in ransom money. 

The goal of a ransomware attack is to infect as many systems as possible, then make as much data inaccessible as possible by encrypting it with a key known only to the attacker. Once the attack is complete, the malware usually displays a window that looks something like this:

<img width="1200" height="897" alt="image" src="https://github.com/user-attachments/assets/1fc75fd1-4013-44ce-88c4-91e40dc4efc2" />

With the ransom paid, the malware may or may not decrypt the data and self-destruct, depending entirely on how nice the attackers are.

### Delivery Methods

There are various ways that an attacker can infect a target with malware — many of these revolve around social engineering or phishing attacks. 

For example, an attacker may send a victim an email containing a Microsoft Word or Excel file that contains a malicious macro (code that is embedded inside the document set to run when a user opens the file). These will not run by default unless the user clicks the "Enable Content" button at the top of the screen to enable macros:

<img width="1052" height="217" alt="image" src="https://github.com/user-attachments/assets/8e25fca4-6156-446d-842f-b6ccda1b1821" />

However, there are situations in which a user may genuinely wish to execute macros, and a good attacker will capitalise on these pretexts to convince the victim to click the button.

A macro is basically a small program or script that automates tasks.

In applications like Microsoft Word or Excel, macros are written in a language called VBA (Visual Basic for Applications). They can be very useful for automating repetitive actions — for example:
- Formatting a document with one click
- Running calculations in a spreadsheet
- Generating reports automatically

Similarly, the attacker may send the file as a compiled `.exe`, a PDF, a `.ps1` PowerShell Script or `.bat` Batch script, an HTML application file (`.hta`), or even a `.js` JavaScript file to be executed by the JavaScript interpreter built into Windows.

In short, there are many different ways and formats in which an attacker can send code to a victim. Once the code is executed, the infection begins.

### Answer the questions below

[Research] What currency did the Wannacry attackers request payment in?

Bitcoin

## Passwords and Authentication

### What Makes A Strong Password?

Current best practices lean more towards length than complexity. For example:

`Vim is _obviously_, indisputably the best text editor in existence!`

By using a passphrase rather than a traditional password, the password is significantly longer whilst still retaining some of the more complex elements — despite not looking quite so obfuscated. This has the advantage of being easier to remember whilst still being incredibly difficult to brute-force.

Ideally, however, you should use long, completely random passwords. For example:

`w41=V1)S7KIJGPN,dII>cHEh>FRVQsj3M^]CB`

These take millions of years to crack and are objectively the most secure option available. The drawback is usability; however, this is largely mitigated by using a password manager.

### What Makes A Weak Password?

People often go for simple passwords that mean something to them, often following one of a few "simple" patterns. For example, a commonly used pattern is a name/location, followed by a year, followed by an exclamation mark. For example:

`Gareth2012!`

Equally, short passwords (especially those that don't contain any non-alphanumeric characters) are weak against brute-force attacks.

Of equal importance to password strength is password reuse. You can have the strongest password in the world, but if you use it across numerous accounts and it gets leaked, an attacker can simply use the same strong password on all affected accounts. Equally, if you find out that your password has been exposed, you will have a lot of work to do changing all of your account passwords!

The industry-standard password storage method is referred to as password hashing. Password hashing (or simply "hashing") involves using complicated mathematical algorithms to take any input and turn it into a unique, fixed-length output in a way that is impossible to reverse. This means that when you sign up, your password will be hashed and stored in the database in a way that stops everyone (including server administrators) from being able to read it!

When you try to sign in, the same algorithm is applied to the password that you supply: if the stored hash matches the hash of the password you are trying to log in with (remembering that the same input will always create the same unique output), then you are considered to have successfully authenticated.

Ideally, every service would hash user passwords with a secure algorithm. Even if the entire database were leaked, the attackers would still need to waste valuable time and computational power attempting to brute-force the (otherwise useless) hashes to find the plaintext passwords. 

This is why it is so important that passwords are long and preferably of a decent level of complexity: the longer the password and the larger the number of potential characters involved, the more power it takes to effectively guess the password input used to generate a hash.

As a worst-case scenario, your plaintext password is either immediately available, or is easy for an attacker to find. If this happens then both your username and password are known to the attacker, allowing them to take over your account or perform "credential stuffing" attacks — using your stolen username and password pair against other services to see if you reused them elsewhere. 

These leaked databases containing credentials frequently appear on the dark web, which leads us to our final point in this section: data exposure notification services.

The largest and most well-known data exposure checker is called [Have I Been Pwned?](https://haveibeenpwned.com/). It exists as a free online service that scours data dumps and catalogues all of the information found, allowing users to enter their email addresses to see if they have been included in any breaches. 

Have I Been Pwned also allows you to add yourself to a notification list, meaning that you will receive an email notifying you if your email address appears in any data breaches.

### Password Attacks

An attacker has a few options when it comes to attacking passwords and authentication systems. Some attacks are entirely local (i.e. working entirely on a device owned by the attacker without interacting with the target service at all), others are remote attacks involving the original server.

Local attacks require a stolen copy of the credentials in question. The attacker will take a file full of stolen usernames/emails and hashed passwords, then use software to effectively try to guess the input that created the hash either using randomly generated sequences of characters (slower but more thorough) or by using a pre-generated wordlist of possible passwords (faster but much more likely to miss things).

Hybrid types are also very widely used; these are when an attacker takes an existing wordlist and mutates it to add new characters, symbols, or random elements. Local password attacks will be demonstrated in the interactive element for this task.

Remote attacks tend to be one of two categories; they either involve attempting to brute-force known usernames by sending requests to the server and seeing what it responds with, or they use known username and password pairs from previous breaches to see if they are valid on the target site — this is the aforementioned credential stuffing.

### Answer the questions below

What is the password?

<img width="402" height="211" alt="image" src="https://github.com/user-attachments/assets/06252d45-449c-4b66-9eab-2d3028b10c60" />







