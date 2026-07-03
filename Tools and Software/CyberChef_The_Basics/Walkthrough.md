# CyberChef: The Basics

Room: [CyberChef: The Basics](https://tryhackme.com/room/cyberchefbasics)

Room Prerequisites: 
1. [Cryptography Basics](https://tryhackme.com/room/cryptographybasics)
2. [Networking Concepts](https://tryhackme.com/room/networkingconcepts)
3. [Web Application Basics](https://tryhackme.com/room/webapplicationbasics)

<img width="940" height="190" alt="image" src="https://github.com/user-attachments/assets/da970afd-e953-445d-8621-f36452df1780" />

## Introduction

CyberChef is a simple, intuitive web-based application designed to help with various “cyber” operation tasks within your web browser. Tasks range from simple encodings like XOR or Base64 to complex operations like AES encryption or RSA decryption. CyberChef operates on recipes, a series of operations executed in order.

## Accessing the Tool

There are different ways to access and run CyberChef. Let's check the two most convenient methods!

---

### Online Access

All you need is a web browser and an internet connection. Then, you can click this [Website](https://gchq.github.io/CyberChef/) to open CyberChef directly within your web browser.

---

### Offline or Local Copy

You can run this offline or locally on your machine by downloading the latest release file from this [GitHub Release](https://github.com/gchq/CyberChef/releases). This will work on both Windows and Linux platforms. As best practice, you should download the most stable version.

## Navigating the Interface

CyberChef consists of four areas. Each consists of different components or features.

These are the following areas:
1. Operations
2. Recipe
3. Input
4. Output

<img width="2984" height="1660" alt="image" src="https://github.com/user-attachments/assets/d3b83621-97a0-4dba-9646-b0eae08c5711" />

---

### The Operations Area

A categorized collection of CyberChef operations, with a search feature for quickly finding and using specific functions.

#### Common CyberChef Operations

| Operation | Description | Example |
|-----------|-------------|---------|
| **From Morse Code** | Translates Morse Code into uppercase alphanumeric characters. | `- .... .-. . .- - ...` → `THREATS` |
| **URL Encode** | Encodes special characters into percent-encoding for URLs. | `https://tryhackme.com/r/room/cyberchefbasics` → `https%3A%2F%2Ftryhackme%2Ecom%2Fr%2Froom%2Fcyberchefbasics` |
| **To Base64** | Encodes raw data into a Base64 ASCII string. | `This is fun!` → `VGhpcyBpcyBmdW4h` |
| **To Hex** | Converts text into hexadecimal bytes. | `This Hex conversion is awesome!` → `54 68 69 73 20 48 65 78 20 63 6f 6e 76 65 72 73 69 6f 6e 20 69 73 20 61 77 65 73 6f 6d 65 21` |
| **To Decimal** | Converts input text into ASCII decimal values. | `This Decimal conversion is awesome!` → `84 104 105 115 32 68 101 99 105 109 97 108 32 99 111 110 118 101 114 115 105 111 110 32 105 115 32 97 119 101 115 111 109 101 33` |
| **ROT13** | Applies a Caesar cipher with a rotation of 13 characters. | `Digital Forensics and Incident Response` → `Qvtvgny Sberafvpf naq Vapvqrag Erfcbafr` |

---

### The Recipe Area

The main workspace where you add, arrange, and configure operations. You can drag operations into this area and customize their arguments and options to achieve the desired output.

Features include the following:
- `Save recipe`: This feature allows the user to save selected operations.
- `Load recipe`: Allows the user to load previously saved recipes.
- `Clear Recipe`: This feature will enable users to clear the chosen recipe during usage.

The bottom part of the image above is the `BAKE!` button. This processes the data with the given recipe.

Additionally, you can tick the `Auto Bake` checkbox. This feature allows users to automatically cook using the selected recipe without manually clicking `BAKE!` every time.

---

### Input Area

The input area provides a user-friendly space where you can easily input text or files by pasting, typing, or dragging them to perform operations.

Additionally, it has the following features:
1. `Add a new input tab`: This is where an additional tab is created for the user to use different values from the previous tab.
2. `Open folder as input`: This feature allows users to upload a whole folder as input value.
3. `Open file as input`: This feature allows the user to upload a file as its input value.
4. `Clear input and output`: This feature allows the user to clear any input values inserted and the corresponding output value.
5. `Reset pane layout`: This feature brings the tool's interface to its default window sizes.

---

### Output Area

The output area is a visual space that showcases the data processing results. It neatly presents the outcomes of any manipulations or transformations you have applied to the input data, allowing for a clear and intuitive display of the processed information.

Features include:
1. `Save output to file`: This feature allows the users to save the result into a .dat file.
2. `Copy raw output to the clipboard`: This feature allows users to copy raw output directly to their clipboard, allowing them to quickly copy the results for use in other applications or documents.
3. `Replace input with output`: This feature allows users to quickly overwrite the input data based on the operations' results.
4. `Maximise output pane`: This feature brings the tool's interface to its default window sizes.

---

### Answer the questions below

1. In which area can you find "From Base64"?

Operations 

2. Which area is considered the heart of the tool?

Recipe

## Before Anything Else

Let's have a quick overview of the thought process when using CyberChef! This process consists of four different steps:

<img width="1140" height="180" alt="image" src="https://github.com/user-attachments/assets/571a33cf-c9ff-409b-b959-a4c5363bdfe9" />

Let's discuss each step further.
1. Set an Objective – Define what you want to achieve (e.g., decode a suspicious string).
2. Provide Input – Paste or upload the data into the input area.
3. Choose Operations – Select the appropriate operations (e.g., ROT13, Base64, Base85) based on your analysis.
4. Check the Output – Verify if the result meets your objective. If not, try different operations and repeat the process.

---

### Answer the questions below

1. At which step would you determine, "What do I want to accomplish?

1

## Practice, Practice, Practice

We will explore some of this task's most commonly used operation categories. Recognizing which category to utilize can enhance your ability to use the tool more efficiently and effectively.

### Extractors

<img width="896" height="229" alt="image" src="https://github.com/user-attachments/assets/227c59ce-010d-444d-9f87-2701ade0a7a4" />

The `Extract IP addresses` will extract any valid IPv4/6 address from any given input.

The `Extract email addresses` extracts any strings and characters with this format, anything@domain[.]com. Examples of domains include hotmail.com, google.com, tryhackme.com, and yahoo.com

---

### Date and Time

<img width="896" height="151" alt="image" src="https://github.com/user-attachments/assets/9a9c87d6-df44-45df-b407-12c5572607f1" />

A UNIX timestamp is a 32-bit value representing the number of seconds since January 1, 1970 UTC (the UNIX epoch). 

To convert "Fri Sep 6 20:30:22 +04 2024" into a UNIX Timestamp, use the operations `To UNIX Timestamp`, where the result would be `1725654622`. If you wish to convert it back to a more readable format, you can use `From UNIX Timestamp`.

---

### Data Format

| Operation | Description | Example |
|-----------|-------------|---------|
| **From Base64** | Decodes a Base64-encoded string back into its original readable text. | `V2VsY29tZSB0byB0cnloYWNrbWUh` → `Welcome to tryhackme!` |
| **URL Decode** | Converts URL-encoded characters (percent-encoded values) back into their normal form. | `https%3A%2F%2Fgchq%2Egithub%2Eio%2FCyberChef%2F` → `https://gchq.github.io/CyberChef/` |
| **From Base85** | Decodes text that has been encoded using Base85. It is similar to Base64 but stores data more efficiently as it can represent the same amount of binary data using few characters. | `BOu!rD]j7BEbo7` → `hello world` |
| **From Base58** | Decodes Base58-encoded data. Base58 removes confusing characters like `0`, `O`, `I`, and `l` to make the text easier for humans to read. | `AXLU7qR` → `Thm58` |
| **To Base62** | Encodes text using Base62, which uses letters and numbers to create shorter encoded strings. | `Thm62` → `6NiRkOY` |

Operations such as `Base(64, 85, 58, 62)` are known as **base encodings**. Base encoding takes binary data (strings of 0s and 1s) and transforms it into a text-based representation using a specific set of ASCII (American Standard Code for Information Interchange) characters.

If you want to view the complete ASCII Table, please refer to this page [ASCII Table](https://www.ascii-code.com/).

---

### Convert THM String to Base64 String

Our example would be to encode the letters "THM". 

#### Step 1: Convert To Binary and Merge(Manually)

Based on our table from the ASCII Table, `T = 01010100`, `H=01001000`, `M = 01001101`. 

Next, concatenate these binaries and make sure they have 24 characters. You should have `010101000100100001001101`

#### Step 2: Divide and Convert to Decimal(Manually)

Separate `010101000100100001001101` into 6 characters each. You should have `010101` `000100` `100001` `001101`. These are 6-bit characters; we should have four instances of this now. We need to convert each instance to Decimal. Let's convert, then!

Result is `010101 = 21`, `000100 = 4`, `100001 = 33` and `001101 = 13`

#### Step 3: Convert to Base64 (Manually)

Now that we have the Numbers from the previous step, which are 21, 4, 33, and 13, let's look for the equivalent characters from our table below. This table represents a base64 index table.

You can check Table from here: [The Base64 Alphabets](https://www.garykessler.net/library/base64.html)

Result is `21 = V`, `4 = E`, `33 = h` and `13 = N`

Combine these characters, and you should have the equivalent of "THM" in base64 format. The answer would be `VEhN`.

---

### URL Decode

This works by converting the percent-encoded characters back to their raw values. 

For a reference of these values, you can check the page [Percent Encoding](https://en.wikipedia.org/wiki/Percent-encoding). 

Note that the default character set in HTML5 is UTF-8. Check the table below for a quick overview of what we can typically see in a URL.

<img width="895" height="296" alt="image" src="https://github.com/user-attachments/assets/b1702f4b-85f5-4c0f-a2c3-ecd579061530" />

---

### Answer the questions below

1. What is the hidden email address?

`hidden@hotmail.com`

<img width="959" height="345" alt="image" src="https://github.com/user-attachments/assets/82dee07c-7f54-49e8-9ac6-26832494a0bd" />

2. What is the hidden IP address that ends in .232?

`102.20.11.232`

<img width="959" height="350" alt="image" src="https://github.com/user-attachments/assets/2ddb37d7-8e08-4412-9d2d-d07ed30d056a" />

3. Which domain address starts with the letter "T"?

`TryHackMe.com`, Use the `Extract Domains` Operation

<img width="959" height="353" alt="image" src="https://github.com/user-attachments/assets/bbece33b-d1c1-46f0-863e-d1f258f86012" />

4. What is the binary value of the decimal number 78?

`01001110`, First use `From Decimal` to convert `78` to `N` and then use `To Binary` to convert `N` to its binary value

<img width="772" height="347" alt="image" src="https://github.com/user-attachments/assets/3e7b9c47-5cc5-4125-a628-c141f2b5f543" />

5. What is the URL encoded value of `https://tryhackme.com/r/careers`?

`https%3A%2F%2Ftryhackme%2Ecom%2Fr%2Fcareers`

<img width="959" height="350" alt="image" src="https://github.com/user-attachments/assets/483b4521-5458-4269-b068-d46a628fd1c4" />

## Your First Official Cook

### Answer the questions below

1. Using the file you downloaded in Task 5, which IP starts and ends with "10"?

`10.10.2.10`, Use the `Extract IP Addresses`

<img width="958" height="353" alt="image" src="https://github.com/user-attachments/assets/857ac47a-cbe0-4f03-bc90-1ce686c318d8" />

2. What is the base64 encoded value of the string "Nice Room!"?

`TmljZSBSb29tIQ==`, Use the `To Base64`

<img width="958" height="335" alt="image" src="https://github.com/user-attachments/assets/812bbd37-9dca-40a8-9a8e-3c069ec10d58" />

3. What is the URL decoded value for `https%3A%2F%2Ftryhackme%2Ecom%2Fr%2Froom%2Fcyberchefbasics`?

`https://tryhackme.com/r/room/cyberchefbasics`, use the `URL Decode`

<img width="959" height="340" alt="image" src="https://github.com/user-attachments/assets/809c410e-38a1-468d-97e0-7fe226dea008" />

4. What is the datetime string for the Unix timestamp `1725151258`?

`Sun 1 September 2024 00:40:58 UTC`, Use `From Unix Timestamp`

<img width="957" height="343" alt="image" src="https://github.com/user-attachments/assets/b83339e6-ac41-4633-b0a6-da539eaa3534" />

5. What is the Base85 decoded string of the value `<+oue+DGm>Ap%u7`?

`This is fun!`, use the `From Base85`

<img width="959" height="347" alt="image" src="https://github.com/user-attachments/assets/f502b2fd-8274-4175-8318-b30bd3b6c75a" />



















