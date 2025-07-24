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

cannot assign twice to immutable variable

This is telling us that we are assigning a value to an immutable variable (a variable that cannot be changed), twice. Which cannot happen.
