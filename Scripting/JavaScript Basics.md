# JavaScript Basics

## Variables & Operators

You can easily link your JavaScript file in HTML by using a Script element.

 ```
<body>
  <script src="script.js"></script>
</body>
 ```

Remember to put the script tag right before the closing body tag. This way our HTML code will execute before our external JavaScript document. 
There are 3 types of variables in JavaScript: `var`, `let`, and `const`.

The var (variable) keyword was originally the only variable available, but thanks to the upgrade to ECMAScript 6 back in 2015, which is the specification that JavaScript conforms too, we now have multiple ways of declaring a variable or data types.

Quick Overview:
- `let`: If a variable is going to be reassigned later within the application, this is the ideal variable type to use.
- `var`: It's better to use either let or const for variables, but this variable type will still work and is still used in applications to this day. This variable can be updated and re-declared.
- `const`: If the variable will never change or won't be reassigned anywhere else in the application, this keyword is the best option.

Good things to remember:
- The `var` variable is globally scoped and can be updated and re-declared.
- The `let` variable is block-scoped and can be updated but not re-declared.
- The `const` variable is block-scoped and cannot be updated or re-declared.

Global Scope: A variable declared outside a function. This means all scripts and functions on a web application or webpage can access this variable.

Block Scope: A variable declared inside a block. This means we can use these variables inside of loops, if statements, or other declarations within curly brackets and have them be only used for that declaration instead of the entire application having access to it.

### Arithmetic Operators

| Operator    | Type           | What it does                             | Example                          |
|-------------|----------------|------------------------------------------|----------------------------------|
| `+`         | Addition       | Adds numbers or strings together         | `25 + 5 = 30`                    |
| `++`        | Increment      | Increases the variable's value by 1      | `let x = 20; x++; x = 21`        |
| `-`         | Subtraction    | Subtracts one number from another        | `15 - 5 = 10`                    |
| `--`        | Decrement      | Decreases the variable's value by 1      | `let x = 20; x--; x = 19`        |
| `*`         | Multiplication | Multiplies one number by another         | `5 * 10 = 50`                    |
| `/`         | Division       | Divides one number by another            | `100 / 10 = 10`                  |
| `%`         | Modulus        | Returns remainder of a division operation| `100 % 8 = 4`                    |

### Comparison Operators

| Operator    | What it Does                | Example           |
|-------------|-----------------------------|-------------------|
| `==`        | Equal to                    | `100 == 100`      |
| `===`       | Equal to & identical        | `500 === 500`     |
| `!=`        | Not equal to                | `100 != 50`       |
| `!==`       | Not identical               | `35 !== 75`       |
| `<`         | Less than                   | `5 < 85`          |
| `<=`        | Less than or equal to       | `60 <= 90`        |
| `>`         | Greater than                | `30 > 5`          |
| `>=`        | Greater than or equal to    | `1,000 >= 1,000`  |

Let's move on to our final lesson for variables: extra data types. It's time to see the available types of data that we can store within our variables. 
- Strings: 'Morpheus'
- Arrays: [1, 2, 3]
- Objects: {Name: 'John', Occupation: 'Master Hacker'}
- Booleans: true (or false)
- Numbers: 455
- Floating-Point Numbers: 10.5

### Answer the questions below

1. What type of data type is this: 'Neo'?

String

2. What data type is true/false?

Boolean

3. What is John's occupation?

Master Hacker

4. What tag is used for linking a JavaScript file to HTML?

Script

## Conditionals

```
if (5 === 10) {
console.log('Hello World!'); // Skips this code
} else if (10 === 10) {
console.log('Hello World!'); // Prints Hello World! to the console
} else {
console.log('ERROR ERROR ERROR');
};
```

If you need to test multiple conditions, then most of the time switch cases are best for optimization and readability within your code. If, else if, else statements and switch cases can both do similar tasks, but switch cases are better for performing multiple different conditions.

```
const animal = 3;
switch (animal) {
case 1:
document.write('Cow');
break;
case 2:
document.write('Chicken');
break;
case 3:
document.write('Monkey');
break;
default:
document.write('Animal?');
} // Outputs Monkey
```

## Functions

ECMAScript 6 is the most popular version of JavaScript. There are a lot of important differences between ES5 and ES6

This is a function in ES6 (ECMAScript 6):
```
const func = (a, b) => {
    let nums = a * b;
    console.log(nums); // Outputs 250
}
func(25, 10);
```

ES5:
```
function func(a, b) // Everything inside of the parenthesis defines our parameter(s)
{
    let nums = a * b;
    console.log(nums); // Outputs 250
}
func(25, 10);
```

## Objects & Arrays

### Objects

The most important thing about objects is to remember that they're just another variation of variables. Here is a quick example of an object:
```
var choosePill = {
    pillOne: 'Red',
    pillTwo: 'Blue',
    numberOfPills: 2
}
var choice = choosePill.pillOne; // This will access the Objects property
```

### Arrays

Arrays are fairly similar to objects, they have different stored values and syntax, but can be used for almost anything.

Here is the same code from before, but in an array:
```
var choosePill = ['Red', 'Blue', 2];
var choice = choosePill[0];
console.log(choice); // Outputs 'Red'
```

### Answer the questions below

1. What type of brackets are used for arrays?

`[]`

2. What color pill did we choose?

Red Pill

3. What is the output of this code?

Tyrell

<img width="975" height="176" alt="image" src="https://github.com/user-attachments/assets/fdc17a83-d74e-490f-9692-dd77a7fa78de" />

## Loops

There are for loops, while loops, and do while loops

### For Loops

Let's break this code down line by line:
```
for (a = 1; a <= 10; a++) {
    console.log(`Number: ${a}`); // Outputs 1-10 in our console
}
```

What does this code do? This code takes a, our variable, and loops through our specified range (1-10) and prints this to the console. By running this loop, we save our counter, or our range of numbers, to the variable a.

We can have more than one value within our first statement, but they must be separated by commas: `for (a = 1, b = 2; component-2; component-3) {}`

### While Loops

The while loop is similar to the for loop, with a few minor differences:
```
let x = 0;
while (x <= 3) {
console.log(x++); // Prints 0-3
}
```

This code will loop through x as long as it is less than or equal to three. 

### Do While Loops

The basics of the do...while loop is the code will execute the loop before checking if the condition is true.

Example:
```
let c = 10;
do {
console.log(c++); // Outputs 10-50
} while (c <= 50);
```

This code will ALWAYS execute at least once. It does this because loops normally require the conditions to be true, but a do...while loop doesn't require this as it executes before checking if the condition is truthy.

### Answer the questions below

1. Loops repeat until the written code is finished running (true/false)

True

2. What loop doesn't require the condition to be true for it execute at least once?

do…while

## Document Object Model (DOM)

Here is what we will be covering in the DOM section (keep in mind that these are just a few lines of code, DOM manipulation is a vast subject):

`document.getElementByID('Name_of_ID'); // Grabs the element with the ID name from the connected HTML file`

`document.getElementByClassName('Name_of_Class'); // Grabs the element with the class name from the connected HTML file`

`document.getElementByTagName('Name_of_Tag'); // Grabs a specific tag name from the connected HTML file`

There are also methods we can use to access different things within our HTML files such as addEventListener, removeEventListener, and many more. Most of what the DOM does is change, replace, edit, or in some form, manipulate the HTML file or webpage that you're working on. For us to successfully manipulate the DOM, we use events. These events are added to HTML tags to work with our JavaScript file. Some of the more important events that are used a lot, you can find here:
- onclick: Activates when a user clicks on the specific element
- onmouseover: Activates when a user hovers over a specific element
- onload: Activates when the element has loaded
- and many more that are used. 

<img width="975" height="358" alt="image" src="https://github.com/user-attachments/assets/5230982c-ee56-402e-83d4-63436cc55a4e" />

Now when a user clicks on the Click Me button, an alert pops up that says POP!!!

### Answer the questions below

What is the DOM? 

Document Object Model

## XSS

Cross-Site Scripting is a security vulnerability that's typically found in web applications which can be used to execute a malicious script on the target's machine.

There are multiple types of attack when talking about XSS:
- Keylogging
- tealing Cookies
- Phishing
- and many more

A keylogger is used by setting up an event listener on the target's keyboard, which will track their keystrokes and save them on the attacker's server.

When an attacker steals a target's cookies, they can use that information to log in as the user without needing advanced authentication or even just find information stored in the cookies that could lead to devastating effects on the target's online saved accounts. This is why so many websites use SSL or some other form of protection against these attacks.

Phishing is an interesting type of exploitation, an attacker can clone the website you're logging into and steal your credentials without you ever knowing. Another form of phishing is an attacker can insert code directly onto the webpage to change forms or input fields to steal the target's information.

The three most common types that I've seen of XSS are DOM-Based XSS (type-0 XSS), Reflected XSS (Non-Persistent XSS), and Stored XSS (Persistent XSS):

- **DOM-Based XSS**: This is when an attack payload is executed by manipulating the DOM (Document Object Model) in the target's browser. This type uses the client-side code instead of server-side code. Example: `https://example.com/#<script>alert('XSS')</script>`
- **Reflected XSS**: This is when a malicious script bounces off another website onto the target's web application or website. Normally, these are passed in the URL as a query, and it's easy as making the target click a link. This type originates from the target's request. Example: `https://example.com/search?q=<script>alert('Hacked')</script>`
- **Stored XSS**: This is when a malicious script is directly injected into the webpage or web application. This type originates from the website's database. Example: Attacker can post a comment like `Nice post! <script>stealCookies()</script>`

### Answer the questions below

What is the attack's name where the user is presented with a fake form to enter their credentials? 

Phishing

## JavaScript Challenge

### Answer the questions below

Sort the array [1,10,5,15,2,7,28,900,45,18,27]

```
let numbers = [1,10,5,15,2,7,28,900,45,18,27];
numbers.sort(function(a, b) {
    return a - b;
});
console.log(numbers);
```

<img width="975" height="222" alt="image" src="https://github.com/user-attachments/assets/767ebb6f-e0a3-4ed3-91a8-6c3df5c0fe6c" />
