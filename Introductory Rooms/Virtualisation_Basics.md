# Virtualisation Basics

Room: [Virtualisation Basics](https://tryhackme.com/room/virtualisationbasics)

<img width="939" height="142" alt="image" src="https://github.com/user-attachments/assets/5101e46c-6816-43f3-ba68-2cd564573037" />

## Vitualisation Overview

Before the concept of virtualization, the rule of thumb in IT was: “One server = one application.”

This meant that if a company wanted to run a website, a database, an email service, and an internal app, they would need separate physical servers for each one. The problems were obvious:
- High cost: Buying multiple physical servers is expensive, not just the hardware, but also electricity, cooling, maintenance, and data center space.
- Low utilization: Most applications don’t use the server’s full capacity. Many servers stayed at 5–20% usage, wasting CPU, memory, and storage resources.
- Slow deployment: Setting up new physical servers could take days or weeks.
- Hard to scale: If an application suddenly needed more resources, you often had to buy yet another server.

### The Need for Sharing Hardware Safely and Efficiently

Virtualization introduced a new idea: “What if multiple applications could share the same physical server safely?”

A virtualization layer, called a hypervisor, was introduced to act as a referee between virtual machines and allow each virtual computer to behave independently, like a physical computer.

### The Building Analogy

This is virtualization:
- The building = the physical server
- The apartments = virtual machines
- The tenants = applications or operating systems
- The building manager = the hypervisor (the software that divides the building safely)

Each virtual computer, known as a Virtual Machine (VM), acts as an independent system with its own operating system, apps, and settings, even though they all share the same physical hardware underneath.

### Answer the questions below

1. What does virtualization enable multiple applications to share?

Physical Server

2. What is the name of the software that manages the resources for each virtual machine?

Hypervisor


