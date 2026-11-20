# Network Security Essentials

Room: [Network Security Essentials](https://tryhackme.com/room/networksecurityessentials)

Prerequisites:
1. [Network Fundamentals](https://tryhackme.com/module/network-fundamentals)
2. [Introduction to SIEM](https://tryhackme.com/room/introtosiem)
3. [Intro to Log Analysis](https://tryhackme.com/room/introtologanalysis)

<img width="948" height="215" alt="image" src="https://github.com/user-attachments/assets/d5393f86-65ef-416d-9ec1-11f98b102c7b" />

## Introduction

The networks are the backbone of every modern organization.  Servers, workstations, applications, and security devices don’t exist in isolation; they are interconnected, forming a single ecosystem. The network perimeter is where this internal ecosystem is segregated from the external Internet, and it is often the first target for attackers.

## A Network - Overview

### Network Components - Building Blocks of a Network

A computer network is not just a random collection of devices; it is an organized structure where network assets connect to enable communication, resource sharing, and connectivity with each other and the world.

---

### Small Enterprise Network

From a security perspective, knowing what these devices do and why they’re important helps quickly identify suspicious activity. Let's take an example of a small enterprise network, and understand its key components, usage, and their importance from a security perspective:

**User Workstations (Endpoints)**

Employees do their daily work at workstations (PCs, laptops). However, they are also the most common entry point for attackers, often via phishing emails or malicious downloads. 

Example: A phishing email drops malware on a finance user’s PC.

Why it matters: Endpoints are often less monitored, but a compromise here can give attackers a foothold to move laterally.

**Importance**: Endpoint logs can reveal malicious processes, but network logs may first show C2 (Command & Control) connections.

**File & Database Servers**

These servers store the business's most important asset, its data. File servers provide centralized access to shared documents, while database servers manage structured data like customer records, HR information, or financial data.

**Importance**: Attackers usually target these servers because compromising them means access to valuable or sensitive data. Ransomware operators, in particular, target file servers to maximize their impact. Data exfiltration campaigns often involve stealthily moving data from these servers out of the network.

Data exfiltration is the deliberate, unauthorized transfer or theft of data from a device, network, or cloud environment to an external or unauthorized location.

**Application Servers (Web, Email, VPN, etc.)**

These servers provide services that employees and customers rely on daily.
- Web Servers: Host company websites and web applications.
- Email Servers: Handle corporate communications.
- VPN Gateways: Allow secure remote access to internal resources.

**Importance**: Because they are externally facing, application servers are high-value targets. Attackers scan them constantly for software vulnerabilities or weak configurations. Exploiting one often provides a foothold into the internal network.

From a security perspective, we need to monitor application logs, firewall alerts, and IDS signatures to identify:
- Exploit attempts (e.g., SQL injection on a web app).
- Brute-force login attempts on email or VPN services.
- Suspicious external IPs interacting with sensitive applications.

**Active Directory (AD) / Authentication Servers**

Active Directory is the identity backbone of most enterprise networks. It manages users, groups, computers, and their access rights. Employees use their AD credentials to log into their computers, access email, file servers, and internal applications.

**Importance**
- AD is the main component that controls all user accounts and systems within the network.
- Attackers commonly target AD for privilege escalation, persistence, and lateral movement.
- A single compromised domain admin account can bring down the entire enterprise.

From a security perspective, we need to monitor authentication logs for suspicious behavior such as:
- Multiple failed login attempts (password spraying).
- Unusual logins from external IPs or at odd hours.
- Accounts accessing systems they normally shouldn’t.

**Routers & Switches (Network Infrastructure)**

Routers connect different networks, most importantly linking the enterprise LAN to the Internet. Switches connect devices within the same network, ensuring employees’ PCs, printers, and servers communicate seamlessly. These devices are the circulatory system of the enterprise.

**Importance**: While routers and switches are not directly exposed in most enterprise setups, if compromised, they provide attackers with the ability to:
- Intercept and manipulate traffic (Man-in-the-Middle attacks).
- Create backdoors by rerouting traffic.
- Open hidden channels to the Internet.

**Firewalls / Perimeter Devices**

A firewall is the primary security gateway that controls traffic between the trusted internal network and the untrusted Internet. It inspects incoming and outgoing packets and decides whether to allow or block them based on defined security rules. Modern firewalls also perform deep inspection of applications, intrusion prevention, and even malware detection.

**Importance**:
- Protects the enterprise from direct exposure to the Internet.
- Prevents unauthorized access to internal services (e.g., database or RDP).
- Logs every connection attempt, successful or blocked. These logs are often the earliest indicators of attacks such as port scans, brute-force attempts, or exploitation attempts.


