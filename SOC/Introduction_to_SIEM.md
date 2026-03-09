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

Windows records every event that can be viewed through the Event Viewer. It assigns a unique ID to each type of log activity, making it easy for the analyst to examine and keep track of. 

To view events in a Windows environment, type `Event Viewer` in the search bar. This takes you to the tool where different logs are stored and can be viewed, as shown below. These logs from all Windows endpoints are forwarded to the SIEM solution for monitoring and better visibility.

<img width="1475" height="807" alt="image" src="https://github.com/user-attachments/assets/fd198a80-a386-4087-a519-0abcff5ed7ff" />

### Linux Machine

Linux OS stores all the related logs, such as events, errors, warnings, etc. These are then ingested into SIEM for continuous monitoring. Some of the common locations where Linux stores logs are:
- `/var/log/httpd`: Contains HTTP Request  / Response and error logs.
- `/var/log/cron`: Events related to cron jobs are stored in this location.
- `/var/log/auth.log` and `/var/log/secure`: Stores authentication-related logs.
- `/var/log/kern`: This file stores kernel-related events.

Here is a sample of a cron log:

```
May 28 13:04:20 ebr crond[2843]: /usr/sbin/crond 4.4 dillon's cron daemon, started with loglevel notice
May 28 13:04:20 ebr crond[2843]: no timestamp found (user root job sys-hourly)
May 28 13:04:20 ebr crond[2843]: no timestamp found (user root job sys-daily) 
May 28 13:04:20 ebr crond[2843]: no timestamp found (user root job sys-weekly) 
May 28 13:04:20 ebr crond[2843]: no timestamp found (user root job sys-monthly
Jun 13 07:46:22 ebr crond[3592]: unable to exec /usr/sbin/sendmail: cron output for user root job sys-daily to /dev/null
```

Cron is a scheduler that automatically runs tasks at specific times (hourly, daily, weekly, monthly).

On May 28, the cron daemon (`crond`) started and noticed that some scheduled root jobs (`sys-hourly`, `sys-daily`, `sys-weekly`, `sys-monthly`) had no previous timestamp, meaning they likely hadn’t run before or the record file was missing. Later, on June 13, cron tried to run the daily job, but it couldn’t execute `/usr/sbin/sendmail`, which is normally used to send the job’s output via email to the root user. Since it failed, the output was redirected to `/dev/null`, meaning it was discarded.

### Web Server

It is important to monitor all requests/responses coming in and out of the web server for any potential web attack attempt. In Linux, common locations to write all apache-related logs are `/var/log/apache` or `/var/log/httpd`.

Here is an example of Apache Logs:

```
192.168.21.200 - - [21/March/2022:10:17:10 -0300] "GET /cgi-bin/try/ HTTP/1.0" 200 3395 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
127.0.0.1 - - [21/March/2022:10:22:04 -0300] "GET / HTTP/1.0" 200 2216 "-" "curl/7.68.0"
```

In the first log, the IP `192.168.21.200` (a device on the internal network) sent a `GET` request to access `/cgi-bin/try/` on March 21, 2022 at 10:17:10. The server responded with status code 200, which means the request was successful, and returned 3395 bytes of data. The request was made using the Chrome browser on Windows 10.

In the second log, the IP `127.0.0.1` (the local machine itself) accessed the homepage `/` at 10:22:04. The request was made using `curl`, a command-line tool for making HTTP requests, and the server again returned status 200, meaning the request was successful.

### Log Ingestion

All these logs provide a wealth of information and can help identify security issues. Each SIEM solution has its own way of ingesting the logs. Some common methods used by these SIEM solutions are explained below:

1. **Agent / Forwarder**: These SIEM solutions provide a lightweight tool called an agent (forwarder by Splunk) that gets installed on the Endpoint. It is configured to capture and send all the important logs to the SIEM server.
2. **Syslog**: Syslog is a widely used protocol to collect data from various systems like web servers, databases, etc., and send real-time data to the centralized destination.
3. **Manual Upload**: Some SIEM solutions, like Splunk, ELK, etc., allow users to ingest offline data for quick analysis. Once the data is ingested, it is normalized and made available for analysis.
4. **Port-Forwarding**: SIEM solutions can also be configured to listen on a certain port, and then the endpoints forward the data to the SIEM instance on the listening port.

An example of how Splunk provides various methods for log Ingestion is shown below:

<img width="1397" height="436" alt="image" src="https://github.com/user-attachments/assets/3f3f956a-57fc-4534-a5ab-b8d265edc565" />

### Answer the questions below

In which location within a Linux environment are HTTP logs stored?

`/var/log/httpd`

## Alerting Process and Analysis

### Behind the Triggered Alerts

SIEM solution has detection rules that catch threats. These rules play an important role in the timely detection of threats, allowing analysts to take action on time. Detection rules are pretty much logical expressions set to be triggered. A few examples of detection rules are:
1. If a user gets five failed Login Attempts in 10 seconds, raise an alert for `Multiple Failed Login Attempts`
2. If login is successful after multiple failed login attempts, raise an alert for `Successful Login After multiple Login Attempts`
3. A rule is set to alert every time a user plugs in a USB (Useful if USB is restricted as per the company policy)
4. If outbound traffic is > 25 MB, raise an alert to potential data exfiltration Attempt (Usually, it depends on the company policy)

### How is a detection rule created?

To explain how the rule works, consider the following Eventlog use cases:

#### Use-Case 1:
Adversaries tend to remove the logs during the post-exploitation phase to remove their tracks. A unique Event ID 104 is logged every time a user tries to remove or clear event logs. To create a rule based on this activity, we can set the condition as follows:

Rule: If the Log source is WinEventLog AND EventID is 104 - Trigger an alert `Event Log Cleared`

#### Use-Case 2:

Adversaries use commands like `whoami` after the exploitation/privilege escalation phase. The following Fields will be helpful to include in the rule.
1. Log source: Identify the log source capturing the event logs
2. Event ID: Which Event ID is associated with Process Execution activity? In this case, Event ID 4688 will be helpful.
3. NewProcessName: Which process name will be helpful to include in the rule?

Rule: If Log Source is WinEventLog AND EventCode is 4688, and NewProcessName contains `whoami`, then Trigger an ALERT `WHOAMI command Execution DETECTED`

### Alert Investigation

Once an alert is triggered, the events/flows associated with the alert are examined, and the rule is checked to see which conditions are met. Based on the investigation, the analyst determines if it's a True or False positive. Some of the actions that are performed after the analysis are:
- Alert is a False Positive. It may require tuning the rule to avoid similar False positives from occurring again.
- Alert is a True Positive. Perform further investigation.
- Contact the asset owner to inquire about the activity.
- Suspicious activity is confirmed. Isolate the infected host.
- Block the suspicious IP.

### Answer the questions below

1. Which Event ID is generated when event logs are removed?

104

2. What type of alert may require tuning?

False Positive

## Lab Work

<img width="911" height="789" alt="image" src="https://github.com/user-attachments/assets/71b916ef-af56-4629-8a11-ce004024c6d2" />

### Answer the questions below

1. After clicking on the Start Suspicious Activity button, which process caused the alert?

`cudominer.exe`

<img width="925" height="295" alt="image" src="https://github.com/user-attachments/assets/7c7c505c-f7cc-493a-92f5-658e26ed1bf4" />

2. Find the event that caused the alert and identify the user responsible for the process execution.

Chris

<img width="857" height="96" alt="image" src="https://github.com/user-attachments/assets/2297737a-dade-4bc0-bfd9-de4ba5801775" />

3. What is the hostname of the suspect user?

`HR_02`

4. Examine the rule and the suspicious process; which term matched the rule that caused the alert?

miner

<img width="872" height="286" alt="image" src="https://github.com/user-attachments/assets/fc65d0cd-5f74-4927-a80a-0bf169f21bd1" />

5. Which option best represents the event? Choose from the following:
- False Positive
- True Positive

True Positive

6. Selecting the right ACTION will display the FLAG. What is the FLAG?

<img width="763" height="276" alt="image" src="https://github.com/user-attachments/assets/219f3162-6c16-43ac-ba60-104f99a9042d" />


















