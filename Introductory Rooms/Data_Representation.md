# Data Representation

Room: [Data Representation](https://tryhackme.com/room/datarepresentation)

<img width="1892" height="395" alt="image" src="https://github.com/user-attachments/assets/c10c3281-18c7-4a2f-a4c5-5f2344e14c31" />

## Introduction

Without giving it much thought, we use the decimal system, where the digits range from 0 to 9. Computers, on the other hand, are limited to two digits: 0 and 1.

## Representing Colors

### Our First Eight Colors

Let’s say that each of the three (red, green and blue) colors can be either on or off, i.e., each has two states.
- The red light can be either on or off
- The green light can be either on or off
- The blue light can be either on or off

These states give us 2 × 2 × 2 = 8, that’s eight different colors.

If a computer were limited to 8 colors, it would only need to indicate which color is “switched on” and which is “switched off.” In fact, it can use three digits of 1 and 0 to represent the states of red, green, and blue. 

For example, 111 would be all 3 lights switched on, while 100 would be only the red switched on. 

This digit, which can be either 1 or 0, is called a bit.

<img width="1692" height="806" alt="image" src="https://github.com/user-attachments/assets/1b837229-af90-45dd-8cdc-a0dc793ef849" />

---

### From 8 to 16,000,000

Being limited to eight colors is inconvenient, as we prefer millions of colors. It would be convenient if each of the 3 lights (red, green, and blue) had 256 levels instead of just 2 (on or off). Let’s repeat the same math as earlier: 256 × 256 × 256 = 16,777,216. That’s more than 16 million colors.

One bit is enough to represent 2 states: on and off. We need 8 bits to express 256 states. In most textbooks, a group of 8 bits is referred to as a byte; however, you can also use the term octet.

You would realise that a color is now represented as 3 × 8 bits, or 3 bytes (24 bits). For example, one green color used on this page is represented as 10100011 11101010 00101010; that’s not a very convenient way to type or read color codes. Here comes the hexadecimal representation to the rescue!

---

### Hexadecimal Representation

| Hexadecimal Digit | Binary Representation |
|-------------------|----------------------|
| 0 | 0000 |
| 1 | 0001 |
| 2 | 0010 |
| 3 | 0011 |
| 4 | 0100 |
| 5 | 0101 |
| 6 | 0110 |
| 7 | 0111 |
| 8 | 1000 |
| 9 | 1001 |
| A | 1010 |
| B | 1011 |
| C | 1100 |
| D | 1101 |
| E | 1110 |
| F | 1111 |

Going back to the green color, instead of typing 10100011 11101010 00101010, we can type `A3EA2A`. In fact, that’s how you specify the color in graphics programs. 

To summarise what we have covered so far:
- In real-life applications, a color is represented in 24 bits, i.e., 3 bytes (24/8 = 3)
- Each byte can represent 256 different values (1 byte = 8 bits, 2^8 = 256)
- Each of the three bytes specifies the intensity of the red, green, and blue lights
- Every 4 bits are represented by one hexadecimal digit
- Each byte is represented as two hexadecimal digits (4 + 4 = 8)

---

### Answer the questions below

1. Preview the color `#3BC81E`. In one word, what does this color appear to be?

Green

2. What is the binary representation of the color `#EB0037`?

11101011 00000000 00110111

3. What is the decimal representation of the color `#D4D8DF`?

212 216 223

