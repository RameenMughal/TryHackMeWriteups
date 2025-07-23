# Search Skills

## Evaluationof Search Results

**DevSecOps**: Fosters the same culture and principles as Devops with the addition of security into the development process, ensuring security is integrated from an early stage.

### Answer the questions below

1. What do you call a cryptographic method or product considered bogus or fraudulent?

Snake Oil

2. What is the name of the command replacing netstat in Linux systems?

`ss`

## Search Engines

Let’s consider the search operators supported by Google.

- `"exact phrase"`: Double quotes indicate that you are looking for pages with the exact word or phrase. For example, one might search for `"passive reconnaissance"` to get pages with this exact phrase.
- `site:`: This operator lets you specify the domain name to which you want to limit your search. For example, we can search for success stories on TryHackMe using `site:tryhackme.com success stories`.
- `-`: The minus sign allows you to omit search results that contain a particular word or phrase. For example, you might be interested in learning about the pyramids, but you don’t want to view tourism websites; one approach is to search for `pyramids -tourism` or `-tourism pyramids`.
- `filetype:`: This search operator is indispensable for finding files instead of web pages. Some of the file types you can search for using Google are Portable Document Format (PDF), Microsoft Word Document (DOC), Microsoft Excel Spreadsheet (XLS), and Microsoft PowerPoint Presentation (PPT). For example, to find cyber security presentations, try searching for `filetype:ppt cyber security`.

### Answer the questions below

1. How would you limit your Google search to PDF files containing the terms cyber warfare report?

`filetype:PDF Cyber Warfare Report`

2. What phrase does the Linux command `ss` stand for?

Socket Statistics

## Specialized Search Engines

### Shodan

A search engine for devices connected to the Internet. It allows you to search for specific types and versions of servers, networking equipment, industrial control systems, and IoT devices. 

You may want to see how many servers are still running `Apache 2.4.1` and the distribution across countries. To find the answer, we can search for apache 2.4.1, which will return the list of servers with the string “apache 2.4.1” in their headers.

### Censys

At first glance, Censys appears similar to Shodan. However, Shodan focuses on Internet-connected devices and systems, such as servers, routers, webcams, and IoT devices. 

Censys, on the other hand, focuses on Internet-connected hosts, websites, certificates, and other Internet assets. Some of its use cases include enumerating domains in use, auditing open ports and services, and discovering rogue assets within a network.

### VirusTotal

VirusTotal is an online website that provides a virus-scanning service for files using multiple antivirus engines. It allows users to upload files or provide URLs to scan them against numerous antivirus engines and website scanners in a single operation. They can even input file hashes to check the results of previously uploaded files

### Have I Been Pwned

Have I Been Pwned (HIBP) does one thing; it tells you if an email address has appeared in a leaked data breach. Finding one’s email within leaked data indicates leaked private information and, more importantly, passwords. 

Many users use the same password across multiple platforms, if one platform is breached, their password on other platforms is also exposed. Indeed, passwords are usually stored in encrypted format; however, many passwords are not that complex and can be recovered using a variety of attacks

### Answer the questions below

1. What is the top country with lighttpd servers?

Search lighttpd in Shodan 

**Answer**: United States

2. What does BitDefenderFalx detect the file with the hash `2de70ca737c1f4602517c555ddd54165432cf231ffc0e21fb2e23b9dd14e7fb4` as?

Search the file hash in VirusTotal, you see BitDefenderFalx in Security Vendors' Analysis

**Answer**: Android.Riskware.Agent.LHH

## Vulnerabilities and Exploits

### CVE

We can think of the Common Vulnerabilities and Exposures (CVE) program as a dictionary of vulnerabilities. It provides a standardized identifier for vulnerabilities and security issues in software and hardware products. 

Each vulnerability is assigned a CVE ID with a standardized format like CVE-2024-29988. This unique identifier (CVE ID) ensures that everyone from security researchers to vendors and IT professionals is referring to the same vulnerability, CVE-2024-29988 in this case.
