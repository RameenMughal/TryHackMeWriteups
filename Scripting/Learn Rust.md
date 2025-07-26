# Learn Rust 

## What is Rust?

Rust is a new programming language created in 2015 by a small team of people, and later adopted by Mozilla (the organisation that created & maintains Firefox).

Rust has 3 goals:
- Fast
- Secure
- Productive

### Fast

Rust is statically typed, which means the data type of a variable is known at compile time. This allows the compiler to optimise the code further than if we didn't know the types.

Rust does not use garbage collection (despite being a low level programming language). Garbage collection is where the program attempts to reclaim memory from garbage. Garbage is memory occupied by objects that are no longer in use by the program.

Python and JavaScript use garbage collection. These abstractions may cause issues (as in Discord's case), which is why many choose a low level programming language.

### Secure

Rust is completely memory safe. This means that exploits involving memory aren't possible in Rust, unless you explicitly specify unsafe Rust code.

The Microsoft Security Response Centre states that 70% of all CVE's MSRC assigns are memory safety issues.

Sometimes programmers must perform unsafe operations. Rust provides tools to wrap these unsafe actions so unsafe code can be statically enforced by the Rust compiler.

The memory safety is guaranteed by the concept of ownership. All Rust code follows these rules:
- Each value has a variable, called an owner.
- There can only be one owner at a time.
- When the owner goes out of scope, the value will be dropped.

Values can be moved or borrowed between variables, but no value can have more than 1 owner.

Python allows functions to alter variables they do not own, whereas Rust doesn't.

Example can be if a list is given to other function it creates a reference to the list and as list can be mutable (can change values), the function can change the variables when this function does not even own the variable.

### Productivity

Rust provides all of the tools developers need to be productive, shipped with the platform itself.
- **Cargo**: Rust's version of NPM or PyPi. Download packages others have created.
- **Clippy**: Microsoft Clippy, but re-imagined for Rust to aid with development.
- **RustFmt**: Automatically formats Rust code
- **Cargo Test**: A built in testing application created by the Rust developers.
- **Cargo docs**: Automatically generate documentation for your code, using documentation comments (written in Markdown). This documentation is then sent to docs.rs upon publishing to Cargo.
- **Rust-Analyzer**: Think IDE but more intelligent. Rust Analyzer clearly labels what is wrong with your code, why it is wrong, the exact characters that conflict and cause the error, and 90% of the time it provides an "auto-fix" function that automatically fixes these errors for you.
- **The Rust Book & Docs**: Rust has a book, called The Book which details everything you could want to know about Rust. Neatly chaptered, easily searchable and at your disposal for free.

### Conclusion

It supports calls from functions written in other languages (foreign function interfacing).

Here's an example of calling C code 

```
extern "C" {
    fn abs(input: i32) -> i32;
}

fn main() {
    unsafe {
        println!("C believes that the absolute value of -3 is: {}", abs(-3));
    }
}
```

This Rust code declares and calls the C standard library function `abs` to compute the absolute value of -3, using an `extern "C"` block and an unsafe call since it's a foreign function.

### Answer the questions below

1. What other language is Rust similar to in terms of performance?

C++

2. What famous company switched from Go to Rust, mentioned in this task?

Discord

3. Microsoft Security Centre reports what percentage of CVE's they assign are memory safety issues? Include the % sign.

70%

4. What is Rust's version of NPM or PyPi?

Cargo

## Installing and Tooling

Rust recommends using the tool `rustup` to manage multiple versions of Rust.

Install RustUp with this command: `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`

Rust comes in 3 flavours. Stable, Beta, and Nightly.

Stable is the latest stable release of Rust (stable releases are usually shipped every 6 weeks). Beta updates periodically. Nightly updates when the language itself updates.

let's install some Rust tools to aid our development.

The command we just ran also installs `cargo`,

Cargo is the package manager for Rust. All the packages get uploaded to https://crates.io and does a lot of cool things.

The 3 core Cargo commands are:
- `cargo install`: Install a package from Crates.io
- `cargo publish`: Publish a package to crates.io
- `cargo update`: Updates all of the local packages

But, since we are developing RustCode there are 3 more important commands
- `cargo test`: Run the tests for our code
- `cargo fmt`: Runs the formatting tool. This tool automatically formats your code (apply the argument `--all` to format all code). Similar to Python's Black but built in.
- `cargo clippy`: Microsoft Clippy but for Rust! Clippy will point out common errors in your code and help you correct them.

There is one tool, that is a community based tool — that is seen as absolutely essential to the Rust ecosystem.

That tool is Rust-Analyzer. Imagine an IDE but smarter and more advanced. Rust-Analyzer will analyse your code as you write it, spot errors before you compile & provide an auto-fix option to automatically fix the errors.

Rust-Analyzer states that their most supported version is VS Code, but they are available on many other platforms.

Something cool to note is that the main tools of Rust are written by the Rust developers themselves. 

### Answer the questions below

1. What is the tool we used to install Rust called?

`rustup`

2. How do we install the package `rustscan` using cargo?

`cargo install rustscan`

3. What command do we run to format our code?

`cargo fmt`

## Hello, World!

Create a new folder, and in the terminal type: `cargo init`

If the error says that it does not recognize this command then update your environment by `source $HOME/.cargo/env`

Then check the version of cargo `cargo --version`

This makes Cargo initialise a new Rust repository. Cargo will take care of most of the work for you.

The file structure is as follows:

```
- Cargo.toml
- src/
    - main.rs
```

`cargo.toml` is the configuration file for our Rust project. It includes our dependencies, project name, authors, the version of Rust we are using and more.

When we have just ran `cargo init`, our file `Cargo.toml` will look like this:

```
[package]
name = "Learn_Rust"
version = "0.1.0"
edition = "2024"

[dependencies]
```

Our `main.rs` file in the folder src is the main file where we write our code. Every single Rust project must have a main file, and every main file must have a main function.

```
fn main() {
    println!("Hello, world!");
}
```

In Rust, we use curly braces to denote blocks of code. And a semi-colon to express the end of an expression.

To print in Rust, we use the macro `println!`.

We know `println` is a macro, as it is called with an exclamation mark. Macros, in a nutshell, allow us to write code that writes more code. To put it even simpler, we can create our own syntax that translate to different code.

To run this program, we execute: `cargo run`

This should result in:

```
➜ cargo run
   Compiling hello_world v0.1.0 (/tmp/hello_world)
    Finished dev [unoptimized + debuginfo] target(s) in 0.21s
     Running `target/debug/hello_world`
Hello, world!
```

This command:
- Compiles the code with the unoptimised build (to increase the speed of compilation)
- Runs the code

You'll also notice a new folder has been created, `target`.

`target` contains the binaries for our project.

```
- Cargo.toml
- src/
    - main.rs
- target/
    - debug/
        = build/
        - deps/
        - examples/
        - hello_world
        - hello_world.d
        - incremental/
```

Right now, the only important file is `hello_world`. This file is actually the binary for our program.

To build our project without running it, run: `cargo build`

And now we can run the binary directly. `./target/debug/hello_world`, mine is the file name Learn_Rust so my command is `./target/debug/Learn_Rust`

This is exactly the same as `cargo run`, but 2 commands.

When we want to build our project and optimise it, run it with the release profile: `cargo build --release`

Use the normal cargo build for quick checking of the code. Use the release argument to optimise the code to the maximum possible that the Rust compiler will allow.

We call `--release` a profile, specifically the release profile. The Rust compiler has different levels of optimisation depending on what you want.

### Answer the questions below

1. How do we initialise a new Rust project?

`cargo init`

2. What character represents a macro?

`!`

3. What does every Rust project need as a file?

`main.rs`

4. If we wanted to add a dependency to our Rust project, what file would we edit?

`Cargo.toml`

5. How do we run our Rust project?

`cargo run`

6. How do we build the project RustScan with the release profile (most optimised)?

`cargo build --release`

7. What folder are the release binaries stored in?

`target/release/`

8. How many release profiles does Rust have using optimisation level?

4

## Variables

All variables, by default, are immutable in Rust.

This is a safety feature, but also a productivity feature. Variables that don't change mean you don't have to track down when the value changed, and immutable variables are great for concurrency

Let's see this in action.

```
fn main() {
    let x = 5;
    println!("The value of x is: {}", x);
    x = 1;
    println!("The value of x is: {}", x);
}
```

This code does not compile. It returns with the error: `error[E0384]: cannot assign twice to immutable variable x`

The error tells us everything we need to know.

`cannot assign twice to immutable variable`

This is telling us that we are assigning a value to an immutable variable (a variable that cannot be changed), twice. Which cannot happen.

To make a variable mutable, we place the `mut` keyword in front of it like so:

```
fn main() {     
     let mut x = 9;     
     println!("The value of x is: {}", x);     
     let x = 4;     
     println!("The value of x is: {}", x); 
}
```

Constants are values that are bound to a name and are not allowed to change

### Answer the questions below

1. In question 1, does this code compile? T(rue) or F(alse)

F

2. What is the error code returned by question 1?

Edit the `main.rs` by `nano` command and run the file by `cargo run`

<img width="373" height="112" alt="image" src="https://github.com/user-attachments/assets/34a30809-9c02-407e-ae97-d6bb35c4ceeb" />

**Answer**: E0308

3. Does the code in question 2 compile? T(rue) or F(alse)

F

4. What is the error message returned?

<img width="374" height="157" alt="image" src="https://github.com/user-attachments/assets/65561550-0526-40b8-b5cd-6fd7d28630df" />

**Answer**: `cannot assign twice to immutable variable`

## Constant Variables

Rust also has constants. These are values that aren't just immutable by default, but are always immutable.

Constants can be declared in any scope, including the global scope. This means that we can use their value in any part of our code, or in multiple places at once.

Constants can only be constant, they cannot be set to a function call or any other value that may change at runtime.

We declare constants with the `const` keyword like so: `const HUNDRED_THOUSAND: u32 = 100_000`;

Notice how in Rust, we can use the _ character to denote a space in number without it affecting the value itself. This is purely for readability. We can also use 100000

`u32` means unsigned 32 bit integer

Also note that it is tradition to name a constant in all uppercase.

### Shadowing

I'm going to show you something that might not make sense at first.

```
fn main(){
    let x = 6;
    let x = x + 1;
    println!("{}", x)
}
```

This is called shadowing. 

Here's an explanation from the official Rust docs about this principle (edited to match the example)

"This program first binds x to a value of 6. Then it shadows x by repeating let x =, taking the original value and adding 1 so the value of x is then 7."

By using let, we can perform transformations on the variable but have the variable still be immutable after all the transformations have completed.

We're effectively creating a new variable with the `let` keyword, which means we can change the type of the value.

```
let word = "hello";
let word = word.len();
```

Which is allowed.

However, if we tried to use `mut`, it wouldn't be allowed — as `mut` cannot change types.

```
let mut word = "hello";
word = word.len();
```

### Answer the questions below

1. How do we define a constant in Rust?

`const`

2. Can we shadow a constant? T(rue) or F(alse)

F

3. What do we use to change the type of an immutable variable once it has been defined?

shadowed

4. Will the code "CONST word = "yes"" compile? T(rue) or F(alse)

F

5. We have "let word = "hello"", how do we get the length of the variable?

`word.len();`

## Data Structures

A type hint defines what the data type of a variable is at compile time.

`let ports: u32 = 65535`

The `: u32` states that the variable `ports` is of size `u32`.

The `u` in the integer means unsigned, and the 32 is how many bits it has.

Unsigned integers can only ever be positive, signed integers can be both positive and negative represented by `i`

Integers range from 16 bits up to 128 bits. Some operating systems can't use integers higher than `u32`, and using such large integer types may slow down the program on some systems.

| 8-bit       | i8           | u8        |
|-------------|--------------|-----------|
| 16-bit      | i16          | u16       |
| 32-bit      | i32          | u32       |
| 64-bit      | i64          | u64       |
| 128-bit     | i128         | u128      |
| arch        | isize        | usize     |

`isize` and `usize` are pointer-sized integer types. That means their size depends on the architecture of the system your program is running on (i.e., 32-bit vs 64-bit)

### Strings

There are two types of strings in Rust. `String` and `&str`.

`String` is a growable allocated data structure whereas `str` is an immutable fixed-length string somewhere in memory.

`&str` is a string slice of `string`.

### Answer the questions below

1. Given the number -6, is this signed or unsigned?

Signed

2. Given the number 65536, what is the smallest unsigned datatype we can fit this into?

With 16 bits 2^16 is 65,535 which does fit 65536 so it will fit in 32 bits

**Answer**: `u32`

3. What's the smallest sized signed integer in rust?

It is `i8` but it accepted `i16`

**Answer**: `i16`

4. Create a mutable u32 variable called "tryhackme" and assign it the number 9

`let mut tryhackme: u32 = 9;`

5. What data type is used to represent a string slice?

`&str`

6. Let's say you had a variable, X. You wanted to typehint the variable as a string. What would you write? Include X in the variable but not the `let` or `=` parts.

`X: string`

## Functions

The main function is the first function called of the main file, which is the first file called.

Every binary file written in Rust needs a main file, and every main file needs a main function.

Functions in Rust are defined as:

```
fn hello() -> u16{
    println!("hello!");
    6
}
```

The main function is the same as this, but in a binary file it doesn't return anything.

```
fn main(){
    println!("I do not return!")
}
```

Well, Rust returns the final expression of the function.

Alternatively, we can use the return statement to return earlier. However, it's not very nice to use it to return the value at the end of the function

Let's add some arguments to our functions.

```
fn print_name(name: String){
    println!("{}", name);
}
```

Our function arguments have to include the type of each argument.

Now let's try to make this function return something.

```
fn print_name(name: String) -> u16{
    println!("{}", name);
    6;
}
```

When we return data, we have to type hint the type of data that is being returned.

### Answer the questions below

1. Will question 1 return 8172192? T(rue) or F(alse)

F

2. Will example 2 run? T(rue) or F(alse)

F

3. What type should we give to the argument for question 3?

`&str`

4. The last expression in a function (the return) needs to have a semicolon. T(rue) or F(alse)

F

5. Every function need to return something. T(rue) or F(alse)

F

6. Functions in Rust can be nested within other functions. T(rue) or F(alse)

T

7. What keyword do we use to return early from a function?

`return`

8. You nest a function named main, inside another function named main. Will this run? T(rue) or F(alse)

T

## Loops

There are 3 loops in Rust.

### loop

The loop keyword loops forever or until we explicitly tell it to stop.

```
fn main(){
    loop {
        println!("TryHackMe Rocks!");
    }
}
```

We can either break with ctrl+c or we can tell Rust to break with break

```
fn main(){
    loop {
        println!("TryHackMe Rocks!");
        break;
    }
}
```

### Conditional While Loops

Rust also has while loops, which loop while a condition is true.

Look at this example for some code, taken from the Rust Book:

```
fn main() {
    let mut number = 3;
    
    while number != 0 {
        println!("{}!", number);
        number -= 1;
    }

    println!("LIFTOFF!!!");
}
```

### For Loops

Rust also has for loops, which we can use to iterate over elements of a collection.

```
fn main() {
    let a = [10, 20, 30, 40, 50];

    for element in a.iter() {
        println!("the value is: {}", element);
    }
}
```

### Answer the questions below

1. How do we break out of a loop?

`break`

2. Simplest keyword to make an infinite loop?

`loop`

3. Turn `let a = [10, 20];` into something we can iterate over.

`a.iter()`

4. While loops can also be infinite. T(rue) or F(alse).

T

## Zero Cost Abstractions

Rust has this really cool thing called Zero Cost Abstractions. It’s also a thing in other low level languages.

Zero cost abstraction is:

"What you don’t use, you don’t pay for. And what you do use, you couldn’t do any better if you coded by hand."

Let’s talk about the 2 parts of this sentence.

"What you don’t use, you don’t pay for."

The language shouldn’t have a global cost for a feature that isn’t used. Let’s say to use a for loop, the language needs to have some massive 1gb file that slows down everything else. If we never use a for loop, we still pay for the for loop!

"And what you do use, you couldn’t do any better if you coded by hand."

Say you wrote some code, a function that calculated Fibonacci numbers. And you compiled this code down into assembly.

Now let’s say you hand-write assembly to do the same function — calculate Fibonacci numbers but this time in assembly.

Handwriting it in assembly would mean we would either gain no performance, or we would lose performance.

If you write a function (like calculating Fibonacci numbers), and Rust compiles it to machine code — Even if you tried to write that machine code by hand, you wouldn’t make it any faster.

So you get the convenience of writing safe, readable code, but the speed of hand-tuned low-level code.

Now, let's explore iterators.

Iterators are a way of processing a series of items with Rust, much like a for loop.

We saw earlier a.iter(). This code turns the variable a into an iterator over the items of a. But this code by itself doesn't do anything useful.

This is because iterators are lazy. You have to tell them to do something to get values from them.

We make the iterator do something by calling it in this for loop.

Now we can make the code do something and consume the iter using some nifty functional programming skills. To square every number in an iterator, and then to sum it we can do:

```
let a = vec![1, 2, 3];
a.iter()
.map(|&i| i * i
.sum()
```

Note, in Rust, we can separate applications of methods with new lines.

Iterators are zero cost abstractions in Rust. For loops are not.

### Answer the questions below

1. Iterators are lazy. T(rue) or F(alse).

T

2. For loops are explicitly mentioned in the Rust book as zero cost abstractions. T(rue) or F(alse).

F

3. Zero Cost Abstractions are common in high level languages like Python or JavaScript T(rue) or F(alse).

F

## Rayon

Rayon is an external crate for Rust. Rayon makes multi threading easy. 

Go to Crates.io and copy the command to install rayon.

<img width="208" height="170" alt="image" src="https://github.com/user-attachments/assets/626ed6e6-3d4f-4c42-bc9f-bb7d68b43ac9" />

Run the `cargo add rayon` or add `rayon = "1.10.0"` under dependencies in `Cargo.toml`

This way you can add Rayon external library used for multi threading.

Okay, now let's take our iter in the last task and make it multi threaded.

```
fn sum_of_squares(input: &[i32]) -> i32 {
    input.iter()
         .map(|&i| i * i)
         .sum()
}
```

This is our previous code.

```
use rayon::prelude::*;
fn sum_of_squares(input: &[i32]) -> i32 {
    input.par_iter() // <-- just change that!
         .map(|&i| i * i)
         .sum()
}
```

This is our multi-threaded code.

### Answer the questions below

1. What crate do we use to easily make an iter multi threaded?

Rayon

2. How do we tell Rust to include an external crate into our program? What file do we place this information in?

`Cargo.toml`

3. Turn a.iter() into a multi threaded parallel iter using Rayon

`a.par_iter()`

4. What website do we go to for Crates?

Crates.io

## if Statements
