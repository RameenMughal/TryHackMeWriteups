# Advanced SQL Injection

Room: [Advanced SQL Injection](https://tryhackme.com/room/advancedsqlinjection)

Prerequisites:
1. [SQL Injection](https://tryhackme.com/room/sqlinjectionlm)
2. [SQLMAP](https://tryhackme.com/room/sqlmap)
3. [OWASP Top 10 (2025)](https://tryhackme.com/module/owasp-top-10-2025)
4. [Nmap](https://tryhackme.com/room/furthernmap)

<img width="941" height="203" alt="image" src="https://github.com/user-attachments/assets/90622ad5-eee0-4b6e-9d6d-d698ac816e83" />

## Introduction

SQL injection remains one of web applications' most severe and widespread security vulnerabilities. This threat arises when an attacker exploits a web application's ability to execute arbitrary SQL queries, leading to unauthorised access to the database, data exfiltration, data manipulation, or even complete control over the application. 

---

### Connecting to the Machine

You can start the lab machine by clicking the `Start Lab Machine` button attached to this task. You may access the VM using the AttackBox or your VPN connection.

I am using my Kali Linux machine by connecting through OpenVPN Command: `sudo openvpn FILENAME`

You can refer to how to connect through OpenVPN by this room: [OpenVPN](https://tryhackme.com/room/openvpn)

Before diving in, it's crucial to clearly understand the lab machine's database version and operating system details. To achieve this, we can utilise Nmap, a powerful network scanning tool, to thoroughly scan the `MACHINE_IP`. This scan will provide valuable insights into the open ports, running services, and the lab machine's operating system.

Firstly identifying the open ports in the Machine: `nmap MACHINE_IP`

<img width="340" height="169" alt="image" src="https://github.com/user-attachments/assets/9abc6cbf-94f9-4a53-ab9d-1a8a97009745" />

Now doing aggresive scan: `nmap -A -T4 -p 3306,3389,445,139,135 MACHINE_IP`

```
Starting Nmap 7.99 ( https://nmap.org ) at 2026-08-25 12:36 -0400
Nmap scan report for 10.48.164.234
Host is up (0.071s latency).

PORT     STATE SERVICE       VERSION
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
3306/tcp open  mysql         MariaDB 10.3.23 or earlier (unauthorized)
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=SQLi
| Not valid before: 2026-08-24T16:32:26
|_Not valid after:  2027-02-23T16:32:26
|_ssl-date: 2026-08-25T16:37:16+00:00; 0s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: SQLI
|   NetBIOS_Domain_Name: SQLI
|   NetBIOS_Computer_Name: SQLI
|   DNS_Domain_Name: SQLi
|   DNS_Computer_Name: SQLi
|   Product_Version: 10.0.17763
|_  System_Time: 2026-08-25T16:37:08+00:00
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Microsoft Windows 10 1709 - 22H2 (97%), Microsoft Windows Server 2019 (96%), Microsoft Windows Server 2016 (95%), Microsoft Windows 10 1903 (93%), Microsoft Windows 11 24H2 - 25H2 (93%), Microsoft Windows 10 1803 (92%), Microsoft Windows Server 2012 (92%), Microsoft Windows Server 2022 (92%), Microsoft Windows Vista SP1 (92%), Microsoft Windows 10 (92%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 3 hops
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2026-08-25T16:37:10
|_  start_date: N/A

TRACEROUTE (using port 3389/tcp)
HOP RTT      ADDRESS
1   53.35 ms 192.168.128.1
2   ...
3   53.92 ms 10.48.164.234

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 33.68 seconds
```

`-A` means Aggresive Scan which does several advanced Nmap detection features at once:
- OS detection — tries to identify the target's operating system.
- Version detection — determines what software/services and their versions are running.
- Default NSE (Nmap Scripting Engine) scripts — runs Nmap's default scripts to gather additional information.
- Traceroute — attempts to determine the network path to the target.

And then the interesting ports were selected to do further scan on them.

The machine is using MySQL service on Windows.

---

### Answer the questions below

What is the port on which MySQL service is running?

3306

## Quick Recap

In the last SQL injection room, we explored the basics of SQL injection, understanding how attackers exploit vulnerabilities in web applications to manipulate SQL queries and access unauthorised data. We covered essential techniques, such as error-based and union-based SQL injection, and blind SQL injection methods, such as boolean-based and time-based attacks. 

<img width="708" height="385" alt="image" src="https://github.com/user-attachments/assets/8380ab3d-97dc-4221-a45d-5fd909a3d608" />

---

### In-band SQL Injection

This technique is considered the most common and straightforward type of SQL injection attack. In this technique, the attacker uses the same communication channel for both the injection and the retrieval of data. There are two primary types of in-band SQL injection:
- **Error-Based SQL Injection**: The attacker manipulates the SQL query to produce error messages from the database. These error messages often contain information about the database structure, which can be used to exploit the database further.
  - Example: `SELECT * FROM users WHERE id = 1 AND 1=CONVERT(int, (SELECT @@version))`. If the database version is returned in the error message, it reveals information about the database.
- **Union-Based SQL Injection**: The attacker uses the UNION SQL operator to combine the results of two or more SELECT statements into a single result, thereby retrieving data from other tables.
  - Example: `SELECT name, email FROM users WHERE id = 1 UNION ALL SELECT username, password FROM admin`.

---

### Inferential (Blind) SQL Injection

Inferential SQL injection does not transfer data directly through the web application, making exploiting it more challenging. Instead, the attacker sends payloads and observes the application’s behaviour and response times to infer information about the database. There are two primary types of inferential SQL injection:
- **Boolean-Based Blind SQL Injection**: The attacker sends an SQL query to the database, forcing the application to return a different result based on a true or false condition. By analysing the application’s response, the attacker can infer whether the payload was true or false.
  - Example: `SELECT * FROM users WHERE id = 1 AND 1=1` (true condition) versus `SELECT * FROM users WHERE id = 1 AND 1=2` (false condition). The attacker can infer the result if the page content or behaviour changes based on the condition.
- **Time-Based Blind SQL Injection**: The attacker sends an SQL query to the database, which delays the response for a specified time if the condition is true. By measuring the response time, the attacker can infer whether the condition is true or false.
  - For example, `SELECT * FROM users WHERE id = 1; IF (1=1) WAITFOR DELAY '00:00:05'--`. If the response is delayed by 5 seconds, the attacker can infer that the condition was true.
 
---

### Out-of-band SQL Injection

Out-of-band SQL injection is used when the attacker cannot use the same channel to launch the attack and gather results or when the server responses are unstable. This technique relies on the database server making an out-of-band request (e.g., HTTP or DNS) to send the query result to the attacker. HTTP is normally used in out-of-band SQL injection to send the query result to the attacker's server.

In-band SQL Injection is easy to exploit and detect but noisy and can be easily monitored. Inferential (Blind) SQL Injection is more challenging to exploit and requires multiple requests but can be used when detailed error messages are unavailable. Out-of-band SQL Injection is less common and highly effective, requires external server control, and relies on the database’s ability to make out-of-band requests. 

---

### Answer the questions below

1. What type of SQL injection uses the same communication channel for both the injection and data retrieval?

In-band

2. In out-of-band SQL injection, which protocol is usually used to send query results to the attacker's server?

HTTP

## Second-Order SQL Injection

Second-order SQL injection, also known as stored SQL injection, exploits vulnerabilities where user-supplied input is saved and subsequently used in a different part of the application, possibly after some initial processing. This type of attack is more insidious because the malicious SQL code does not need to immediately result in a SQL syntax error or other obvious issues, making it harder to detect with standard input validation techniques. The injection occurs upon the second use of the data when it is retrieved and used in a SQL command, hence the name "Second Order".

---

### Impact

The danger of Second-Order SQL Injection lies in its ability to bypass typical front-end defences like basic input validation or sanitisation, which only occur at the point of initial data entry. Since the payload does not cause disruption during the first step, it can be overlooked until it's too late, making the attack particularly stealthy.

**Example**

We will be using a book review application. The application allows users to add new books via a web page (`add.php`). Users are prompted to provide details about the book they wish to add to the database. You can access the app at `http://MACHINE_IP/second/add.php`. The data collected includes the `SSN`, `book_name`, and `author`.

<img width="248" height="283" alt="image" src="https://github.com/user-attachments/assets/215d43b4-9feb-4737-9194-2a5adb81f079" />

Let's consider adding a book with the following details: SSN: UI00012, Book Name: Intro to PHP, Author: Tim. This information is input through a form on the add.php page, and upon submission, it is stored in the BookStore database.

As we know, Second-Order SQL injection is notably challenging to identify. Unlike traditional SQL Injection, which exploits real-time processing vulnerabilities, it occurs when data previously stored in a database is later used in a SQL query. Detecting this vulnerability often requires understanding how data flows through the application and is reused, necessitating a deep knowledge of the backend operations.

**Analysis of the Code**

Consider the PHP code snippet used in our application for adding books:

```
if (isset($_POST['submit'])) {

    $ssn = $conn->real_escape_string($_POST['ssn']);

    $book_name = $conn->real_escape_string($_POST['book_name']);

    $author = $conn->real_escape_string($_POST['author']);

    $sql = "INSERT INTO books (ssn, book_name, author) VALUES ('$ssn', '$book_name', '$author')";

    if ($conn->query($sql) === TRUE) {

        echo "<p class='text-green-500'>New book added successfully</p>";

    } else {

        echo "<p class='text-red-500'>Error: " . $conn->error . "</p>";

    }

}
```

The code uses the `real_escape_string()` method to escape special characters in the inputs. While this method can mitigate some risks of immediate SQL Injection by escaping single quotes and other SQL meta-characters, it does not secure the application against Second Order SQLi. 

The key issue here is the lack of parameterised queries, which is essential for preventing SQL injection attacks. When data is inserted using the `real_escape_string()` method, it might include payload characters that don't cause immediate harm but can be activated upon subsequent retrieval and use in another SQL query. 

Parameterized queries (also called prepared statements) are a method of executing database queries where the SQL command structure is strictly separated from the user-provided data parameters. Instead of dynamically building an SQL query string by concatenating strings or inserting raw user input directly, parameterized queries use placeholders (`?` or named parameters like `:ssn`) for any data values.

For instance, inserting a book with a name like `Intro to PHP'; DROP TABLE books;--` might not affect the INSERT operation but could have serious implications if the book name is later used in another SQL context without proper handling.

Let's try adding another book with the SSN `test'`.

<img width="563" height="332" alt="image" src="https://github.com/user-attachments/assets/6c75df8c-60fe-4837-a0a4-4d8d8eedc150" />

Here we go, the SSN `test'` is successfully inserted into the database. The application includes a feature to update book details through an interface like `update.ph`p. This interface might display existing book details in editable form fields, retrieved based on earlier stored data, and then update them based on user input. 

The pentester would investigate whether the application reuses the data (such as `book_name`) that was previously stored and potentially tainted. Then, he would construct SQL queries for updating records using this potentially tainted data without proper sanitisation or parameterisation. By manipulating the update feature, the tester can see if the malicious payload added during the insertion phase gets executed during the update operation. If the application fails to employ proper security practices at this stage, the earlier injected payload `'; DROP TABLE books; --` could be activated, leading to the execution of a harmful SQL command like dropping a table. 

You can visit the page `http://MACHINE_IP/second/update.php` to update any book details.

<img width="737" height="335" alt="image" src="https://github.com/user-attachments/assets/4df1600d-4e58-4168-bd5c-24b280463553" />

Now, let's review the `update.php` code. The PHP script allows users to update book details within the BookStore database. 

Through the query structure, we will analyse a typical scenario where a penetration tester might look for SQL injection vulnerabilities, specifically focusing on how user inputs are handled and utilised in SQL queries. 

```
 if ( isset($_POST['update'])) {
    $unique_id = $_POST['update'];
    $ssn = $_POST['ssn_' . $unique_id];
    $new_book_name = $_POST['new_book_name_' . $unique_id];
    $new_author = $_POST['new_author_' . $unique_id];

    $update_sql = "UPDATE books SET book_name = '$new_book_name', author = '$new_author' WHERE ssn = '$ssn'; INSERT INTO logs (page) VALUES ('update.php');";
```

The script begins by checking if the request method is POST and if the update button was pressed, indicating that a user intends to update a book's details. Following this, the script retrieves user inputs directly from the POST data:

```
     $unique_id = $_POST['update'];
    $ssn = $_POST['ssn_' . $unique_id];
    $new_book_name = $_POST['new_book_name_' . $unique_id];
    $new_author = $_POST['new_author_' . $unique_id];
```

These variables (`ssn`, `new_book_name`, `new_author`) are then used to construct an SQL query for updating the specified book's details in the database:

```
 $update_sql = "UPDATE books SET book_name = '$new_book_name', author = '$new_author' WHERE ssn = '$ssn'; INSERT INTO logs (page) VALUES ('update.php');";
```

The script uses` multi_query` to execute multiple queries. It also inserts logs into the logs table for analytical purposes.

---

### Preparing the Payload

We know that we can add or modify the book details based on their ssn. The normal query for updating a book might look like this:

```
 UPDATE books SET book_name = '$new_book_name', author = '$new_author' WHERE ssn = '123123';
```

However, the SQL command could be manipulated if an attacker inserts a specially crafted `ssn` value. For example, if the attacker uses the `ssn` value:

```
12345'; UPDATE books SET book_name = 'Hacked'; --
```

When this value is used in the update query, it effectively ends the initial update command after `12345` and starts a new command. This would change the `book_name` of all entries in the books table to Hacked.

**Let's do this**

**Initial Payload Insertion**: A new book is added with the payload `12345'; UPDATE books SET book_name = 'Hacked'; --` is inserted as the `ssn`. The semicolon (`;`) will be used to terminate the current SQL statement.

<img width="238" height="153" alt="image" src="https://github.com/user-attachments/assets/41911d3d-a126-4fc0-a27d-d3cc3866a7c9" />

**Malicious SQL Execution**: After that, when the admin or any other user visits the URL `http://MACHINE_IP/second/update.php` and updates the book, the inserted payload breaks out of the intended SQL command structure and injects a new command that updates all records in the books table. 

Let's visit the page  `http://MACHINE_IP/second/update.php` page, update the book name to anything, and click the Update button. The code will execute the following statement in the backend.

```
UPDATE books SET book_name = 'Testing', author = 'Hacker' WHERE ssn = '12345'; Update books set book_name ="hacked"; --'; INSERT INTO logs (page) VALUES ('update.php');
```

**Commenting Out the Rest**: The double dash (`--`) is an SQL comment symbol. Anything following `--` will be ignored by the SQL server, effectively neutralising any remaining parts of the original SQL statement that could cause errors or reveal the attack. Once the above query is executed, it will change the name of all the books to hacked, as shown below:

<img width="233" height="145" alt="image" src="https://github.com/user-attachments/assets/a7f270cb-5aa2-4893-a839-2f20b3b7f153" />

---

### Answer the questions below

1. What is the flag value after updating the title of all books to "compromised"?

Updating the SQL Query for `ssn`: `12345'; UPDATE books SET book_name = 'compromised'; --`

Adding this in `ssn` and adding a book:

<img width="234" height="178" alt="image" src="https://github.com/user-attachments/assets/2743a0a4-f54e-4d95-b36b-84a1515df54d" />

Updating the book name then we get the flag:

<img width="636" height="418" alt="image" src="https://github.com/user-attachments/assets/1dffe6f7-e5cd-4340-a36c-4dd4f087dae0" />

2. What is the flag value once you drop the table hello from the database?

SQL Query as `ssn`: `12345'; DROP TABLE hello; --`

<img width="237" height="214" alt="image" src="https://github.com/user-attachments/assets/56e40619-98a3-40a1-a20c-296d64a8b141" />

Then update the book name, you get the flag:

<img width="643" height="403" alt="image" src="https://github.com/user-attachments/assets/559f98a8-eee0-48c4-bd1d-67ed48023b06" />

## Filter Evasion Techniques

In advanced SQL injection attacks, evading filters is crucial for successfully exploiting vulnerabilities. 

Statement “evading filters is crucial” it means bypassing input restrictions/security filters so that the intended SQL injection reaches and is processed by the database.

Modern web applications often implement defensive measures to sanitise or block common attack patterns, making simple SQL injection attempts ineffective. As pentesters, we must adapt using more sophisticated techniques to bypass these filters.

Even if a web application has strong checks that try to prevent attacks, understanding filter-evasion techniques can help an attacker find ways around those checks.

---

### Character Encoding

Character encoding involves converting special characters in the SQL injection payload into encoded forms that may bypass input filters.

**URL Encoding**: URL encoding is a common method where characters are represented using a percent (`%`) sign followed by their ASCII value in hexadecimal. 

For example, the payload `' OR 1=1--` can be encoded as `%27%20OR%201%3D1--`. This encoding can help the input pass through web application filters and be decoded by the database, which might not recognise it as malicious during initial processing.

**Hexadecimal Encoding**: Hexadecimal encoding is another effective technique for constructing SQL queries using hexadecimal values. 

For instance, the query `SELECT * FROM users WHERE name = 'admin'` can be encoded as `SELECT * FROM users WHERE name = 0x61646d696e`. By representing characters as hexadecimal numbers, the attacker can bypass filters that do not decode these values before processing the input.

**Unicode Encoding**: Unicode encoding represents characters using Unicode escape sequences. 

For example, the string `admin` can be encoded as `\u0061\u0064\u006d\u0069\u006e`. This method can bypass filters that only check for specific ASCII characters, as the database will correctly process the encoded input.

**Example**

In this example, we explore how developers can implement basic filtering to prevent SQL injection attacks by removing specific keywords and characters from user input. However, we will also see how attackers can bypass these defences using character encoding techniques like URL encoding.

You can access the page at `http://10.48.172.223/encoding/`.

<img width="353" height="104" alt="image" src="https://github.com/user-attachments/assets/fdb39db7-190b-4a41-bbcc-245b9bf96034" />

Here's the PHP code (`search_books.php`) that handles the search functionality:

```
$book_name = $_GET['book_name'] ?? '';
$special_chars = array("OR", "or", "AND", "and" , "UNION", "SELECT");
$book_name = str_replace($special_chars, '', $book_name);
$sql = "SELECT * FROM books WHERE book_name = '$book_name'";
echo "<p>Generated SQL Query: $sql</p>";
$result = $conn->query($sql) or die("Error: " . $conn->error . " (Error Code: " . $conn->errno . ")");
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
```

In the above example, the developer has implemented a basic defence mechanism to prevent SQL injection attacks by removing specific SQL keywords, such as `OR`, `AND`, `UNION`, and `SELECT`. The filtering uses the `str_replace` function, which strips these keywords from the user input before they are included in the SQL query. This filtering approach aims to make it harder for attackers to inject malicious SQL commands, as these keywords are essential for many SQL injection payloads.

Here's the Javascript code in the index.html page that provides the user interface for searching books:



This `searchBooks()` function takes the book name entered by the user from the `book_name` input box, creates a request using XMLHttpRequest, and sends the book name to `search_books.php` using a GET request. `encodeURIComponent()` safely encodes the book name for use in the URL.


        





