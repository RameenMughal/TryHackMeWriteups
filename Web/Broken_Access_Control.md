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



