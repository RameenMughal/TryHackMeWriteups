# Passive Reconnaissance

## Introduction

We will learn three command-line tools:
- whois to query WHOIS Servers
- nslookup to query DNS Servers
- dig to query DNS Servers

These are all publicly available records and hence do not alert the target.

We will also learn the usage of two online services:
- DNSDumpster
- Shodan.io

## Passive Versus Active Recon

Reconnaissance (recon) can be defined as a preliminary survey to gather information about a target. 

We divide reconnaissance into:
1.	Passive Reconnaissance
2.	Active Reconnaissance

In passive reconnaissance, you rely on publicly available knowledge. It is the knowledge that you can access from publicly available resources without directly engaging with the target.

Passive reconnaissance activities include many activities, for instance:
- Looking up DNS records of a domain from a public DNS server.
- Checking job ads related to the target website.
- Reading news articles about the target company.

Active reconnaissance, on the other hand, cannot be achieved so discreetly. It requires direct engagement with the target. 

Examples of active reconnaissance activities include:
- Connecting to one of the company servers such as HTTP, FTP, and SMTP.
- Calling the company in an attempt to get information (social engineering).
- Entering company premises pretending to be a repairman.

### Answer the questions below

1. You visit the Facebook page of the target company, hoping to get some of their employee names. What kind of reconnaissance activity is this? (A for active, P for passive)

P

2. You ping the IP address of the company webserver to check if ICMP traffic is blocked. What kind of reconnaissance activity is this? (A for active, P for passive)

A

3. You happen to meet the IT administrator of the target company at a party. You try to use social engineering to get more information about their systems and network infrastructure. What kind of reconnaissance activity is this? (A for active, P for passive)

A

## Whois

WHOIS is a request and response protocol that follows the RFC 3912 specification. A WHOIS server listens on TCP port 43 for incoming requests. The domain registrar is responsible for maintaining the WHOIS records for the domain names it is leasing. The WHOIS server replies with various information related to the domain requested. Of particular interest, we can learn:
- Registrar: Via which registrar was the domain name registered?
- Contact info of registrant: Name, organization, address, phone, among other things. (unless made hidden via a privacy service)
- Creation, update, and expiration dates: When was the domain name first registered? When was it last updated? And when does it need to be renewed?
- Name Server: Which server to ask to resolve the domain name?

To get this information, we need to use a whois client or an online service. Many online services provide whois information;

The syntax is `whois DOMAIN_NAME`, where `DOMAIN_NAME` is the domain about which you are trying to get more information.

The information collected can be inspected to find new attack surfaces, such as social engineering or technical attacks. 

### Answer the questions below

1. When was TryHackMe.com registered?

20180705

2. What is the registrar of TryHackMe.com?

namecheap.com

3. Which company is TryHackMe.com using for name servers?

cloudflare.com

## nslookup and dig

Find the IP address of a domain name using nslookup, which stands for Name Server Look Up. You need to issue the command nslookup DOMAIN_NAME

You can use `nslookup OPTIONS DOMAIN_NAME SERVER`. These three main parameters are:
- `OPTIONS` contains the query type as shown in the table below. For instance, you can use A for IPv4 addresses and AAAA for IPv6 addresses.
- `DOMAIN_NAME` is the domain name you are looking up.
- `SERVER` is the DNS server that you want to query. You can choose any local or public DNS server to query. Cloudflare offers 1.1.1.1 and 1.0.0.1, Google offers 8.8.8.8 and 8.8.4.4, and Quad9 offers 9.9.9.9 and 149.112.112.112.

Following are the query type and their results:
- `A`: IPv4 Address
- `AAAA`: IPv6 Address
- `CNAME`: Canonical Name ( type of DNS record that maps an alias name to a true or canonical domain name)
- `MX`: Mail Servers
- `SOA`: Start of Authority
- `TXT`: TXT Records

For instance, `nslookup -type=A tryhackme.com 1.1.1.1` (or `nslookup -type=a tryhackme.com 1.1.1.1` as it is case-insensitive) can be used to return all the IPv4 addresses used by tryhackme.com.

You can issue `nslookup -type=MX tryhackme.com`

We can use `dig DOMAIN_NAME`, but to specify the record type, we would use `dig DOMAIN_NAME TYPE`. Optionally, we can select the server we want to query using `dig @SERVER DOMAIN_NAME TYPE`.
- `SERVER` is the DNS server that you want to query.
- `DOMAIN_NAME` is the domain name you are looking up.
- `TYPE` contains the DNS record type, as shown in the table provided earlier.

 If you want to query a 1.1.1.1 DNS server, you can execute `dig @1.1.1.1 tryhackme.com MX`.

 ### Answer the questions below

 Check the TXT records of thmlabs.com. What is the flag there?

By command `nslookup -type=TXT thmlabs.com` or `dig thmlabs.com TXT`

## DNSDumpster

There are many subdomains that tools like `nslookup` or `dig` wont give.

If we search DNSDumpster for tryhackme.com, we will discover the subdomain blog.tryhackme.com, which a typical DNS query cannot provide. 

In addition, DNSDumpster will return the collected DNS information in easy-to-read tables and a graph. DNSDumpster will also provide any collected information about listening servers.

### Answer the questions below

Lookup tryhackme.com on DNSDumpster. What is one interesting subdomain that you would discover in addition to www and blog? 

remote

## Shodan.io

Shodan.io tries to connect to every device reachable online to build a search engine of connected “things” in contrast with a search engine for web pages. Once it gets a response, it collects all the information related to the service and saves it in the database to make it searchable.

### Answer the questions below

1. According to Shodan.io, what is the 2nd country in the world in terms of the number of publicly accessible Apache servers?

China

2. Based on Shodan.io, what is the 3rd most common port used for Apache?

8080

3. Based on Shodan.io, what is the 3rd most common port used for nginx?

5001
