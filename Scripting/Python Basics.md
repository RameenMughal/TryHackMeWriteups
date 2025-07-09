# Python Basics

## Hello World

### Answer the questions below

On the code editor, print "Hello World". What is the flag?

`print("Hello World")`

![image](https://github.com/user-attachments/assets/390a693d-d9bc-4b6c-ba88-99ce9d202baa)

## Mathematical Operators

The table below shows the different operations.

| Operator        | Syntax    | Example                 |
|-----------------|-----------|-------------------------|
| Addition        | `+`       | `1 + 1 = 2`             |
| Subtraction     | `-`       | `5 - 1 = 4`             |
| Multiplication  | `*`       | `10 * 10 = 100`         |
| Division        | `/`       | `10 / 2 = 5`            |
| Modulus         | `%`       | `10 % 2 = 0`            |
| Exponent        | `**`      | `5 ** 2 = 25` (`5^2`)   |

Now that we know basic mathematical operators, let's move on to comparison operators;

- Greater than: `>`
- Less than: `<`
- Equal to: `==`
- Not Equal to: `!=`
-	Greater than or equal to: `>=`
- Less than or equal to: `<=`

### Answer the questions below

1. In the code editor, print the result of 21 + 43. What is the flag?

`print(21 + 43)`

![image](https://github.com/user-attachments/assets/42581ed8-a906-4b6e-8ca3-bf5e34b15836)

2. Print the result of 142 - 52. What is the flag?

`print(142 - 52)`

![image](https://github.com/user-attachments/assets/8d5bd4cf-bfb4-4094-b188-2781739463c7)

3. Print the result of 10 * 342. What is the flag?

`print(10 * 342)`

![image](https://github.com/user-attachments/assets/0aea96be-3340-4e66-80c0-b73ee4d90125)

4. Print the result of 5 squared. What is the flag?

`print(5 ** 2)`

![image](https://github.com/user-attachments/assets/51b25658-0e02-4cb8-a3bc-92d7d77f43d8)

## Variables and DataTypes

Variables allow you to store and update data in a computer program.

Data Types, which is the type of data being stored in a variable. You can store text, or numbers, and many other types. The data types to know are:
- String - Used for combinations of characters, such as letters or symbols
- Integer - Whole numbers
- Float - Numbers that contain decimal points or for fractions
- Boolean - Used for data that is restricted to True or False options
- List - Series of different data types stored in a collection

### Answer the questions below

1. In the code editor, create a variable called height and set its initial value to 200.

`height = 200`

2. On a new line, add 50 to the height variable.

`height = height + 50`

3. On another new line, print out the value of height. What is the flag that appears?

`print(height)`

![image](https://github.com/user-attachments/assets/3336536c-77d6-4eff-9841-8aa6f5aba824)

## Logical and Boolean Operators

Logical operators allow assignment and comparisons to be made and are used in conditional testing (such as if statements).

|  Comparison Type           | Operator    | Example        |
|----------------------------|-------------|----------------|
| Equivalence                | `==`        | `if x == 5`    |
| Less than                  | `<`         | `if x < 5`     |
| Less than or equal to      | `<=`        | `if x <= 5`    |
| Greater than               | `>`         | `if x > 5`     |
| Greater than or equal to   | `>=`        | `if x >= 5`    |

Boolean operators are used to connect and compare relationships between statements. Like an if statement, conditions can be true or false.

| Logic Description                                | Operator    | Example                              |
|--------------------------------------------------|-------------|--------------------------------------|
| Both conditions must be true                     | `AND`       | `if x >= 5 AND x <= 100`             |
| Only one condition needs to be true              | `OR`        | `if x == 1 OR x == 10`               |
| Condition is the opposite of the given argument  | `NOT`       | `if NOT y`                           |

## Introduction to if Statements

Using "if statements" allows programs to make decisions.

### Answer the questions below

In the code editor, click on the "shipping.py" tab and follow the instructions to complete this task.

1. In the code editor, click on the "shipping.py" tab and follow the instructions to complete this task.

```
shipping_cost_per_kg = 1.20
customer_basket_cost = 34
customer_basket_weight = 44

if(customer_basket_cost >= 100):
  print('Free shipping!')
else:
  shipping_cost = 1.20 * customer_basket_weight
  customer_basket_cost += shipping_cost

print("Total basket cost including shipping is " + str(customer_basket_cost))
```

2. Once you've written the application in the code editor's shipping.py tab, a flag will appear, which is the answer to this question.

![image](https://github.com/user-attachments/assets/2039f448-797a-4935-83f0-cfe8e29ab10d)

3. In shipping.py, on line 15 (when using the Code Editor's Hint), change the customer_basket_cost variable to 101 and re-run your code. You will get a flag (if the total cost is correct based on your code); the flag is the answer to this question.

![image](https://github.com/user-attachments/assets/4df41e20-318a-42f1-8091-edc720fd0eec)

## Loops

In programming, loops allow programs to iterate and perform actions a number of times. There are two types of loops, for and while loops.

For the structure a while loop. We can have the loop run indefinitely or (similar to an if statement) determine how many times the loop should run based on a condition.

A for loop is used to iterate over a sequence such as a list. Lists are used to store multiple items in a single variable, and are created using square brackets

### Answer the questions below

On the code editor, click back on the "script.py" tab and code a loop that outputs every number from 0 to 50.

```
for i in range(51):
  print(i)
```

![image](https://github.com/user-attachments/assets/d0b43898-10e2-4e80-937f-1a29ef08416d)

## Introduction to Functions

As programs start to get bigger and more complex, some of your code will be repetitive, writing the same code to do the same calculations, and this is where functions come in. A function is a block of code that can be called at different places in your program.

### Answer the questions below

1. You've invested in Bitcoin and want to write a program that tells you when the value of Bitcoin falls below a particular value in dollars.
In the code editor, click on the bitcoin.py tab. Write a function called `bitcoinToUSD` with two parameters: `bitcoin_amount`, the amount of Bitcoin you own, and `bitcoin_value_usd`, the value of bitcoin in USD. The function should return `usd_value`, which is your bitcoin value in USD (to calculate this, in the function, you times `bitcoin_amount` variable by `bitcoin_value_usd` variable and return the value). The start of the function should look like this:

`def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):`

Once you've written the `bitcoinToUSD` function, use it to calculate the value of your Bitcoin in USD, and then create an if statement to determine if the value falls below $30,000; if it does, output a message to alert you (via a print statement).

```
investment_in_bitcoin = 1.2
bitcoin_to_usd = 40000

def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
  usd_value = bitcoin_amount * bitcoin_value_usd
  return usd_value

investment_in_usd = bitcoinToUSD(investment_in_bitcoin, bitcoin_to_usd)
if investment_in_usd <= 30000:
  print("Investment below $30,000! SELL!")
else:
  print("Investment above $30,000")
```

![image](https://github.com/user-attachments/assets/6d672fe2-0ac0-4ba9-be8f-b0e671ad1853)

2. 1 Bitcoin is now worth $24,000. In the code editor on line 14, update the bitcoin_to_usd variable value to 24000 and see if your Python program recognises that your investment is below the $30,000 threshold.

![image](https://github.com/user-attachments/assets/441070cd-dd5a-4c0a-aed8-7e39fdc90479)

## Files

In Python, you can read and write from files.

To open the file, we use the built-in open() function, and the "r" parameter stands for "read" and is used as we're reading the contents of the file. 

The variable has a `read()` method for reading the contents of the file. 

You can also use the `readlines()` method and loop over each line in the file; useful if you have a list where each item is on a new line.

You can also create and write files. 

If you're writing to an existing file, you open the file first and use the "a" in the open function after the filename call (which stands for append). 

If you're writing to a new file, you use "w" (write) instead of "a". 

We use the `close()` method after writing to a file; this closes the file so no more writing to the file (within the program) can occur.

### Answer the questions below

In the code editor, write Python code to read the flag.txt file. What is the flag in this file?

```
f = open("flag.txt", "r")
print(f.read())
```

![image](https://github.com/user-attachments/assets/7044ec28-d798-4ef0-a3a8-60dc809be91d)

## Imports

In Python, we can import libraries, which are a collection of files that contain functions.

Here are some popular libraries you may find useful in scripting as a pentester:
- Request - simple HTTP library.
- Scapy - send, sniff, dissect and forge network packets
- Pwntools - a CTF & exploit development library.

Many of these libraries are already built into the programming language; however, libraries written by other programmers not already installed in your machine can be installed using an application called pip, which is Python's package manager.
