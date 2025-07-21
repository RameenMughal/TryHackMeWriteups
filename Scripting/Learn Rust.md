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

The command we just ran also installs `Cargo`,

Cargo is the package manager for Rust. All the packages get uploaded to https://crates.io and does a lot of cool things.
