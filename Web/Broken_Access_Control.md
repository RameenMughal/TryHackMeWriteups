# Broken Access Control

Room: [Broken Access Control](https://tryhackme.com/room/owaspbrokenaccesscontrol)

Pre-requisites:
1. [Owasp Top 10 2025 Module](https://tryhackme.com/module/owasp-top-10-2025)
2. [Burp Suite Module](https://tryhackme.com/module/learn-burp-suite)

<img width="934" height="200" alt="image" src="https://github.com/user-attachments/assets/7e24a435-a259-447e-8126-c4fbfe66c82f" />

## Introduction

Broken access controls are a type of security vulnerability that arises when an application or system fails to properly restrict access to sensitive data or functionality. This vulnerability allows attackers to gain unauthorized access to resources that should be restricted, such as user accounts, files, databases, or administrative functions. Broken access controls can occur due to a variety of factors, including poor design, configuration errors, or coding mistakes.

---

### Pre-requisites:

1. Basic understanding of JSON, web applications, and HTTP protocols.
2. Familiarity with scripting languages such as PHP and JavaScript.
3. Knowledge of web application security standards and frameworks such as [OWASP Top 10](https://tryhackme.com/module/owasp-top-10-2025).
4. Basic understanding and usage of a proxy tool like [Burp Suite](https://tryhackme.com/module/learn-burp-suite).

## Broken Access Control Information

### What is Access Control?

Access control is a security mechanism used to control which users or systems are allowed to access a particular resource or system. Access control is implemented in computer systems to ensure that only authorized users have access to resources, such as files, directories, databases, and web pages. The primary goal of access control is to protect sensitive data and ensure that it is only accessible to those who are authorized to access it.

Access control can be implemented in different ways, depending on the type of resource being protected and the security requirements of the system.

Some common access control mechanisms include:

1. **Discretionary Access Control (DAC)**: In this type of access control, the resource owner or administrator determines who is allowed to access a resource and what actions they are allowed to perform. DAC is commonly used in operating systems and file systems.
2. **Mandatory Access Control (MAC)**: In this type of access control, access to resources is determined by a set of predefined rules or policies that are enforced by the system. MAC is commonly used in highly secure environments, such as government and military systems.
3. **Role-Based Access Control (RBAC)**: In this type of access control, users are assigned roles that define their level of access to resources. RBAC is commonly used in enterprise systems, where users have different levels of authority based on their job responsibilities. That’s the essence of RBAC - assigning access based on a person’s role within an organization.
4. **Attribute-Based Access Control (ABAC)**: In this type of access control, access to resources is determined by a set of attributes, such as user role, time of day, location, and device. ABAC is commonly used in cloud environments and web applications.

Implementing access control can help prevent security breaches and unauthorized access to sensitive data. However, access control is not foolproof and can be vulnerable to various types of attacks, such as privilege escalation and broken access control vulnerabilities. Therefore, it is important to regularly review and test access control mechanisms to ensure that they are working as intended.

---

### Broken Access Control:

Broken access control vulnerabilities refer to situations where access control mechanisms fail to enforce proper restrictions on user access to resources or data. 

Here are some common exploits for broken access control and examples:

1. **Horizontal privilege escalation** occurs when an attacker can access resources or data belonging to other users with the same level of access.
   - For example, a user might be able to access another user’s account by changing the user ID in the URL.
2. **Vertical privilege escalation** occurs when an attacker can access resources or data belonging to users with higher access levels.
   - For example, a regular user can access administrative functions by manipulating a hidden form field or URL parameter.
3. **Insufficient access control** checks occur when access control checks are not performed correctly or consistently, allowing an attacker to bypass them.
   - For example, an application might allow users to view sensitive data without verifying their proper permissions.
4. **Insecure direct object references** occur when an attacker can access a resource or data by exploiting a weakness in the application’s access control mechanisms.
   - For example, an application might use predictable or easily guessable identifiers for sensitive data, making it easier for an attacker to access.

These exploits can be prevented by implementing strong access control mechanisms and regularly reviewing and testing them to ensure they are functioning as intended.

---

### Answer the questions below

1. What is IDOR?

Insecure Direct Object Reference

2. What occurs when an attacker can access resources or data belonging to other users with the same level of access?

Horizontal privilege escalation

3. What occurs when an attacker can access resources or data from users with higher access levels?

Vertical privilege escalation

4. What is ABAC?

Attribute-Based Access Control 

5. What is RBAC?

Role-Based Access Control

## Deploy the Machine

Start the Lab Machine and as I am using my Kali Linux Machine, we will connect to the TryHackMe Server by OpenVPN.

Connect to the TryHackMe Server by: `sudo openvpn FILENAME`

You can check how to connect through OpenVPN by this room: [OpenVPN](https://tryhackme.com/room/openvpn)

You can now start accessing the target website application by entering `http://TARGET_IP/` into the browser.

<img width="609" height="215" alt="image" src="https://github.com/user-attachments/assets/5af2dbb1-399e-46c5-b78b-63e0ab02f5ac" />

## Accessing the Web Application

### Assessing the Application:

When you browse a web application as a penetration tester, imagine what the underlying code looks like and what vulnerabilities come to mind for each functionality, request, and response.

The web application for this room features a Dashboard, Login, and Registration form that enables users to access the dashboard of the website. From a web app pentester standpoint, the pentester will usually register an account. After the registration, the pentester will then try to check the login function for any access control vulnerabilities.

In order for us to capture the HTTP requests being sent to the server, we can use [OWASP ZAP](https://www.zaproxy.org/) or Burp Suite Community Edition.

---

### Capturing the HTTP traffic

In order for us to further analyze the requests and responses being sent and received from the server, we will use the “Proxy” module of Burp Suite to capture the HTTP traffic that is being sent to the server. The captured HTTP traffic can be used with the other modules of Burp Suite.

These can then be manipulated or sent to other tools, such as “Repeater”, for further processing before being allowed to continue to their destination. 

Below is the captured HTTP traffic that is being sent to `functions.php` after login.

<img width="1608" height="390" alt="image" src="https://github.com/user-attachments/assets/13561db9-c04c-4042-8240-60af2e9cd3b4" />

Based on the screenshot displayed above, we can observe that upon completing the login process, the web application will give us a JSON response that contains the status, message, first_name, last_name, is_admin, and redirect_link which the server uses to redirect the user to the dashboard.php with the parameter “isadmin” in the URL.

---

### Understanding the content of the HTTP request and response:

- The target web application does not have any implemented security headers, which indicates that there are no preventative measures (like a first line of defense) in place to protect the web application against certain types of attacks.
- The target web application is running on a Linux operating system (`Debian`) and is using Apache web server (`Apache/2.4.38`). This information can be useful in identifying potential security vulnerabilities that may exist in the target web application.
- The target web application utilizes `PHP/8.0.19` as its backend programming language. This information is important for understanding the technology stack of the application and identifying potential security vulnerabilities or compatibility issues that may arise with other software components.
- The target web application redirects the user to the dashboard with a parameter that we can possibly test for privilege escalation vulnerabilities.

---

### Opening Burp Suite

First open Burp Suite, then go to the "Proxy" Section.

Click "Open Browser" then go the `http://TARGET_IP/` where you will first Register yourself.

Then at the Login Page, first click in Burp Suite "Intercept on", then Login with your credentials, you will get your request in Burp Suite.

Click "Intecept off" to finish off the request, then go to the "HTTP history" section in Proxy, where you can see the process.

<img width="797" height="128" alt="image" src="https://github.com/user-attachments/assets/7e932af4-4161-45be-9678-cda16b94d3c4" />

Where you can see that first it goes to `index.php` for the registration and then `login.php` and then `functions.php` having the JSON response and then finally `dashboard.php` after successful login.

---

### Answer the questions below

1. What is the type of server that is hosting the web application? This can be found in the response of the request in Burp Suite.

Apache

You can see any request page, where you can see `Server: Apache/2.4.38 (Debian)`

<img width="628" height="157" alt="image" src="https://github.com/user-attachments/assets/f03d2b71-27f5-4f35-86f1-8ec96f0ebfd7" />

2. What is the name of the parameter in the JSON response from the login request that contains a redirect link?

`redirect_link`

<img width="629" height="167" alt="image" src="https://github.com/user-attachments/assets/d2244ced-6455-4f54-bf6b-4dff820e4bf8" />

3. What Burp Suite module allows us to capture requests and responses between ourselves and our target?

Proxy

4. What is the admin’s email that can be found in the online users’ table?

`admin@admin.com`

<img width="419" height="352" alt="image" src="https://github.com/user-attachments/assets/9273660f-4764-4505-a116-6e953105f0e7" />









