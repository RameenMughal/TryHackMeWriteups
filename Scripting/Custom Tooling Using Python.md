# Custom Tooling using Python

<img width="860" height="173" alt="image" src="https://github.com/user-attachments/assets/d4605618-a448-403f-ac40-e531d04daf7c" />

## Introduction

Creating your own custom tooling is critically important for web application red teaming, as you rarely find a tool or plugin that will do exactly what you need. This then calls for you to develop custom tooling!

Code is the most versatile option, as it allows you to create brand new software specifically for your needs. Being able to use code also allows you to take existing tools and exploits to customise them to your needs. 

While we will showcase using Python in this room, the principles can be applied to any coding language of your choice.

## Using a Coding Language for Custom Tooling

### Why Create Your Own Tools?

When you go up against a web application during a red team, relying solely on existing tools may not always be sufficient. While there are many open-source and commercial options available, they may not fully align with the specific needs of your engagement.

Creating custom tooling allows you to:
- Tailor functionality to your specific needs
- Automate exploit and create automated workflows to perform repetitive tasks
- Bypass detection mechanisms
- Modify existing exploits and tools to suit your exact needs

Coding is the ultimate form of this. It allows you to either create something entirely from scratch or build a new tool from existing parts.

### To Script or Not to Script

When selecting a language for building your custom tools, one of the primary considerations is whether to use a scripting language or a compiled language. 

While it is good to be able to do both, it is worth considering which is best for your current situation given their advantages and trade-offs:

| Decision Factor     | Scripting Languages (Python, Ruby, JavaScript)                                                                 | Compiled Languages (Go, C++, .NET)                                                                 |
|---------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| Speed of Development | Fast development and testing as code is immediately interpreted and executed                                  | Slower development due to compilation requirements                                                 |
| Performance         | Generally slower as interpretation only happens at runtime                                                    | Faster execution as it can be compiled and optimised into machine code                             |
| Ease of Use         | Easier to create and modify on the fly                                                                         | More complex to modify and stricter syntax complexities                                            |
| Portability         | Cross-platform but depends on interpreter availability                                                        | Platform-specific builds, but compiled versions often run with native software                     |
| Detection and Evasion | Can be obfuscated but may trigger AV/EDR due to scripting signatures                                          | Harder to analyse, sometimes better at bypassing detection mechanisms                              |
| OS Interfacing      | Great for automation and tool scripting                                                                       | Provides lower-level access to system resources                                                    |

### Choosing the Right Language

Different coding languages have unique strengths and weaknesses when creating custom tooling and exploits. Let's take a look at a comparison:

| Language   | Type      | Key Features                                      | Advantages                                                            | Disadvantages                                                                 |
|------------|-----------|---------------------------------------------------|------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Python     | Scripting | Extensive libraries and dynamic typing            | Easy to learn and allows for fast prototyping                          | Slower execution and often easily detected by AVs or EDRs                     |
| JavaScript | Scripting | Browser-based and easy-to-perform threading       | Useful for web-based exploits and widely supported in web applications | Not suitable for low-level system tasks and has a high detection rate         |
| Go (Golang)| Compiled  | Statically typed and provides efficient concurrency | Fast execution and easy cross-compilation                              | Creates larger binary sizes and has fewer security-specific libraries currently |
| .NET (C#)  | Compiled  | Windows-focused and integrates well with system APIs | Good for Windows exploitation and has easy obfuscation techniques      | Limited cross-platform compatibility and requires the .NET runtime            |
| C++        | Compiled  | High performance and allows direct memory manipulation | Very fast execution and grants low-level system access (stealthy tools) | Complex syntax and harder to debug                                            |

### Popular Python

Among these options, Python remains one of the most widely used languages for building custom security tools and exploits. Some of the main reasons for its popularity are:
- Python has an extensive library list for things like networking, web interaction, and automation.
- Python scripts can run on any operating system with the Python interpreter installed. Using libraries such as py2exe, you could even create a compiled binary of your Python code to execute on Windows systems that do not have the Python interpreter.
- Given Python's popularity, there is large community support for it, making it easy to modify it using existing tools.

Choosing the right coding language depends on the specific requirements of your custom tooling. While Python offers rapid development and strong community support, compiled languages like Go and .NET can provide better stealth and performance. 

### Answer the questions below

1. Does a scripting language perform better than a compiled language? (Yea/Nay)

Nay

2. Which compiled language is easy to cross-compile?

Go

3. Which scripting language is best suited for web-based exploits?

Javascript
