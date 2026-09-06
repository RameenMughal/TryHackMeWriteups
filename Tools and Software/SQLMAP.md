# SQLMAP

Room: [SQLMAP](https://tryhackme.com/room/sqlmap)

<img width="944" height="203" alt="image" src="https://github.com/user-attachments/assets/f58c0b47-977b-4ef7-8b6e-f351b372e9f2" />

## Introduction

### What is sqlmap? 

sqlmap is an open source penetration testing tool developed by Bernardo Damele Assumpcao Guimaraes and Miroslav Stampar that automates the process of detecting and exploiting SQL injection flaws and taking over database servers.

It comes with a powerful detection engine, many niche features for the ultimate penetration tester, and a broad range of switches lasting from database fingerprinting, fetching data from the database, to accessing the underlying file system and executing commands on the operating system via out-of-band connections.

---

### Installing Sqlmap

If you're using Kali Linux, sqlmap is pre-installed. Otherwise, you can download it here: [sqlmap repo](https://github.com/sqlmapproject/sqlmap)

## Using Sqlmap

### Sqlmap Commands

To show the basic help menu, simply type `sqlmap -h` in the terminal.

<img width="430" height="359" alt="image" src="https://github.com/user-attachments/assets/4aba52e6-525b-4bc9-aa39-ad1e49dee822" />

**Basic commands**:

| **Option** | **Description** |
|---|---|
| `-u URL, --url=URL` | Target URL (e.g. `http://www.site.com/vuln.php?id=1`) |
| `--data=DATA` | Data string to be sent through POST (e.g. `id=1`) |
| `--random-agent` | Use randomly selected HTTP User-Agent header value |
| `-p TESTPARAMETER` | Testable parameter(s) |
| `--level=LEVEL` | Level of tests to perform (1-5, default 1) |
| `--risk=RISK` | Risk of tests to perform (1-3, default 1) |

**Enumeration commands**:

These options can be used to enumerate the back-end database management system information, structure, and data contained in tables.

| Options | Description |
| :--- | :--- |
| `-a`, `--all` | Retrieve everything |
| `-b`, `--banner` | Retrieve DBMS banner |
| `--current-user` | Retrieve DBMS current user |
| `--current-db` | Retrieve DBMS current database |
| `--passwords` | Enumerate DBMS users password hashes |
| `--dbs` | Enumerate DBMS databases |
| `--tables` | Enumerate DBMS database tables |
| `--columns` | Enumerate DBMS database table columns |
| `--schema` | Enumerate DBMS schema |
| `--dump` | Dump DBMS database table entries |
| `--dump-all` | Dump all DBMS databases tables entries |
| `--is-dba` | Detect if the DBMS current user is DBA |
| `-D <DB NAME>` | DBMS database to enumerate |
| `-T <TABLE NAME>` | DBMS database table(s) to enumerate |
| `-C COL` | DBMS database table column(s) to enumerate |

