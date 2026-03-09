# Introduction to SIEM

Room: [Introduction to SIEM](https://tryhackme.com/room/introtosiem)

<img width="1879" height="386" alt="image" src="https://github.com/user-attachments/assets/b5fcdeae-a854-4cce-b909-39e73deb4ca7" />

## Introduction

Security Information and Event Management system (SIEM) is the core security solution that a SOC analyst uses in the security operations center.

### Answer the questions below

What does SIEM stand for?

Security Information and Event Management System

## Logs Everywhere, Answers Nowhere

Multiple devices in a network communicate with each other and, most of the time, with the Internet through a router. 

The image below shows an example of a simple network that comprises multiple Linux/Windows-based Endpoints, one data server, and one website.

<img width="921" height="801" alt="image" src="https://github.com/user-attachments/assets/9b53ae77-54f6-4919-ab3a-9bcd1fd3dece" />

These devices continuously generate logs of the activities that occur within them. We can also call these devices **log sources**. The logs they generate serve as a trail of all the activities and are extremely helpful for identifying malicious activities or general troubleshooting. 

These log sources are mainly divided into two categories:

### 1. Host-Centric Log Sources

These log sources capture events that occurred within or related to the host. Devices that generate host-centric logs include Windows, Linux, servers, etc. Some examples of host-centric logs are:
- A user accessing a file
- A user attempting to authenticate.
- A process execution activity
- A process adding/editing/deleting a registry key or value.
- PowerShell execution

### 2. Network-Centric Log Sources

Network-related logs are generated when the hosts communicate with each other or access the internet to visit a website. Devices that generate network-centric logs are firewalls, IDS/IPS, routers, etc. Some examples of network-centric logs are:
- SSH connection
- A file being accessed via FTP
- Web traffic
- A user accessing the company's resources through VPN.
- Network file sharing Activity

Together, these host-centric and network-centric log sources constantly create numerous logs in a network. 

### Answers Nowhere

Until now, it seems pretty straightforward that these log sources generate logs, we analyze them, and identify malicious activities. However, it's not that simple. It has some challenges. Some of them are discussed below:
- Numerous Log Sources
- No Centralization
- Limited Context 
- Limited Analysis 
- Format Issues

### Answer the questions below

1. Is Registry-related activity host-centric or network-centric?

Host-centric

2. Is VPN-related activity host-centric or network-centric?

Network-centric

## Why SIEM ?

Security Information and Event Management (SIEM) is a security solution that collects logs from various types of log sources, standardizes their format into a consistent one, correlates them, and detects malicious activities using detection rules.

<img width="733" height="729" alt="image" src="https://github.com/user-attachments/assets/d9dd4fa2-0915-4d87-8204-5c5e10d784f0" />

### Features of SIEM

Let's discuss some of the core features that a SIEM provides.

1. **Centralized Log Collection**: SIEM collects logs from all sources (endpoints, servers, firewalls, etc.) and centralizes them in one place. These logs are pulled through lightweight agents or APIs and populated into the SIEM solution. This solves the problem of jumping on every machine individually to analyze its logs. 
2. **Normalization of Logs**: Raw logs are of different formats and sizes. It also ensures that all the logs are broken down into different fields and presented in one consistent format. Breaking down a log into several fields for ease of understanding is known as **Parsing**, and converting all the logs of various log sources into one consistent format is known as **Normalization**. 
3. **Correlation of Logs**: Individual logs are not very useful. SIEM correlates the logs of different sources and finds any relationship between them. This helps to identify malicious activity by analyzing its pattern.
4. **Real-time Alerting**: SIEM detects malicious activities based on the rules it contains. Many rules come with a SIEM by default. However, analysts make new detection rules based on their requirements to mature future detections. When the conditions for these detection rules are satisfied, alerts are triggered, and the analysts are notified. Analysts can then investigate these alerts within the SIEM platform.  
5. **Dashboards and Reporting**: Dashboards are the most important components of any SIEM. SIEM presents the data for analysis after being normalized and ingested. The summary of this analysis is presented in the form of actionable insights with the help of multiple dashboards.

An example of a dashboard made in Splunk SIEM is shown below:

<img width="2542" height="1400" alt="image" src="https://github.com/user-attachments/assets/91c595be-bc0b-44d9-85b6-43eaf64bdfd8" />

There are several other features of a SIEM that we will not cover in detail in this room. These features include integration with threat intelligence feeds, extensive data retention, powerful searching capabilities, and many others. 

## Log Sources and Ingestion

### Log Sources

Every device in the network generates some kind of log whenever an activity is performed on it, such as a user visiting a website, connecting to SSH, logging into their workstation, etc. Let's see what the logs of some common devices that are found in a network environment look like.

### Windows Machine

Windows records every event that can be viewed through the Event Viewer. It assigns a unique ID to each type of log activity, making it easy for the analyst to examine and keep track of. To view events in a Windows environment, type Event Viewer in the search bar. This takes you to the tool where different logs are stored and can be viewed, as shown below. These logs from all Windows endpoints are forwarded to the SIEM solution for monitoring and better visibility.






