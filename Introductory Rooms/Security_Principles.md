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

## ISO/IEC 19249

The International Organization for Standardization (ISO) and the International Electrotechnical Commission (IEC) have created the ISO/IEC 19249. In this task, we will brush briefly upon *ISO/IEC 19249:2017 Information technology - Security techniques - Catalogue of architectural and design principles for secure products, systems and applications*. The purpose is to have a better idea of what international organizations would teach regarding security principles.

---

### Architectural Principles:

ISO/IEC 19249 lists five architectural principles:

#### 1. Domain Separation

Domain Separation means putting related things into separate groups (called domains) so they are isolated from each other.
- Each group contains related programs, data, or resources.
- Every group has its own security rules and permissions.
- A group can only access what it is allowed to access.

In an x86 processor:
- Ring 0 → Used by the operating system (kernel). It has the highest privileges and can control everything.
- Ring 3 → Used by normal applications (like Chrome or Word). It has limited privileges and cannot directly access important system resources.

This separation helps keep the system secure. If a normal application is hacked, it cannot easily take full control of the operating system.

#### 2. Layering

Layering means dividing a system into different levels (layers), where each layer has a specific job.
- Every layer performs its own task.
- A layer only communicates with the layer directly above or below it.
- Security rules can be added at each layer.
- If one layer has a problem, the other layers still provide protection.
- Layering relates to Defence in Depth.

**Example 1: OSI Model**

A computer network has 7 layers in the OSI model.
- Each layer has a different responsibility (such as sending data or checking errors).
- Each layer provides services to the layer above it.
- Security can be applied at every layer, making the network safer and easier to test.

**Example 2: Programming**

When a programmer reads or writes a file:
- They use simple functions like `read()` and `write()`.
- The programming language handles the complex, low-level system calls in the background.
- This makes programming easier and more secure.

#### 3. Encapsulation

Encapsulation means hiding the internal details of a system or object and only allowing access through safe and approved methods.
- Users cannot directly change important data.
- They must use specific functions (methods) provided by the system.
- This helps prevent mistakes and keeps the data secure

**Example 1: Clock Object**

Suppose you have a clock object.
- Bad: Letting the user directly change the seconds value (they could set it to 80, which is invalid).
- Good: Providing an `increment()` method that safely increases the time by one second.

This ensures the clock always shows a valid time.

**Example 2: Database**

Instead of letting an application directly access the database:
- The application uses an API (Application Programming Interface).
- The API checks requests and only allows valid operations.
- This protects the database from incorrect or unauthorized changes.

#### 4. Redundancy

Redundancy means having a backup or extra copy of important components so the system keeps working even if one part fails.
- If one part stops working, another backup part takes over.
- This helps keep the system available and protects the data.

**Example 1: Power Supply**

A server has two power supplies.
- If one power supply fails, the other one continues providing power.
- The server keeps running without interruption.

**Example 2: RAID 5**

A RAID 5 system uses three hard drives.
- If one hard drive fails, the data can still be recovered from the other two drives.
- If data on one drive is changed incorrectly, the system can detect it using parity, helping maintain data integrity.

#### 5. Virtualization

With the advent of cloud services, virtualization has become more common and popular. The concept of virtualization is sharing a single set of hardware among multiple operating systems. Virtualization provides sandboxing capabilities that improve security boundaries, secure detonation, and observance of malicious programs.

---

### Design Principles

ISO/IEC 19249 teaches five design principles:

1. **Least Privilege**: You can also phrase it informally as “need-to basis” or “need-to-know basis” as you answer the question, “who can access what?” The principle of least privilege teaches that you should provide the least amount of permissions for someone to carry out their task and nothing more. For example, if a user needs to be able to view a document, you should give them read rights without write rights.
2. **Attack Surface Minimisation**: Every system has vulnerabilities that an attacker might use to compromise a system. Some vulnerabilities are known, while others are yet to be discovered. These vulnerabilities represent risks that we should aim to minimize. For example, in one of the steps to harden a Linux system, we would disable any service we don’t need.
3. **Centralized Parameter Validation**: Many threats are due to the system receiving input, especially from users. Invalid inputs can be used to exploit vulnerabilities in the system, such as denial of service and remote code execution. Therefore, parameter validation is a necessary step to ensure the correct system state. Considering the number of parameters a system handles, the validation of the parameters should be centralized within one library or system.
4. **Centralized General Security Services**: As a security principle, we should aim to centralize all security services. For example, we would create a centralized server for authentication. Of course, you might take proper measures to ensure availability and prevent creating a single point of failure.
5. **Preparing for Error and Exception Handling**: Whenever we build a system, we should take into account that errors and exceptions do and will occur. This principle teaches that the systems should be designed to fail safe; for example, if a firewall crashes, it should block all traffic instead of allowing all traffic. Moreover, we should be careful that error messages don’t leak information that we consider confidential, such as dumping memory content that contains information related to other customers.

---

### Answer the questions below

1. Which principle are you applying when you turn off an insecure server that is not critical to the business?

2

2. Your company hired a new sales representative. Which principle are they applying when they tell you to give them access only to the company products and prices?

1

3. While reading the code of an ATM, you noticed a huge chunk of code to handle unexpected situations such as network disconnection and power failure. Which principle are they applying?

5

## Zero Trust versus Trust but Verify

Trust is a very complex topic; in reality, we cannot function without trust. If we think of trust on a business level, things only become more sophisticated; however, we need some guiding security principles. Two security principles that are of interest to us regarding trust:

**Trust but Verify**: Even if you trust a user or system, always check and verify their actions. This is done using logs and security tools like intrusion detection and prevention systems.

**Zero Trust**: Never trust by default. Every user and device must prove their identity before accessing resources, even if they are inside the organization.

Microsegmentation means dividing a network into very small sections, even down to a single computer (host).
- Each section is protected separately.
- Devices must authenticate and get permission before communicating with another section.
- This is a key part of the Zero Trust security model.

## Threat versus Risk

There are three terms that we need to take note of to avoid any confusion.
- **Vulnerability**: Vulnerable means susceptible to attack or damage. In information security, a vulnerability is a weakness.
- **Threat**: A threat is a potential danger associated with this weakness or vulnerability.
- **Risk**: The risk is concerned with the likelihood of a threat actor exploiting a vulnerability and the consequent impact on the business.

## Conclusion

Finally, the Shared Responsibility Model is worth mentioning, especially with the increased reliance on cloud services. Various aspects are required to ensure proper security. They include hardware, network infrastructure, operating systems, applications, etc. However, customers using cloud services have different access levels depending on the cloud services they use. For example, an Infrastructure as a Service (IaaS) user has complete control (and responsibility) over the operating system.

On the other hand, a Software as a Service (SaaS) user has no direct access to the underlying operating system. Consequently, achieving security in a cloud environment necessitates both the cloud service provider and the user to do their parts. The Shared Responsibility Model is a cloud security framework to ensure that each party is aware of its responsibility.

The Shared Responsibility Model means that both the cloud provider and the customer are responsible for security, but they are responsible for different things.
- Cloud Provider → Protects the cloud infrastructure (hardware, networking, data centers).
- Customer → Protects their own data, accounts, applications, and settings.
