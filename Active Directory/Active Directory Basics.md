# Active Directory Basics

## Introduction

Microsoft's Active Directory is the backbone of the corporate world. It simplifies the management of devices and users within a corporate environment.

## Windows Domain

**Windows domain** is a group of users and computers under the administration of a given business. A Windows domain is like a big digital office where all the computers, users, and files are managed in one place by a company or organization.

The main idea behind a domain is to centralise the administration of common components of a Windows computer network in a single repository called **Active Directory (AD)**. At the center of this system is something called Active Directory (AD) — think of it like a master list or control center that keeps track of who can access what.

The server that runs the Active Directory services is known as a **Domain Controller (DC)**. The computer that runs and manages this Active Directory is called the Domain Controller (DC). It acts like the boss — it checks passwords, controls permissions, and makes sure everything is running smoothly across all the connected computers.

### Real World Example

In school/university networks, you will often be provided with a username and password that you can use on any of the computers available on campus. Your credentials are valid for all machines because whenever you input them on a machine, it will forward the authentication process back to the Active Directory, where your credentials will be checked. Thanks to Active Directory, your credentials don't need to exist in each machine and are available throughout the network.

Active Directory is also the component that allows your school/university to restrict you from accessing the control panel on your school/university machines. Policies will usually be deployed throughout the network so that you don't have administrative privileges over those computers.

### Answer the questions below

1. In a Windows domain, credentials are stored in a centralised repository called...

Active Directory

2. The server in charge of running the Active Directory services is called...

Domain Controller

## Active Directory

The core of any Windows Domain is the Active Directory Domain Service (AD DS). This service acts as a catalogue that holds the information of all of the "objects" that exist on your network. Amongst the many objects supported by AD, we have users, groups, machines, printers, shares and many others.

### Users

Users are one of the most common object types in Active Directory. Users are one of the objects known as security principals, meaning that they can be authenticated by the domain and can be assigned privileges over resources like files or printers. 

You could say that a security principal is an object that can act upon resources in the network.

Users can be used to represent two types of entities:
- **People**: users will generally represent persons in your organisation that need to access the network, like employees.
- **Services**: you can also define users to be used by services like IIS or MSSQL. Every single service requires a user to run, but service users are different from regular users as they will only have the privileges needed to run their specific service.

Just like people need a user account to log in and access things on a computer, services also need a kind of user account to run — but they are not real people. These are called service accounts.

### Machines

Machines are another type of object within Active Directory; for every computer that joins the Active Directory domain, a machine object will be created. Machines are also considered "security principals" and are assigned an account just as any regular user.

The machine accounts themselves are local administrators on the assigned computer, they are generally not supposed to be accessed by anyone except the computer itself, but as with any other account, if you have the password, you can use it to log in.

**Note**: Machine Account passwords are automatically rotated out and are generally comprised of 120 random characters.

Identifying machine accounts is relatively easy. They follow a specific naming scheme. The machine account name is the computer's name followed by a dollar sign. For example, a machine named `DC01` will have a machine account called `DC01$`.

### Security Groups






