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





