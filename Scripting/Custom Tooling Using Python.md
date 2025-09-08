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

## Developing a Brute-Forcing Tool

Let’s explore how we can develop a brute-forcing tool to bypass authentication.

Brute-force attacks involve trying multiple username-password combinations until the correct credentials are found. While these attacks are commonly mitigated by rate limiting and account lockout mechanisms, they still remain an easy-to-do job for hackers.

### Essential Commands

Before we start coding, let's go over some essential functions and techniques used in brute-forcing:
- **Requests library**: A Python library that facilitates sending HTTP requests and receiving responses from web apps. It has built-in functions to send custom headers like user-agent, HTTP method, and more. 
- **Handling responses**: Identifying successful logins based on HTTP status codes, redirects, or content patterns, which further helps to identify valid credentials.
- **String library**: Built-in functions from the String module make it easy to generate letter sequences, perform text formatting and manipulation, and more.

### Practical

In order to understand the essence of custom tooling using Python, consider a web application hosted at `http://python.thm/labs/lab1`. Visit the application, and you will see the following login panel. 

As a pentester, your task is to bypass the authentication mechanism and get access to the main dashboard. Suppose you discover that the username is `admin` and the password is a 4-digit numeric value from the system logs or the frontend. 

One option is to manually try different combinations, but this is inefficient. A more viable approach is to use Python to automate the brute-force attack and try to attempt all possible 4-digit passwords.

Now, we will write a simple Python script to automate brute-force attacks. This script will attempt different password combinations against the server and, based on the response, determine whether a combination is valid. In the AttackBox, create a new script called `bruteforce.py` with the following code:

```
import requests

url = "http://python.thm/labs/lab1/index.php"

username = "admin"

# Generating 4-digit numeric passwords (0000-9999)
password_list = [str(i).zfill(4) for i in range(10000)]

def brute_force():
    for password in password_list:
        data = {"username": username, "password": password}
        response = requests.post(url, data=data)
        
        if "Invalid" not in response.text:
            print(f"[+] Found valid credentials: {username}:{password}")
            break
        else:
            print(f"[-] Attempted: {password}")

brute_force()
```

### Key Areas in the Code 

- **Target URL**: The above code sends `POST` requests to `http://python.thm/labs/lab1/index.php`, simulating login attempts. The endpoint information is stored in the `url` variable.
- **Generating password list**: It creates a list of 4-digit numeric passwords (0000-9999) using Python’s `zfill()` function. If you need to iterate over characters, you can use `string.ascii_uppercase` for A-Z and `string.ascii_lowercase` for a-z. This is carried out through the code `password_list = [str(i).zfill(4) for i in range(10000)]`.
- **Brute-force function**: The brute_force function iterates through the password list, sending different username and password combinations to the server.
- **Response handling**: If the response does not contain the word "Invalid", the script assumes the login is successful and prints the valid credentials.

### Executing the Script

Navigate to the terminal and execute the following command python3 bruteforce.py. Upon execution, the script will try all possible 4-digit numeric passwords. Once it finds the correct password, it will display the valid credentials.
