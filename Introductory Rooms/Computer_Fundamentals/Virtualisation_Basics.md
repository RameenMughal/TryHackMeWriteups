# Virtualisation Basics

Room: [Virtualisation Basics](https://tryhackme.com/room/virtualisationbasics)

<img width="939" height="142" alt="image" src="https://github.com/user-attachments/assets/5101e46c-6816-43f3-ba68-2cd564573037" />

## Vitualization Overview

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

## Virtualization Components

### Hypervisor (The Building Manager)

A hypervisor is the core technology behind virtualization. It's the software that creates and manages virtual machines.

It is a special piece of software that:
- Divides a physical computer into multiple virtual ones.
- Gives each virtual machine its own share of CPU, memory, and storage.
- Keeps everything isolated and safe.
- Manages the lifecycle of virtual machines (start, stop, pause, clone, delete).

Hypervisors have two main types of implementation, each of which is used for specific scenarios, from home labs to large data centers:
- Type 1 hypervisors run directly on the physical hardware, making them fast, efficient, and ideal for servers and professional environments.
- Type 2 hypervisors run within an existing operating system, making them easier to install and ideal for learning, testing, or small setups.

Below is a table showing which use case is best suited to each hypervisor type. The use cases can run on both hypervisor types, but it's not the best approach given the main objectives of each.

<img width="1051" height="696" alt="image" src="https://github.com/user-attachments/assets/e3917a86-5918-43d5-9810-f3d90fa4a25d" />

When using virtualization to test malicious files, care should be taken to ensure that the host machine does not become infected by the malware being tested in the guest machine. One approach is to use different operating systems for the guest and host machines, or to isolate the guest machine so that it does not communicate with the host.

### Virtual Machines (The Apartments)

A Virtual Machine (VM) is a virtual computer created by the hypervisor.

Even though it’s virtual, it behaves as a real machine:
- It has its own virtual CPU, RAM, storage, and network.
- It can run any operating system (Windows, Linux, etc.).
- It’s completely isolated from other VMs. This means that if one VM breaks, the others continue to work.

You can deploy VMs on your own computer using tools such as Oracle VirtualBox and VMware Workstation. This type of software acts as a type 2 hypervisor and lets you run multiple operating systems, such as Windows, Linux, and macOS.

### Containers (The Rooms Inside the Apartment)

A container is a lightweight, isolated environment that runs a single application and all the necessary components to support it. Instead of bringing a whole separate operating system, a container borrows the core of the existing system by running on the kernel, which is the part of an operating system that communicates with the hardware and manages resources such as memory and running programs.

Because containers share this kernel, they start quickly and use fewer resources than full virtual machines, but it also means they must match the host system’s type. For example, you can’t run a Windows container on a Linux machine.

Containers behave like small, self-contained spaces because:
- They package the application and its dependencies (libraries, tools, versions).
- They share the host’s operating system, so they start almost instantly.
- They remain isolated from each other, so a misbehaving container doesn’t affect the others.
- They can run consistently on any machine, making them perfect for development, testing, and scalable deployments.

The easiest way to deploy containers in a VM is using Docker.
Docker is an open-source software platform that simplifies the process of building, deploying, and running applications using containerization.

The image below illustrates the relationship between Hypervisors, VMs, and containers:

<img width="1159" height="732" alt="image" src="https://github.com/user-attachments/assets/7b0867a2-ebcd-4c2e-ac82-bc5cc6c890dc" />

### Answer the questions below

1. Suppose a user wants to deploy a study lab on their machine to practice some exercises for a cyber security certification. Which type of hypervisor will they use?

Type 2

2. Suppose a company wants to host multiple small applications in the same virtual machine. What should they use?

Containers

## Managing Virtual Machines

<img width="1881" height="866" alt="image" src="https://github.com/user-attachments/assets/890152f5-2844-4f20-8f69-381a11b61cac" />

### Answer the questions below

1. What is the name of the virtual machine that has been running for the longest time?

Monitoring-SYS

<img width="1669" height="78" alt="image" src="https://github.com/user-attachments/assets/6e605d44-e18e-4bab-9974-c9cac3b11876" />

2. What is the name of the virtual machine that is using the biggest amount of memory?

DB-Cluster-01

<img width="1663" height="72" alt="image" src="https://github.com/user-attachments/assets/1d6c4cfa-3b11-4cd2-bc7f-69eadafcccdc" />

3. How many VMs are in the running state after you solved the issue on `Mail-SERVER`?

8

<img width="1799" height="849" alt="image" src="https://github.com/user-attachments/assets/ee8902d3-a254-48da-8e83-020f23f715a0" />

4. What is the name of the physical machine that is hosting most of the VMs?

HV-PROD-02

## Conclusion

### Key Terminology

Let's quickly review some concepts we learned in this room:
- **Virtualization**: Enables a single physical computer to act like multiple separate computers.
- **Hypervisor**: The “manager” software that makes and runs the virtual computers.
- **Virtual Machine (VM)**: A whole virtual computer inside the real one, with its own system.
- **Container**: A small, isolated box for one app that shares the same system as the host.
- **Container Images**: A pre-packed recipe/template used to create containers.
- **Network Ports**: Special numbered entry points that apps use to talk over the network.

We also concluded that the key benefits of virtualization are:
- Cost savings
- Better resource usage
- Safe testing for cyber security
- Faster deployment
- Flexibility
- Portability
- Scalability
- Centralized Management
