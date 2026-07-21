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

## Exploiting the Web Application

In the previous task, we learned that the file functions.php returns a JSON response upon login. The response contains a `redirect_link` with a parameter that we can test for access control vulnerabilities.

To start testing for this vulnerability, we can intercept the HTTP response and copy the value of the redirect_link parameter to our address bar. `http://TARGET_IP/dashboard.php?isadmin=false`

Since the application redirects the user to dashboard.php while the JSON response can only be seen by intercepting using a proxy tool, we can try changing the parameter’s value from “false” to “true” or vice versa. `http://TARGET_IP/dashboard.php?isadmin=true`

Upon changing the value from false to true, application redirects us to `admin.php`, which is hidden to a normal user by default. Below is the HTTP request that is captured using Burp Suite Proxy.

<img width="630" height="287" alt="image" src="https://github.com/user-attachments/assets/46d845cb-154b-431a-b24a-db18ee6e320f" />

<img width="1684" height="406" alt="image" src="https://github.com/user-attachments/assets/c81a7037-b78e-458c-9756-8b52aacd87f7" />

Since we have access to admin.php using a low-privilege account, we might as well check for a vertical privilege escalation attack.

Checking the box in the “Admin access” column of the account you registered and clicking the “Save Changes” button will give us admin privileges. Which in return enables us to revoke the access of other admin users.

<img width="850" height="136" alt="image" src="https://github.com/user-attachments/assets/20814d47-7b20-4b48-be15-a9bf042a03d0" />

---

### Answer the questions below

1. What kind of privilege escalation happened after accessing admin.php?

Vertical

2. What parameter allows the attacker to access the admin page?

`isadmin`

3. What is the flag in the admin page?

Screenshot provided above after accessing the `admin.php`

## Mitigation

There are several steps that can be taken to mitigate the risk of broken access control vulnerabilities in PHP applications:

### 1. Implement Role-Based Access Control (RBAC)

Role-based access control (RBAC) is a method of regulating access to computer or network resources based on the roles of individual users within an enterprise. By defining roles in an organization and assigning access rights to these roles, you can control what actions a user can perform on a system. 

The provided code snippet illustrates how you can define roles (such as ‘admin’, ‘editor’, or ‘user’) and the permissions associated with them. The `hasPermission` function checks if a user of a certain role has a specified permission.

```
// Define roles and permissions
 $roles = [
     'admin' => ['create', 'read', 'update', 'delete'],
     'editor' => ['create', 'read', 'update'],
     'user' => ['read'],
 ];

 // Check user permissions
 function hasPermission($userRole, $requiredPermission) {
     global $roles;
     return in_array($requiredPermission, $roles[$userRole]);
 }

 // Example usage
 if (hasPermission('admin', 'delete')) {
     // Allow delete operation
 } else {
     // Deny delete operation
 }
```

---

### 2. Use Parameterized Queries 

Parameterized queries are a way to protect PHP applications from SQL Injection attacks, where malicious users could potentially gain unauthorized access to your database. By using placeholders instead of directly including user input into the SQL query, you can significantly reduce the risk of SQL Injection attacks. 

The provided example demonstrates how a query can be made secure using prepared statements, which separates SQL syntax from data and handles user input safely.

```
// Example of vulnerable query
 $username = $_POST['username'];
 $password = $_POST['password'];
 $query = "SELECT * FROM users WHERE username='$username' AND password='$password'";

 // Example of secure query using prepared statements
 $username = $_POST['username'];
 $password = $_POST['password'];
 $stmt = $pdo->prepare("SELECT * FROM users WHERE username=? AND password=?");
 $stmt->execute([$username, $password]);
 $user = $stmt->fetch();
```

---

### 3. Proper Session Management 

Proper session management ensures that authenticated users have timely and appropriate access to resources, thereby reducing the risk of unauthorized access to sensitive information. Session management includes using secure cookies, setting session timeouts, and limiting the number of active sessions a user can have. 

The code snippet shows how to initialize a session, set session variables and check for session validity by looking at the last activity time.

```
// Start session
 session_start();

 // Set session variables
 $_SESSION['user_id'] = $user_id;
 $_SESSION['last_activity'] = time();

 // Check if session is still valid
 if (isset($_SESSION['last_activity']) && (time() - $_SESSION['last_activity'] > 1800)) {
     // Session has expired
     session_unset();
     session_destroy();
 }
```

---

### 4. Use Secure Coding Practices 

Secure coding practices involve methods to prevent the introduction of security vulnerabilities. Developers should sanitize and validate user input to prevent malicious data from causing harm and avoid using insecure functions or libraries. 

The given example shows how to sanitize user input using PHP’s `filter_input` function and demonstrates how to securely hash a password using `password_hash` instead of an insecure function like `md5`.

```
// Validate user input
 $username = filter_input(INPUT_POST, 'username', FILTER_SANITIZE_STRING);
 $password = filter_input(INPUT_POST, 'password', FILTER_SANITIZE_STRING);

 // Avoid insecure functions
 // Example of vulnerable code using md5
 $password = md5($password);
 // Example of secure code using password_hash
 $password = password_hash($password, PASSWORD_DEFAULT);
```

## Conclusion

Broken access control is a security vulnerability that occurs when a system fails to properly enforce access controls, which can result in unauthorized users gaining access to sensitive information or performing actions they are not authorized to do.

Horizontal privilege escalation occurs when a user is able to access data or perform actions that they are not authorized to do within their own privilege level. This can be dangerous because it can allow an attacker who has already gained access to the system to move laterally through the network and access additional resources or sensitive data.

Vertical privilege escalation occurs when a user is able to gain access to data or perform actions that are reserved for users with higher privilege levels, such as system administrators. This can be even more dangerous because it can allow an attacker to gain full control of the system and potentially take over the entire network.

Here are some references that you can give to PHP developers to help them implement these mitigation strategies:
1. [OWASP PHP Configuration Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/PHP_Configuration_Cheat_Sheet.html)
2. [PHP The Right Way: Security](https://phptherightway.com/#security)
3. [Secure Coding in PHP](https://www.php.net/manual/en/security.php)












