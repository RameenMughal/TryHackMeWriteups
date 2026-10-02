# Insecure Deserialisation

Room: [Insecure Deserialisation](https://tryhackme.com/room/insecuredeserialisation)

Module Prerequisite: [OWASP Top 10 (2025)](

<img width="943" height="206" alt="image" src="https://github.com/user-attachments/assets/ac450169-ba85-40a9-8859-0398647d22af" />

## Introduction

User-supplied input has consistently been a catalyst for vulnerabilities, posing persistent threats across numerous platforms and applications. Exploiting user input, from SQL injection to cross-site scripting, is a well-known challenge in securing web applications. Another less understood but equally dangerous vulnerability associated with user input is insecure deserialisation. 

Insecure deserialisation exploits occur when an application trusts serialised data enough to use it without validating its authenticity. 

Serialized data is data that has been converted from a complex in-memory format (such as an object, array, or data structure in programming) into a standardized, flat format—like a string of text or a stream of bytes—so that it can be easily stored or transmitted.

This trust can lead to disastrous outcomes as attackers manipulate serialised objects to achieve remote code execution, escalate privileges, or launch denial-of-service attacks. This type of vulnerability is prevalent in applications that serialise and deserialise complex data structures across various programming environments, such as Java, .NET, and PHP, which often use serialisation for remote procedure calls, session management, and more.
