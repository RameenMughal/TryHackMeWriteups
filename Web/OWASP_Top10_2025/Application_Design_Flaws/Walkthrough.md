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

Looking at the code of `app.py` given to us, one thing immediately stands out:

```
if data == 'debug':
    return jsonify(debug_info())
```

If you send "debug" as the input, the application calls `debug_info()` from the vulnerable library.

A debug function is meant for developers, not for users. It often reveals sensitive information that attackers can use. So it is accessible to everyone which is a bad thing

Using curl command: 

```
curl -X POST http://MACHINE_IP:5003/api/process \
-H "Content-Type: application/json" \
-d '{"data":"debug"}'
```

<img width="571" height="193" alt="image" src="https://github.com/user-attachments/assets/a81a5eb5-656e-43c8-a79b-b0ca9324c675" />

## AS04: Cryptographic Failures

### Cryptographic Failures

**What It Is**

Cryptographic failures happen when encryption is used incorrectly or not at all. This includes weak algorithms, hard-coded keys, poor key handling, or unencrypted sensitive data. These flaws let attackers access information that should be private.

**Why It Matters**

Web applications rely on cryptography everywhere: protecting network traffic, securing stored data, verifying identities, and safeguarding secrets. When these controls fail, sensitive data such as passwords, tokens, or personal information can be exposed, leading to account takeovers or full-scale breaches.

Attackers can exploit these flaws through man-in-the-middle attacks, brute-force attacks on weak keys, or by simply discovering secrets that were never properly protected.

**Common Patterns**
- Using deprecated or weak algorithms like MD5, SHA-1, or ECB mode
- Hard-coded secrets in code or configuration
- Poor key rotation or management practices
- Lack of encryption for sensitive data at rest or in transit
- Self-signed or invalid TLS certificates
- Using AI/ML systems without proper secret handling for model parameters or sensitive inputs

**How To Prevent It**
- Use strong, modern algorithms such as AES-GCM, ChaCha20-Poly1305, or enforce TLS 1.3 with valid certificates
- Use secure key management services like Azure Key Vault, AWS KMS, or HashiCorp Vault
- Rotate secrets and keys regularly, following defined crypto periods
- Document and enforce policies and standard operating procedures for key lifecycle management
- Maintain a complete inventory of certificates, keys, and their owners
- Ensure AI models and automation agents never expose unencrypted secrets or sensitive data

---

### Challenge

Navigate to `MACHINE_IP:5004`. Can you find the key to decrypt the file?

---

### Answer the questions below

What's the flag?

Navigating to the page gives us Encrypted document where only administrator can access.

<img width="837" height="215" alt="image" src="https://github.com/user-attachments/assets/dddd99a6-a730-416f-9c88-ae9ee0752eb8" />

Checking the source page of this web page gives us `decrypt.js` which contains hardcoded secret key `my-secret-key-16` and algorithm ECB.

The developer has hardcoded the encryption key in client-side JavaScript.

Anyone can open `/static/js/decrypt.js` and see the key.

As we know the secret key and algorithm, we can create a `decrypt.py` which decrypts the encrypted document:

<img width="895" height="82" alt="image" src="https://github.com/user-attachments/assets/b1acaeb0-9257-4040-bba1-0a3cec162684" />

## AS06: Insecure Design

### Insecure Design 

**What It Is**

Insecure design happens when flawed logic or architecture is built into a system from the start. These flaws stem from skipped threat modelling, no design requirements or reviews, or accidental errors.

Moreover, with the introduction of AI assistants, AI systems exacerbate insecure design. Developers often assume that models are safe, correct, or predictable, or that the code they produce is flaw-free. When an AI system can generate queries, write code, or classify users without limits, the risk is built into the design, leading to poor architectural patterns.

**Why It Matters**

You can't patch an insecure design. It's built into the workflow, logic, and trust boundaries. Fixing it means rethinking how systems, and now AI, make decisions.

**Common Insecure Designs In 2025**
- Weak business logic controls, like recovery or approval flows
- Flawed assumptions about user or model behaviour
- AI components with unchecked authority or access
- Missing guardrails for LLMs and automation agents
- Test or debug bypasses left in production
- No consistent abuse-case review or AI threat modelling

Guardrails are rules, controls, or security measures that prevent a system from doing something unsafe or unauthorized.

**Insecure Design In The AI Era**

AI introduces new kinds of design failures. For example, prompt injection occurs when user input is blended with system prompts, allowing attackers to hijack the context or extract hidden data. Blind trust in model output creates fragile systems that act on AI decisions without validation or oversight, which is why human review remains necessary. When it comes to poisoned models, pulled from unverified sources or fine-tuned on unsafe data, they can embed hidden behaviours or backdoors that compromise the system from within.

**How To Design Securely**

- Treat every model as untrusted until proven otherwise.
- Validate and filter all model inputs and outputs to ensure accuracy and integrity.
- Separate system prompts from user content.
- Keep sensitive data out of prompts unless absolutely needed and protect it with strict controls.
- Require human review for high-risk AI actions.
- Log model provenance, monitor behaviour, and apply differential privacy for sensitive data.
- Include AI-specific threat modelling for prompt attacks, inference risks, agent misuse, and supply chain compromise throughout the design process.
- Build threat modelling into every stage of development, not just at the start.
- Define clear security requirements for each feature before implementation.
- Apply the principle of least privilege across users, APIs, and services.
- Ensure proper authentication, authorisation, and session management across the system.
- Keep dependencies, third-party components, and supply chain sources verified and up to date.
- Continuously monitor and test the system for logic flaws, abuse paths, and emergent risks as new features or AI components are added.

--

### Challenge

Navigate to `MACHINE_IP:5005`. Have they assumed that only mobile devices can access it?

---

### Answer the questions below

What's the flag?

Navigating to the web page, we get SecureChat which has mobile app:

<img width="832" height="331" alt="image" src="https://github.com/user-attachments/assets/44e74e47-ad38-42c1-8237-c008616014de" />

Checking the source page, there is nothing new there and the download button is also just dead CSS.

I also tried to curl acting to request data from Android but got the same web page:

`curl -H "User-Agent: Android" http://MACHINE_IP:5005/` and `curl -A "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)" http://MACHINE_IP:5005/`

So we can think as it assumes that users will only access it from mobile, there will be some pages pubicly available that we can see from our browser

Trying `gobsuter` to find hidden directories or pages: 

`gobuster dir -u http://10.49.155.85:5005 -w /usr/share/wordlists/dirb/common.txt`

I only get `/console` but got Bad Request after accessing it.

We can think again that there will be an `api` directory that manages users and their messages as the app is about messages.

Trying another `gobuster` scan with api, so we get `users` directory: 

`gobuster dir -u http://MACHINE_IP:5005/api -w /usr/share/wordlists/dirb/common.txt`

<img width="452" height="206" alt="image" src="https://github.com/user-attachments/assets/0a7dc8d3-253d-40eb-8eba-6194ed1b5b8e" />

Accessing the `/users` we get user's information in which `admin` is important:

<img width="350" height="161" alt="image" src="https://github.com/user-attachments/assets/628ba683-cfe3-4483-9b2d-643182dbea18" />

But still there is no flag, so as this is about messages so there will be an api named as `messages` so accessing the admin messages would be helpful.

Tried accessing multiple like `/api/users/admin/messages`, `/api/users/messages` and `/api/messages`

Then finally at `/api/messages/admin` we get the flag:

<img width="664" height="267" alt="image" src="https://github.com/user-attachments/assets/272bbcd6-7759-44a4-9fdb-b82f718b2afa" />






