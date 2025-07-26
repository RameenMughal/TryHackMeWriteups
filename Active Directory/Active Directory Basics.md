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

If you are familiar with Windows, you probably know that you can define user groups to assign access rights to files or other resources to entire groups instead of single users. This allows for better manageability as you can add users to an existing group, and they will automatically inherit all of the group's privileges. 

Security groups are also considered security principals and, therefore, can have privileges over resources on the network.

Groups can have both users and machines as members. If needed, groups can include other groups as well.

Several groups are created by default in a domain that can be used to grant specific privileges to users. As an example, here are some of the most important groups in a domain:

| **Security Group**     | **Description**                                                                                   |
|------------------------|---------------------------------------------------------------------------------------------------|
| Domain Admins          | Users of this group have administrative privileges over the entire domain. By default, they can administer any computer on the domain, including the DCs. |
| Server Operators       | Users in this group can administer Domain Controllers. They cannot change any administrative group memberships. |
| Backup Operators       | Users in this group are allowed to access any file, ignoring their permissions. They are used to perform backups of data on computers. |
| Account Operators      | Users in this group can create or modify other accounts in the domain.                           |
| Domain Users           | Includes all existing user accounts in the domain.                                               |
| Domain Computers       | Includes all existing computers in the domain.                                                   |
| Domain Controllers     | Includes all existing DCs on the domain.                                                         |

### Active Directory Users and Computers

To configure users, groups or machines in Active Directory, we need to log in to the Domain Controller and run "Active Directory Users and Computers" from the start menu

This will open up a window where you can see the hierarchy of users, computers and groups that exist in the domain. These objects are organised in **Organizational Units (OUs)** which are container objects that allow you to classify users and machines. OUs are mainly used to define sets of users with similar policing requirements. 

The people in the Sales department of your organisation are likely to have a different set of policies applied than the people in IT, for example. Keep in mind that a user can only be a part of a single OU at a time.

It is very typical to see the OUs mimic the business' structure, as it allows for efficiently deploying baseline policies that apply to entire departments. Remember that while this would be the expected model most of the time, you can define OUs arbitrarily.

If you open any OUs, you can see the users they contain and perform simple tasks like creating, deleting or modifying them as needed. You can also reset passwords if needed (pretty useful for the helpdesk)

You probably noticed already that there are other default containers apart from the THM OU. These containers are created by Windows automatically and contain the following:
- **Builtin**: Contains default groups available to any Windows host.
- **Computers**: Any machine joining the network will be put here by default. You can move them if needed.
- **Domain Controllers**: Default OU that contains the DCs in your network.
- **Users**: Default users and groups that apply to a domain-wide context.
- **Managed Service Accounts**: Holds accounts used by services in your Windows domain.

### Security Groups vs OUs

You are probably wondering why we have both groups and OUs. While both are used to classify users and computers, their purposes are entirely different:
- OUs are handy for applying policies to users and computers, which include specific configurations that pertain to sets of users depending on their particular role in the enterprise. Remember, a user can only be a member of a single OU at a time, as it wouldn't make sense to try to apply two different sets of policies to a single user.
- Security Groups, on the other hand, are used to grant permissions over resources. For example, you will use groups if you want to allow some users to access a shared folder or network printer. A user can be a part of many groups, which is needed to grant access to multiple resources.

### Answer the questions below

1. Which group normally administrates all computers and resources in a domain?

Domain Admins

2. What would be the name of the machine account associated with a machine named TOM-PC?

`TOM-PC$`

3. Suppose our company creates a new department for Quality Assurance. What type of containers should we use to group all Quality Assurance users so that policies can be applied consistently to them?

Organizational Units










