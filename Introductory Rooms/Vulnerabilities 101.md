# Vulnerabilities 101

<img width="902" height="174" alt="image" src="https://github.com/user-attachments/assets/65bec57b-d8a9-4b06-9180-b2a078134451" />

## Introduction to Vulnerabilities

A vulnerability in cybersecurity is defined as a weakness or flaw in the design, implementation or behaviours of a system or application. 

An attacker can exploit these weaknesses to gain access to unauthorised information or perform unauthorised actions.

NIST defines a vulnerability as “weakness in an information system, system security procedures, internal controls, or implementation that could be exploited or triggered by a threat source”.

National Institute of Standards and Technology (NIST). This organisation develops frameworks and policies for information security that is used all throughout the industry.

There are arguably five main categories of vulnerabilities:

| Vulnerability             | Description                                                                                      |
|----------------------------|--------------------------------------------------------------------------------------------------|
| Operating System           | Found within OSs and often result in privilege escalation.                                       |
| (Mis)Configuration-based   | Stem from incorrectly configured applications or services, e.g., a website exposing data.        |
| Weak or Default Credentials| Services with default login details (e.g., admin/admin) that attackers can easily guess.         |
| Application Logic          | Result of poorly designed apps, e.g., weak authentication allowing impersonation.               |
| Human-Factor               | Exploit human behavior, e.g., phishing emails tricking users into believing they are legitimate. |

As a cybersecurity researcher, you will be assessing applications and systems - using vulnerabilities against these targets in day-to-day life, so it is crucial to become familiar with this discovery and exploitation process.

### Answer the questions below

1. An attacker has been able to upgrade the permissions of their system account from "user" to "administrator". What type of vulnerability is this?

Operating System

2. You manage to bypass a login panel using cookies to authenticate. What type of vulnerability is this?

Application Logic

## Scoring Vulnerabilities (CVSS & VPR)

Vulnerability management is the process of evaluating, categorising and ultimately remediating threats (vulnerabilities) faced by an organisation.

It is arguably impossible to patch and remedy every single vulnerability in a network or computer system and sometimes a waste of resources.

thousands of vulnerabilities are discovered every year, only a very small percentage—around 2%—are ever actively exploited by attackers. In practice, this shows that not every vulnerability poses an immediate threat. Instead of trying to fix every single issue, security teams focus on identifying and addressing the most dangerous vulnerabilities, particularly those that are easier to exploit or more likely to be targeted. 

By prioritizing high-risk weaknesses, organizations can significantly reduce the chances of attackers finding and using an exploit path, making their systems much harder to compromise.

This is where vulnerability scoring comes into play. Vulnerability scoring serves a vital role in vulnerability management and is used to determine the potential risk and impact a vulnerability may have on a network or computer system. 

For example, the popular Common Vulnerability Scoring System (CVSS) awards points to a vulnerability based upon its features, availability, and reproducibility.

Let’s explore two of the more common frameworks and analyse how they differ.

### Common Vulnerability Scoring System

First introduced in 2005, the Common Vulnerability Scoring System (or CVSS) is a very popular framework for vulnerability scoring and has three major iterations. As it stands, the current version is CVSSv3.1 (with version 4.0 currently in draft) a score is essentially determined by some of the following factors (but many more):

1. How easy is it to exploit the vulnerability?

2. Do exploits exist for this?

3. How does this vulnerability interfere with the CIA triad?

In fact, there are so many variables that you have to use a calculator to figure out the score using this framework. A vulnerability is given a classification (out of five) depending on the score that is has been assigned. 

| Rating   | Score       |
|----------|-------------|
| None     | 0           |
| Low      | 0.1 - 3.9   |
| Medium   | 4.0 - 6.9   |
| High     | 7.0 - 8.9   |
| Critical | 9.0 - 10.0  |

### Vulnerability Priority Rating (VPR)

The VPR framework is a much more modern framework in vulnerability management - developed by Tenable, an industry solutions provider for vulnerability management. This framework is considered to be risk-driven; meaning that vulnerabilities are given a score with a heavy focus on the risk a vulnerability poses to the organisation itself, rather than factors such as impact (like with CVSS).

Unlike CVSS, VPR scoring takes into account the relevancy of a vulnerability. For example, no risk is considered regarding a vulnerability if that vulnerability does not apply to the organisation (i.e. they do not use the software that is vulnerable). VPR is also considerably dynamic in its scoring, where the risk that a vulnerability may pose can change almost daily as it ages.

VPR uses a similar scoring range as CVSS. However, two notable differences are that VPR does not have a "None/Informational" category, and because VPR uses a different scoring method, the same vulnerability will have a different score using VPR than when using CVSS.

| Rating   | Score     |
|----------|-----------|
| Low      | 0.0 - 3.9 |
| Medium   | 4.0 - 6.9 |
| High     | 7.0 - 8.9 |
| Critical | 9.0 - 10.0|

### Answer the questions below

1. What year was the first iteration of CVSS published?

2005

2. If you wanted to assess vulnerability based on the risk it poses to an organisation, what framework would you use? Note: We are looking for the acronym here.

VPR

3. If you wanted to use a framework that was free and open-source, what framework would that be? Note: We are looking for the acronym here.

CVSS

## Vulnerability Databases

This room will showcase two databases that we can use to look up existing vulnerabilities for applications discovered in our infosec journey, specifically the following websites:
- [NVD National Vulnerability Database](https://nvd.nist.gov/vuln)
- [Exploit-DB](https://www.exploit-db.com/)

Let's ensure that our understanding of some fundamental key terms is on the same page:

| Term                  | Definition                                                                 |
|------------------------|----------------------------------------------------------------------------|
| Vulnerability          | A weakness or flaw in the design, implementation, or behavior of a system or application. |
| Exploit                | An action or behavior that takes advantage of a vulnerability in a system or application. |
| Proof of Concept (PoC) | A technique or tool that demonstrates the exploitation of a vulnerability. |

### NVD – National Vulnerability Database

The National Vulnerability Database is a website that lists all publically categorised vulnerabilities. In cybersecurity, vulnerabilities are classified under “Common Vulnerabilities and Exposures” (Or CVE for short).

These CVEs have the formatting of `CVE-YEAR-IDNUMBER`. For example, the vulnerability that the famous malware WannaCry used was `CVE-2017-0144`.

NVD allows you to see all the CVEs that have been confirmed, using filters by category and month of submission. 

While this website helps keep track of new vulnerabilities, it is not great when searching for vulnerabilities for a specific application or scenario.

### Exploit-DB

Exploit-DB is a resource that we, as hackers, will find much more helpful during an assessment. Exploit-DB retains exploits for software and applications stored under the name, author and version of the software or application.

We can use Exploit-DB to look for snippets of code (known as Proof of Concepts) that are used to exploit a specific vulnerability.

### Answer the questions below

1. Using NVD, how many CVEs were published in July 2021?

1554

2. Who is the author of Exploit-DB?

Offsec

## An Example of Finding a Vulnerability

### Answer the questions below

What type of vulnerability did we use to find the name and version of the application in this example?

Version Disclosure

## Showcase: Exploiting Ackme's Application

### Answer the questions below

Follow along with the showcase of exploiting ACKme's application to the end to retrieve a flag. What is this flag?

Understand each step and then you get the Flag!
