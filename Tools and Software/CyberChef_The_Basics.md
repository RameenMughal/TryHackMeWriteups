# CyberChef: The Basics

Room: [CyberChef: The Basics](https://tryhackme.com/room/cyberchefbasics)

Room Prerequisite: [Cryptography Basics](https://tryhackme.com/room/cryptographybasics)

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



