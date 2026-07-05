# Security Principles

Room: [Security Principles](https://tryhackme.com/room/securityprinciples)

<img width="944" height="196" alt="image" src="https://github.com/user-attachments/assets/7c1de141-9dc3-447f-ba7d-0d2b2345b8cf" />

## CIA

When you want to judge the security of a system, you need to think in terms of the security triad: confidentiality, integrity, and availability (CIA).
- **Confidentiality** ensures that only the intended persons or recipients can access the data.
- **Integrity** aims to ensure that the data cannot be altered; moreover, we can detect any alteration if it occurs.
- **Availability** aims to ensure that the system or service is available when needed.

---

### Beyond CIA

Going one more step beyond the CIA security triad, we can think of:
- **Authenticity**: Authentic means not fraudulent or counterfeit. Authenticity is about ensuring that the document/file/data is from the claimed source.
- **Nonrepudiation**: Repudiate means refusing to recognize the validity of something. Nonrepudiation ensures that the original source cannot deny that they are the source of a particular document/file/data. This feature is very important in areas like online shopping, hospitals, and banks.

These two requirements are closely related. The need to tell authentic files or orders from fake ones is important. Moreover, ensuring that the other party cannot deny being the source is vital for many systems to be usable.

---

### Parkerian Hexad

In 1998, Donn Parker proposed the Parkerian Hexad, a set of six security elements. They are:
- Availability
- Utility
- Integrity
- Authenticity
- Confidentiality
- Possession

We have already covered four of the above six elements. Let's discuss the remaining two elements:
- **Utility**: Utility focuses on the usefulness of the information.
  - For example, a person may lose the password/key needed to open an encrypted laptop. Even though they still have the laptop and the files are still there, they cannot open or use them. In other words, although still available, the information is in a form that is not useful, i.e., of no utility.
- **Possession**: This means we must stop unauthorized people from taking, copying, or controlling our information.
  - For example, a hacker or thief may steal a backup drive, so we no longer have control of the information while they have it.
  - Another example is when a hacker locks our files with ransomware. We still have the files, but we cannot control or use them, so we lose possession of the data.

---

### Answer the questions below

1. Click on "View Site" and answer the five questions. What is the flag that you obtained at the end?

<img width="966" height="238" alt="image" src="https://github.com/user-attachments/assets/02c610a4-df8d-4fed-90f6-b5e49629ab6a" />

## DAD

The security of a system is attacked through one of several means. It can be via the disclosure of secret data, alteration of data, or destruction of data.
- **Disclosure** is the opposite of confidentiality. In other words, disclosure of confidential data would be an attack on confidentiality.
- **Alteration** is the opposite of Integrity. For example, the integrity of a cheque is indispensable.
- **Destruction/Denial** is the opposite of Availability.

The opposite of the CIA Triad would be the DAD Triad: Disclosure, Alteration, and Destruction.

Protecting against disclosure, alteration, and destruction/denial is of utter significance. This protection is equivalent to working to maintain confidentiality, integrity and availability.

Protecting confidentiality and integrity to an extreme can restrict availability, and increasing availability to an extreme can result in losing confidentiality and integrity. Good security principles implementation requires a balance between the three.

---

### Answer the questions below

1. The attacker managed to gain access to customer records and dumped them online. What is this attack?

Disclosure

2. A group of attackers were able to locate both the main and the backup power supply systems and switch them off. As a result, the whole network was shut down. What is this attack?

Destruction/Denial

## Fundamental Concepts of Security Models

We have learned that the security triad is represented by Confidentiality, Integrity, and Availability (CIA). One might ask, how can we create a system that ensures one or more security functions? The answer would be in using security models. In this task, we will introduce three foundational security models:

---

### Bell-LaPadula Model

The Bell-LaPadula Model aims to achieve confidentiality by specifying three rules:
- **Simple Security Property**: This property is referred to as “no read up”; it states that a subject at a lower security level cannot read an object at a higher security level. This rule prevents access to sensitive information above the authorized level.
- **Star Security Property**: This property is referred to as “no write down”; it states that a subject at a higher security level cannot write to an object at a lower security level. This rule prevents the disclosure of sensitive information to a subject of lower security level.
- **Discretionary-Security Property**: This property uses an access matrix to allow read and write operations. An example access matrix is shown in the table below and used in conjunction with the first two properties.

<img width="898" height="155" alt="image" src="https://github.com/user-attachments/assets/205a0502-0a42-4802-becb-55e8c0ab4b70" />

The first two properties can be summarized as “write up, read down.” You can share confidential information with people of higher security clearance (write up), and you can receive confidential information from people with lower security clearance (read down).

There are certain limitations to the Bell-LaPadula model. For example, it was not designed to handle file-sharing.

---

### Biba Model

The Biba Model aims to achieve integrity by specifying two main rules:
- **Simple Integrity Property**: This property is referred to as “no read down”; a higher integrity subject should not read from a lower integrity object.
- **Star Integrity Property**: This property is referred to as “no write up”; a lower integrity subject should not write to a higher integrity object.

These two properties can be summarized as “read up, write down.” This rule is in contrast with the Bell-LaPadula Model, and this should not be surprising as one is concerned with confidentiality while the other is with integrity.

Biba Model suffers from various limitations. One example is that it does not handle internal threats (insider threat).

---

### Clark-Wilson Model

The Clark-Wilson Model also aims to achieve integrity by using the following concepts:
- **Constrained Data Item (CDI)**: This refers to the data type whose integrity we want to preserve.
- **Unconstrained Data Item (UDI)**: This refers to all data types beyond CDI, such as user and system input.
- **Transformation Procedures (TPs)**: These procedures are programmed operations, such as read and write, and should maintain the integrity of CDIs.
- **Integrity Verification Procedures (IVPs)**: These procedures check and ensure the validity of CDIs.

We covered only three security models. The reader can explore many additional security models. Examples include:
- Brewer and Nash model
- Goguen-Meseguer model
- Sutherland model
- Graham-Denning model
- Harrison-Ruzzo-Ullman model

---

### Answer the questions below

1. Click on "View Site" and answer the four questions. What is the flag that you obtained at the end?

<img width="922" height="216" alt="image" src="https://github.com/user-attachments/assets/ba5a9400-4809-46d7-90fc-994dceb7538e" />

## Defence-in-Depth

Defence-in-Depth refers to creating a security system of multiple levels; hence it is also called Multi-Level Security.

Consider the following analogy: you have a locked drawer where you keep your important documents and pricey stuff. The drawer is locked; however, do you want this drawer lock to be the only thing standing between a thief and your expensive items? If we think of multi-level security, we would prefer that the drawer be locked, the relevant room be locked, the main door of the apartment be locked, the building gate be locked, and you might even want to throw in a few security cameras along the way. Although these multiple levels of security cannot stop every thief, they would block most of them and slow down the others.


