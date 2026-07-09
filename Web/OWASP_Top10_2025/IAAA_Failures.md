# OWASP Top 10 2025: IAAA Failures

Room: [OWASP Top 10 2025: IAAA Failures](https://tryhackme.com/room/owasptopten2025one)

<img width="932" height="191" alt="image" src="https://github.com/user-attachments/assets/b066e835-0e77-4fa7-8681-4e1d43a5f8b9" />

## Introduction

This room breaks down 3 of the OWASP Top 10 2025 categories. In this room, you will learn about the categories that are related to failures in how Identity, Authentication, Authorisation, and Accountability (IAAA) is implemented in the application. 

The following categories are covered in this room:
- A01: Broken Access Control
- A07: Authentication Failures
- A09: Logging & Alerting Failures

## What is IAAA?

IAAA is a simple way to think about how users and their actions are verified on applications. Each item plays a crucial role and it isn't possible to skip a level. The four items are:
- Identity - the unique account (e.g., user ID/email) that represents a person or service.
- Authentication - proving that identity (passwords, OTP, passkeys).
- Authorisation - what that identity is allowed to do.
- Accountability - recording and alerting on who did what, when, and from where.

The three categories of OWASP Top 10:2025 discussed in this room relates to failures in how IAAA was implemented. 

---

### Answer the questions below

What does IAAA stand for?

Identity, Authentication, Authorisation, Accountability

## A01: Broken Access Control

Broken Access Control happens when the server doesn’t properly enforce who can access what on every request. A common occurence of this is IDOR (Insecure Direct Object Reference): if changing an ID (like `?id=7` → `?id=6`) lets you see or edit someone else’s data, access control is broken.

In practice this shows up as horizontal privilege escalation (same role, other user’s stuff) or vertical privilege escalation (jumping to admin-only actions) because the application trusts the client too much.

Room to learn more about this: [Broken Access Control](https://tryhackme.com/room/owaspbrokenaccesscontrol)

---

### Answer the questions below

1. If you don't get access to more roles but can view the data of another users, what type of privilege escalation is this?

Horizontal

2. What is the note you found when viewing the user's account who had more than $ 1 million?

<img width="1023" height="843" alt="image" src="https://github.com/user-attachments/assets/83164b17-0943-4a35-915f-eb2af4051953" />


