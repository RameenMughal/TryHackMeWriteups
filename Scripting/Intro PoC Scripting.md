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

1.	sets target IP and port
	
2.	obtains Webmin login page URL
  
3.	sends a POST request to the server

Here we simply have elements of a POST request, the login page, test cookie, and credentials. We know we need authenticated credentials in order to use this exploit, the POST request logs us in and assigns us a unique cookie to verify our local access privileges on the target and communicate as if we had a graphical interface.

The next section of the check function can be intimidating to beginners, but it's more simple than it appears. All this section does is format the unique cookie to exclude unnecessary text and generate a random string.
•	if res and res.code == 302 and res.get_cookies =~ /sid/ - if statement to continue if the HTTP response code is 302 and if the cookie equals the value of sid, session ID
•	session = res.get_cookies.split("sid=")[1].split(";")[0] - formats the cookie into a readable string based on the Set-Cookie header in the HTTP response
•	command = "echo #{rand_text_alphanumeric(rand(5) + 5)}" - generates a random string of 5 alphanumeric characters to use as invalid input

This part has some important duties within the script. We verify that
1.	the first POST request responds with a 302 (found) status code
2.	the cookies are labeled as sid
3.	format the cookies for excess text
4.	generate the invalid input to pipe into the malicious command

The most important information in this section is the format of the unique cookie and generating a random alphanumeric string.

The cookie is formatted by reading the output of the Set-Cookie header. The actual cookie is a random alphanumeric string but there is other information (the name and path) that is apart of the header, this line of code simply gets rid of the excess information and stores the alphanumeric value. From the developer tools, we see the name sid proceeds the actual value, so the method split is used to split the text at "sid=" and returns an array, storing the alphanumeric value and the remaining text. It's then repeated to split at ";" and return an array with no elements, leaving only the alphanumeric cookie value.

The command variable uses echo to print five random alphanumeric characters to be used as invalid input to pipe to the malicious command, generating a random alphanumeric string.

Information to convert
•	the login page URI data (credentials and login page file)
•	POST request sending the URI data
•	format the cookie
•	HTTP response code and the session id is not empty
•	generate five random characters
The second request simply checks if the target is vulnerable to the exploit, we'll discuss this in more detail below.
