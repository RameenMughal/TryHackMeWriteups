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

## A07: Authentication Failures

Authentication Failures happen when an application can’t reliably verify or bind a user’s identity. Common issues include:
- username enumeration
- weak/guessable passwords (no lockout/rate limits)
- logic flaws in the login/registration flow
- insecure session or cookie handling

If any of these are present, an attacker can often log in as someone else or bind a session to the wrong account.

To bind a session means linking (associating) a session with a specific user's identity.

For example:
- You visit example.com.
- You log in as User.
- The server creates Session ID = ABC123.
- The server binds ABC123 to your account.
- Every time your browser sends ABC123, the server knows: This is your account.

If you want more depth or broader techniques (e.g., brute force, session handling, cookies/JWT/OAuth, and MFA specifics), work through these after this room: [Authentication Module](https://tryhackme.com/module/authentication)

---

### Answer the questions below

What is the flag on the `admin` user's dashboard?

<img width="1033" height="654" alt="image" src="https://github.com/user-attachments/assets/74ed61c5-339f-4038-8eae-595042dc9458" />

## A09: Logging & Alerting Failures

When applications don’t record or alert on security-relevant events, defenders can’t detect or investigate attacks. Good logging underpins accountability (being able to prove who did what, when, and from where). In practice, failures look like missing authentication events, vague error logs, no alerting on brute-force or privilege changes, short retention, or logs stored where attackers can tamper with them.

Short retention means that logs are kept for only a short period of time before they are deleted or overwritten.

---

### Answer the questions below

1. It looks like an attacker tried to perform a brute-force attack, what is the IP of the attacker?

`203.0.113.45`

<img width="501" height="270" alt="image" src="https://github.com/user-attachments/assets/4eeaa285-29fd-4bb2-aed7-7f64b167f5a8" />

2. Looks like they were able to gain access to an account! What is the username associated with that account?

`admin`

3. What action did the attacker try to do with the account? List the endpoint the accessed.

`/supersecretadminstuff`

<img width="490" height="307" alt="image" src="https://github.com/user-attachments/assets/060c23a2-4d2f-4f00-860c-fa2ca61f6fc6" />

## Conclusion

The big ideas to keep:
- **A01 Broken Access Control**: Enforce server-side checks on every request
- **A07 Authentication Failures**: Enforce unique indexes on the canonical form, rate-limit/lock out brute force, and rotate sessions on password/privilege changes.
- **A09 Logging & Alerting Failures**: Log the full auth lifecycle (fail/success, password/2FA/role changes, admin actions), centralise logs off-host with retention, and alert on anomalies (e.g., brute-force bursts, privilege elevation).

