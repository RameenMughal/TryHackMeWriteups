# Insecure Deserialisation

Room: [Insecure Deserialisation](https://tryhackme.com/room/insecuredeserialisation)

Module Prerequisite: [OWASP Top 10 (2025)](https://tryhackme.com/module/owasp-top-10-2025)

<img width="943" height="206" alt="image" src="https://github.com/user-attachments/assets/ac450169-ba85-40a9-8859-0398647d22af" />

## Introduction

User-supplied input has consistently been a catalyst for vulnerabilities, posing persistent threats across numerous platforms and applications. Exploiting user input, from SQL injection to cross-site scripting, is a well-known challenge in securing web applications. Another less understood but equally dangerous vulnerability associated with user input is insecure deserialisation. 

Insecure deserialisation exploits occur when an application trusts serialised data enough to use it without validating its authenticity. 

Serialized data is data that has been converted from a complex in-memory format (such as an object, array, or data structure in programming) into a standardized, flat format—like a string of text or a stream of bytes—so that it can be easily stored or transmitted.

This trust can lead to disastrous outcomes as attackers manipulate serialised objects to achieve remote code execution, escalate privileges, or launch denial-of-service attacks. This type of vulnerability is prevalent in applications that serialise and deserialise complex data structures across various programming environments, such as Java, .NET, and PHP, which often use serialisation for remote procedure calls, session management, and more.

---

### Connecting to the Machine

You can start the lab machine by clicking the `Start Lab Machine` button attached in this task. We use a vulnerable application later in the room to practically perform the exercise and become familiar with various attack vectors.

I am using my Kali Linux Machine as an Attack Machine and connecting to TryHackMe Server by OpenVPN.

You can check the [OpenVPN](https://tryhackme.com/room/openvpn) room to see how to connect through your machine.

OpenVPN Command: `sudo openvpn <FILENAME>`

## Some Important Concepts

### Serialisation

Think of serialisation, like packing your school bag in the morning. You have books, notebooks, a lunchbox, and a water bottle, which you need to organise into your bag. Serialisation is just like taking different pieces of information (like notes) and putting them together to make them easy to store or send to a friend. 

In programming, serialisation is the process of transforming an object's state into a human-readable or binary format (or a mix of both) that can be stored or transmitted and reconstructed as and when required. This capability is essential in applications where data must be transferred between different parts of a system or across a network, such as in web-based applications. In PHP, this process is performed using the `serialize()` function.

**Example**

```
<?php
$noteArray = array("title" => "My THM Note", "content" => "Welcome to THM!");
$serialisedNote = serialize($noteArray);  // Converting the note into a storable format
file_put_contents('note.txt', $serialisedNote);  // Saving the serialised note to a file
?>
```

The following output shows the serialised string in the `note.txt` file, which includes details of the note's structure and content. It’s stored in a way that can be easily saved or transmitted.

Serialised Note: `a:2:{s:5:"title";s:12:"My THM Note";s:7:"content";s:12:"Welcome to THM!";}`

---

### Deserialisation

Imagine you arrive at school and need everything you packed this morning. Deserialisation is like unpacking your school bag when you get to class; you take out each item so you can use it throughout the day. As you unpack your bag to get your books and lunch, deserialisation takes the packed-up data and turns it back into something you can use. Deserialisation is the process of converting the formatted data back into an object. It's crucial for retrieving data from files, databases, or across networks, restoring it to its original state for usage in applications.

Following our previous example, here's how you might deserialise the note data in PHP:

```
<?php
$serialisedNote = file_get_contents('note.txt');  // Reading the serialised note from the file
$noteArray = unserialize($serialisedNote);  // Converting the serialised string back into a PHP array
echo "Title: " . $noteArray['title'] . "<br>";
echo "Content: " . $noteArray['content'];
?>
```

This code reads the serialised note from a file and converts it back into an array, effectively reconstructing the original note. 

Discussing serialisation also necessitates a conversation about security. Like you wouldn’t want someone tampering with your school bag, insecure deserialisation can lead to significant security vulnerabilities in software applications. Attackers might alter serialised objects to execute unauthorised actions or steal data.

---

### Specific Incidents Involving Serialisation Vulnerabilities

Let's discuss specific incidents where serialisation vulnerabilities played a critical role in cyber security breaches or attacks, highlighting the importance of secure serialisation practices. These examples illustrate how attackers exploit serialisation flaws to achieve remote code execution, data leakage, and more.

**Log4j Vulnerability CVE-2021-44228**

- **Incident**: The [Log4j vulnerability](https://nvd.nist.gov/vuln/detail/cve-2021-44228), or Log4Shell, is a critical security flaw found in the Apache Log4j 2 library, a widely used logging library in Java applications. The vulnerability allows remote attackers to execute arbitrary code on affected systems by exploiting the library's insecure deserialisation functionality.
- **Impact**: The vulnerability facilitated remote code execution, enabling attackers to execute arbitrary commands on affected systems. This allowed attackers to compromise critical infrastructure, leading to unauthorised access to sensitive data, service disruptions, and potential supply chain attacks.

**WebLogic Server Remote Code Execution CVE-2015-4852**
- **Incident**: This vulnerability was related to how the [Oracle WebLogic Server](https://www.oracle.com/security-alerts/alert-cve-2015-4852.html) deserialised data was sent to the T3 protocol. Attackers could send maliciously crafted objects to the server, which, when deserialised, led to remote code execution.
- **Impact**: This vulnerability was widely exploited to gain unauthorised access to systems, deploy ransomware, or steal data. It affected all versions of the WebLogic Server that had not disabled the vulnerable service or patched the issue.

The T3 protocol is Oracle WebLogic Server's proprietary, high-performance transport layer used to transmit data between WebLogic Server instances and other Java programs, including external Java clients.

**Jenkins Java Deserialisation CVE-2016-0792**
- **Incident**: [Jenkins](https://www.tenable.com/plugins/nessus/89034), a popular automation server used in software development, experienced a critical vulnerability involving Java deserialisation. Attackers could send crafted serialisation payloads to the Jenkins CLI, which, when deserialised, could allow arbitrary code execution.
- **Impact**: This allowed attackers to execute shell commands, potentially taking over the Jenkins server, which often has broad access to a software development environment, including source code, build systems, and potentially deployment environments.

---

### Answer the questions below

1. What is the function used in PHP for serialisation?

`serialize()`

2. What is the base score for the vulnerability CVE-2015-4852?

7.5

3. Does serialisation allow only saving to a byte stream file? (yea/nay)

nay






