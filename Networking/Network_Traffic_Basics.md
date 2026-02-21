# Network Traffic Basics

## Introduction

Network Traffic Analysis (NTA) is a process that encompasses capturing, inspecting, and analyzing data as it flows in a network. 

Its goal is to have complete visibility and understand what is communicated inside and outside the network. 

It is important to stress that NTA is not a synonym for the tool Wireshark. It is more than that: It is a combination of correlating several logs, deep packet inspection, and network flow statistics with specific outlined goals 

In this room, we will focus on defining network traffic analysis, why you need it, what and how you can observe network traffic, and some of the sources and flows of network traffic you need to be aware of.

## What is the Purpose of Network Traffic Analysis?

Why should we analyze network traffic? Before we answer this question, let's look at the following scenario.

### DNS Tunneling and Beaconing

You are an SOC analyst, and you receive an alert stating that an unusual number of DNS queries are coming from a host named WIN-016 with IP 192.168.1.16. The DNS logs on the firewall show multiple DNS queries going to the same TLD, each time using a different subdomain.
