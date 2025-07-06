# Shodan.io

## Introduction

Shodan.io is a search engine for the Internet of Things.

Shodan scans the whole internet and indexes the services run on each IP address.

### Finding Services

Let’s say we are performing a pentest on a company, and we want to find out what services one of their servers run.

We need to grab their IP address. We can do this using ping.

Then we put the IP address and get to know the services used by that IP address


Cloudflare acts as a proxy between TryHackMe and their real servers. If we were pentesting a large company, this isn’t helpful. We need some way to get their IP addresses.

We can do this using Autonomous System Numbers.

### Autonomous System Numbers

An autonomous system number (ASN) is a global identifier of a range of IP addresses. If you are an enormous company like Google you will likely have your own ASN for all of the IP addresses you own.

We can put the IP address into an ASN lookup tool such as https://asnlookup.com/, which tells us they have the ASN AS14061

When we google AS14061 we can see it is a DigitalOcean ASN number.

### Getting Started

Devices run services, and Shodan stores information about them. The information is stored in a banner. It’s the most fundamental part of Shodan.

An example banner looks like:

```
{
  "data": "Moxa Nport Device",
  "Status": "Authentication disabled",
  "Name": "NP5232I_4728",
  "MAC": "00:90:e8:47:10:2d",
  "ip_str": "46.252.132.235",
  "port": 4800,
  "org": "Starhub Mobile",
  "location":
   {
            "country_code": "SG"
         }
}
```

We’re looking at the output of a single port, which includes information about the IP and authentication details.

## Filters

If we look at the search, we can see it is another filter. `product:MySQL`

On TryHackMe’s ASN, let’s try to find some MYSQL servers.

We use this search query `asn:AS14061 product:MySQL`

There is a filter that lets you know IP addresses that are vulnerable to exploit  such as `vuln:ms17-010`

### API

API, which stands for Application Programming Interface, is a set of rules and protocols for building software and applications. 

An API allows different software programs to communicate with each other. 

It defines methods of communication between various components, including the kinds of requests that can be made, how they're made, the data formats that should be used, and conventions to follow.

Shodan has an API

The API lets us programmatically search Shodan and receive a list of IP addresses in return. If we are a company, we can write a script to check over our IP addresses to see if any of them are vulnerable.

### Answer the questions below

What command is used to find Eternal Blue exploits on Shodan using the vuln filter?

`vuln:ms17-010`

## Google & Filtering

### Answer the questions below

1. What is the top operating system for MYSQL servers in Google's ASN?

Search `ASN:AS15169 PRODUCT:MYSQL`

**Answer**: 5.6.40-84.0-log

2. What is the 2nd most popular country for MYSQL servers in Google's ASN?

**Answer**: Netherlands

3. Under Google's ASN, which is more popular for nginx, Hypertext Transfer Protocol or Hypertext Transfer Protocol with SSL?

Search `ASN:AS15169 PRODUCT:nginx`

**Answer**: Hypertext Transfer Protocol

4. Under Google's ASN, what is the most popular city?

Search `ASN:AS15169 COUNTRY:US`

**Answer**: Kansas City

5. Under Google's ASN in Los Angeles, what is the top operating system according to Shodan?

Search `ASN:AS15169 COUNTRY:US CITY:Los Angeles`

**Answer**: Debian

6. Using the top Webcam search from the explore page, does Google's ASN have any webcams? Yay / nay.

Search `webcam ASN:AS15169`

**Answer**: Nay

## Shodan Monitor

Shodan Monitor is an application for monitoring your devices in your own network.

It asks for an IP range

When we add a network, we can see it in dashboard

If we click on the settings cog, we can see that we have a range of “scans” Shodan performs against our network.

Anytime Shodan detects a security vulnerability in one of these categories, it will email us.

The interesting part is that you can actually monitor other peoples networks using this. For bug bounties you can save a list of IPs and Shodan will email you if it finds any problems.

### Answer the questions below

What URL takes you to Shodan Monitor?

**Answer**: https://monitor.shodan.io/dashboard

## Shodan Dorking
Shodan has some lovely webpages with Dorks that allow us to find things. 

Example: `has_screenshot:true encrypted attention`

Which uses optical character recognition and remote desktop to find machines compromised by ransomware on the internet. 

### Answer the questions below

What dork lets us find PCs infected by Ransomware?

**Answer**: `has_screenshot:true encrypted attention`

## Shodan Extension

Shodan also has an extension.

When installed, you can click on it and it’ll tell you the IP address of the webserver running, what ports are open, where it’s based and if it has any security issues.
