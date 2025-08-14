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

Connecting to the Windows machine through RDP (Remote Desktop Protocol), install `xfreerdp3` in Kali Linux

The Remote Desktop Protocol (RDP) is a protocol, or technical standard, for using a desktop computer remotely.

Connect to the machine by `xfreerdp3 /v:MACHINE_IP /u:'THM\Administrator' /p:Password321 ` and then the windows login appears. Login with given credentials.

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

## Managing Users in AD

Your first task as the new domain administrator is to check the existing AD OUs and users, as some recent changes have happened to the business. You have been given the following organisational chart and are expected to make changes to the AD to match it:

<img width="1542" height="702" alt="image" src="https://github.com/user-attachments/assets/939ffbe4-7d56-4281-a7cc-02569d997a74" />

### Deleting extra OUs and users

The first thing you should notice is that there is an additional department OU in your current AD configuration that doesn't appear in the chart. We've been told it was closed due to budget cuts and should be removed from the domain. If you try to right-click and delete the OU, you will get the following error:

<img width="404" height="159" alt="image" src="https://github.com/user-attachments/assets/26ef0eaa-cc34-4a82-acab-fceb93094ccf" />

By default, OUs are protected against accidental deletion. To delete the OU, we need to enable the Advanced Features in the View menu

This will show you some additional containers and enable you to disable the accidental deletion protection. To do so, right-click the OU and go to Properties. You will find a checkbox in the Object tab to disable the protection

<img width="420" height="472" alt="image" src="https://github.com/user-attachments/assets/d18ba9a9-189c-404f-a86a-693931aa893a" />

Be sure to uncheck the box and try deleting the OU again. You will be prompted to confirm that you want to delete the OU, and as a result, any users, groups or OUs under it will also be deleted.

After deleting the extra OU, you should notice that for some of the departments, the users in the AD don't match the ones in our organisational chart. Create and delete users as needed to match them.

Delete the Research and Development OU as it is not in the chart and delete two users in the Sales department.

### Delegation

One of the nice things you can do in AD is to give specific users some control over some OUs. This process is known as delegation and allows you to grant users specific privileges to perform advanced tasks on OUs without needing a Domain Administrator to step in.

One of the most common use cases for this is granting IT support the privileges to reset other low-privilege users' passwords. According to our organisational chart, Phillip is in charge of IT support, so we'd probably want to delegate the control of resetting passwords over the Sales, Marketing and Management OUs to him.

For this example, we will delegate control over the Sales OU to Phillip. To delegate control over an OU, you can right-click it and select Delegate Control

This should open a new window where you will first be asked for the users to whom you want to delegate control as Delegation of Control Wizard

**Note**: To avoid mistyping the user's name, write "phillip" and click the Check Names button. Windows will autocomplete the user for you.

<img width="583" height="570" alt="image" src="https://github.com/user-attachments/assets/4f432c0f-f87d-432a-8025-4d82ffe4ba37" />

Click OK, and on the next step, select the following option to Reset password

<img width="531" height="414" alt="image" src="https://github.com/user-attachments/assets/edf3b1a2-c0f8-48e9-a8b3-1dc9ea573142" />

Click next a couple of times, and now Phillip should be able to reset passwords for any user in the sales department.

Now let's use Phillip's account to try and reset Sophie's password.

Login to the Phillip's account by `xfreerdp3 /v:MACHINE_IP /u:'THM\phillip' /p:Claire2008` 

While you may be tempted to go to Active Directory Users and Computers to try and test Phillip's new powers, he doesn't really have the privileges to open it, so you'll have to use other methods to do password resets. In this case, we will be using Powershell to do so

The password should not be too short or simple, I used Sunset!42

<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/107dccd3-4213-4a05-b294-bb19741cf614" />

Since we wouldn't want Sophie to keep on using a password we know, we can also force a password reset at the next logon with the following command:

<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/eb36461f-1fb8-4dc6-8bad-54cb36a809df" />

Then Login to the Sophie account to get the flag `xfreerdp3 /v:MACHINE_IP /u:'THM\sophie' /p:'Sunset!42'`

I used '' with the password as the shell was not accepting number 42 with the password

It asks us to give it a new password as the password needs to be changed before logging in. So give it a new password and then you get the access

### Answer the questions below

1. What was the flag found on Sophie's desktop?

Logging in to the Sophie account, you see flag.txt at the Desktop

<img width="300" height="100" alt="image" src="https://github.com/user-attachments/assets/f702d6fd-6d60-4b28-83fa-7eeabf23979b" />

2. The process of granting privileges to a user over some OU or other AD Object is called...

Delegation

## Managing Computers in AD

By default, all the machines that join a domain (except for the DCs) will be put in the container called "Computers".

We can see some servers, some laptops and some PCs corresponding to the users in our network. Having all of our devices there is not the best idea since it's very likely that you want different policies for your servers and the machines that regular users use on a daily basis.

In general, you'd expect to see devices divided into at least the three following categories:

### 1. Workstations

Workstations are one of the most common devices within an Active Directory domain. Each user in the domain will likely be logging into a workstation. This is the device they will use to do their work or normal browsing activities. These devices should never have a privileged user signed into them.

### 2. Servers

Servers are the second most common device within an Active Directory domain. Servers are generally used to provide services to users or other servers.

### 3. Domain Controllers

Domain Controllers are the third most common device within an Active Directory domain. Domain Controllers allow you to manage the Active Directory Domain. These devices are often deemed the most sensitive devices within the network as they contain hashed passwords for all user accounts within the environment.

Now, move the personal computers and laptops to the Workstations OU and the servers to the Servers OU from the Computers container. Doing so will allow us to configure policies for each OU later.

### Answer the questions below

1. After organising the available computers, how many ended up in the Workstations OU?

7

2. Is it recommendable to create separate OUs for Servers and Workstations? (yay/nay)

yay

## Group Policies

So far, we have organised users and computers in OUs just for the sake of it, but the main idea behind this is to be able to deploy different policies for each OU individually. That way, we can push different configurations and security baselines to users depending on their department.

Windows manages such policies through Group Policy Objects (GPO). GPOs are simply a collection of settings that can be applied to OUs. GPOs can contain policies aimed at either users or computers, allowing you to set a baseline on specific machines and identities.

To configure GPOs, you can use the Group Policy Management tool, available from the start menu

The first thing you will see when opening it is your complete OU hierarchy, as defined before. To configure Group Policies, you first create a GPO under Group Policy Objects and then link it to the OU where you want the policies to apply

<img width="954" height="577" alt="image" src="https://github.com/user-attachments/assets/c2bed534-fbaf-49e5-a86c-75eb287f8d86" />

We can see in the image above that 3 GPOs have been created. From those, the Default Domain Policy and RDP Policy are linked to the thm.local domain as a whole, and the Default Domain Controllers Policy is linked to the Domain Controllers OU only. Something important to have in mind is that any GPO will apply to the linked OU and any sub-OUs under it. For example, the Sales OU will still be affected by the Default Domain Policy.

Let's examine the Default Domain Policy to see what's inside a GPO. The first tab you'll see when selecting a GPO shows its scope, which is where the GPO is linked in the AD. For the current policy, we can see that it has only been linked to the thm.local domain:

<img width="954" height="577" alt="image" src="https://github.com/user-attachments/assets/f50b734a-d149-4b69-9d8d-1f6d4b1d4225" />

As you can see, you can also apply Security Filtering to GPOs so that they are only applied to specific users/computers under an OU. By default, they will apply to the Authenticated Users group, which includes all users/PCs.

The Settings tab includes the actual contents of the GPO and lets us know what specific configurations it applies. As stated before, each GPO has configurations that apply to computers only and configurations that apply to users only. In this case, the Default Domain Policy only contains Computer Configurations:

<img width="954" height="598" alt="image" src="https://github.com/user-attachments/assets/bcbe599d-08be-463b-9c97-b7ece669a891" />

Since this GPO applies to the whole domain, any change to it would affect all computers. Let's change the minimum password length policy to require users to have at least 10 characters in their passwords. To do this, right-click the GPO and select Edit

<img width="418" height="374" alt="image" src="https://github.com/user-attachments/assets/1368bc08-818a-4522-a6a9-cce15c40c56e" />

This will open a new window where we can navigate and edit all the available configurations. To change the minimum password length, go to Computer Configurations -> Policies -> Windows Setting -> Security Settings -> Account Policies -> Password Policy and change the required policy value:

<img width="787" height="565" alt="image" src="https://github.com/user-attachments/assets/3c3609dd-daf0-4960-8dfa-4b180aca05bb" />

### GPO Distribution

GPOs are distributed to the network via a network share called `SYSVOL`, which is stored in the DC. All users in a domain should typically have access to this share over the network to sync their GPOs periodically. The SYSVOL share points by default to the `C:\Windows\SYSVOL\sysvol\` directory on each of the DCs in our network.

Once a change has been made to any GPOs, it might take up to 2 hours for computers to catch up. If you want to force any particular computer to sync its GPOs immediately, you can always run the following command on the desired computer: `gpupdate /force`

### Creating some GPOs for THM Inc.

As part of our new job, we have been tasked with implementing some GPOs to allow us to:

1. Block non-IT users from accessing the Control Panel.

2. Make workstations and servers lock their screen automatically after 5 minutes of user inactivity to avoid people leaving their sessions exposed.

#### Restrict Access to Control Panel

We want to restrict access to the Control Panel across all machines to only the users that are part of the IT department. Users of other departments shouldn't be able to change the system's preferences.

Let's create a new GPO called Restrict Control Panel Access and open it for editing. Since we want this GPO to apply to specific users, we will look under User Configuration for the following policy:

Create New GPO, then Edit then User Configuration -> Administrative Templates -> Control Panel -> Click the Policy and click Enabled

<img width="919" height="565" alt="image" src="https://github.com/user-attachments/assets/29fc6d5f-7801-4d07-ba78-10a2ac61de23" />

Once the GPO is configured, we will need to link it to all of the OUs corresponding to users who shouldn't have access to the Control Panel of their PCs. In this case, we will link the Marketing, Management and Sales OUs by dragging the GPO to each of them:

<img width="923" height="619" alt="image" src="https://github.com/user-attachments/assets/a6020217-7e63-45d8-ba0a-18e7a6c80d84" />

#### Auto Lock Screen GPO

For the first GPO, regarding screen locking for workstations and servers, we could directly apply it over the Workstations, Servers and Domain Controllers OUs we created previously.

While this solution should work, an alternative consists of simply applying the GPO to the root domain, as we want the GPO to affect all of our computers. Since the Workstations, Servers and Domain Controllers OUs are all child OUs of the root domain, they will inherit its policies.

**Note**: You might notice that if our GPO is applied to the root domain, it will also be inherited by other OUs like Sales or Marketing. Since these OUs contain users only, any Computer Configuration in our GPO will be ignored by them.

Let's create a new GPO, call it Auto Lock Screen, and edit it. The policy to achieve what we want is located in the following route:

Create, Edit then Computer Configuration -> Policies -> Windows Settings -> Security Settings -> Local Policies -> Security Options -> Interactive logon: Machine inactivity limit

<img width="787" height="565" alt="image" src="https://github.com/user-attachments/assets/d4cb0fce-4349-457b-9222-ff5d2e0fee8b" />

We will set the inactivity limit to 5 minutes so that computers get locked automatically if any user leaves their session open. After closing the GPO editor, we will link the GPO to the root domain by dragging the GPO to it:

<img width="923" height="579" alt="image" src="https://github.com/user-attachments/assets/42f30c18-7ef8-4cc1-aec3-9e62ded19b2c" />

Once the GPOs have been applied to the correct OUs, we can log in as any users in either Marketing, Sales or Management for verification. For this task, let's connect via RDP using Mark's credentials

If we try opening the Control Panel, we should get a message indicating this operation is denied by the administrator. You can also wait 5 minutes to check if the screen is automatically locked if you want.

Since we didn't apply the control panel GPO on IT, you should still be able to log into the machine as any of those users and access the control panel. 

Note: If you created and linked the GPOs, but for some reason, they still don't work, remember you can run `gpupdate /force` to force GPOs to be updated.

### Answer the questions below

1. What is the name of the network share used to distribute GPOs to domain machines?

SYSVOL

2. Can a GPO be used to apply settings to users and computers? (yay/nay)

yay





























