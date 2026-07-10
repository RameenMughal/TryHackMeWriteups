# OWASP Top 10 2025: Application Design Flaws

Room: [OWASP Top 10 2025: Application Design Flaws](https://tryhackme.com/room/owasptopten2025two)

<img width="935" height="199" alt="image" src="https://github.com/user-attachments/assets/264e6a89-6868-4325-a5b4-c834771a6c57" />

## Introduction

This room breaks each 4 of the OWASP Top 10 2025 categories. In this room, you will learn about the categories that are related to failures in architecture and system design. The following categories are covered in this room:
- AS02: Security Misconfigurations
- AS03: Software Supply Chain Failures
- AS04: Cryptographic Failures
- AS06: Insecure Design

---

### Deploy Practical

Start the Lab Machine and I am using my Kali Linux Machine as an Attack Box, so I will connect my machine to the TryHackMe Server by OpenVPN.

You can check how to connect your machine by OpenVPN through this room: [OpenVPN](https://tryhackme.com/room/openvpn)

Connecting by command: `sudo openvpn <filename>`

## AS02: Security Misconfigurations

### Security Misconfigurations

**What it is**

Security misconfigurations happen when systems, servers, or applications are deployed with unsafe defaults, incomplete settings, or exposed services. These are not code bugs but mistakes in how the environment, software, or network is set up. They create easy entry points for attackers.

**Why It Matters**

Even small misconfigurations can expose sensitive data, enable privilege escalation, or give attackers a foothold into the system. Modern applications rely on complex stacks, cloud services, and third-party APIs. A single exposed admin panel, an open storage bucket, or misconfigured permissions can compromise the entire system.

**Common Patterns**
- Default credentials or weak passwords left unchanged
- Unnecessary services or endpoints exposed to the internet
- Misconfigured cloud storage or permissions (S3, Azure Blob, GCP buckets)
- Unrestricted API access or missing authentication/authorisation
- Verbose error messages exposing stack traces or system details
- Outdated software, frameworks, or containers with known vulnerabilities
- Exposed AI/ML endpoints without proper access controls

**How To Prevent It**
- Harden default configurations and remove unused features or services
- Enforce strong authentication and least privilege across all systems
- Reduce how much of your network is exposed to others and separate important systems from the rest of the network.
- Keep software, frameworks, and containers up to date with patches
- Hide stack traces and system information from error messages
- Audit cloud configurations and permissions regularly
- Secure AI endpoints and automation services with proper access controls and monitoring
- Regularly check your system settings and use automated tools to find security problems before releasing your application.

---

### Challenge 

Navigate to `MACHINE_IP:5002`. It appears that the developers left too many traces in their User Management APIs.

---

### Answer the questions below

What's the flag?

Navigating to the page it gives us hint about using only numeric `user_id` to get the information by `GET`

So I created a python script `endpoints.py` which checks `user_id` from 1 to 200 but got no flag.

Then we can think that it says that you must use only numeric `user_id` so lets check how it handles errors if we don't put numeric `user_id`

Using curl command: `curl "http://MACHINE_IP:5002/api/user/<user_id>"` by writing `user_id` as text:

<img width="1708" height="195" alt="image" src="https://github.com/user-attachments/assets/9ff7be9b-7295-4396-a9bf-d11e96d8d158" />

## AS03: Software Supply Chain Failures

### Software Supply Chain Failures

**What It Is**

Software supply chain failures happen when applications rely on components, libraries, services, or models that are compromised, outdated, or improperly verified. These weaknesses are not inherent in your code, but rather in the software and tools you depend on. Attackers exploit these weak links to inject malicious code, bypass security, or steal sensitive data.

**Why It Matters**

Modern applications are built from many third-party packages, APIs, and AI models. One compromised dependency can compromise your entire system, allowing attackers to gain access without ever touching your own code. Supply chain attacks can be automated and distributed, making them hard to detect and very damaging.

With AI, we can observe this when using unverified third-party models or fine-tuned datasets that can embed hidden behaviours, backdoors, or biased outputs, compromising systems or leaking data.

**Common Patterns**
- Using unverified or unmaintained libraries and dependencies
- Automatically installing updates without verification
- Over-reliance on third-party AI models without monitoring or auditing
- Insecure build pipelines or CI/CD processes that allow tampering
- Poor license or provenance tracking for components
- Lack of monitoring for vulnerabilities in dependencies after deployment

**How To Protect The Supply Chain**
- Verify all third-party components, libraries, and AI models before use
- Monitor and patch dependencies regularly
- Sign, verify, and audit software updates and packages
- Lock down CI/CD pipelines and build processes to prevent tampering
- Track provenance and licensing for all dependencies
- Implement runtime monitoring for unusual behaviour from dependencies or AI components
- Integrate supply chain threat modelling into the SDLC, including testing, deployment, and update workflows

A CI/CD pipeline is an automated process that builds, tests, and deploys software whenever developers make changes to the code.
- CI = Continuous Integration
- CD = Continuous Delivery or Continuous Deployment

---

### Challenge

Navigate to `MACHINE_IP:5003`. The code is outdated and imports an old `lib/vulnerable_utils.py` component. Can you debug it?

---

### Answer the questions below

What's the flag?

