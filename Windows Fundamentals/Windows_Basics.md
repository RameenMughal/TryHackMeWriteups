# Windows Basics

Room: [Windows Basics](https://tryhackme.com/room/windowsbasics)

<img width="1876" height="393" alt="image" src="https://github.com/user-attachments/assets/a088dc39-b4d3-4c05-a808-9cd52498a1d6" />

## Introduction

<img width="1916" height="887" alt="image" src="https://github.com/user-attachments/assets/2cde636e-f65d-4da1-bc65-7c4b4429ff19" />

## Exploring the Windows Workspace

Before Windows had its current polished look, Microsoft’s operating systems were much simpler. Early computers ran MS-DOS, which showed a black screen where you had to type commands instead of clicking icons. 

In 1985, Microsoft released Windows 1.0, a basic graphical user interface (GUI) built on top of DOS, introducing windows, menus, and mouse controls to personal computers. 

Over time, Windows has added more features, which turned the original shell into a complete operating system. Today, the modern Windows OS is the result of those changes.

<img width="1451" height="377" alt="image" src="https://github.com/user-attachments/assets/d6135313-581f-4ee7-b03a-a7057920d127" />

### Logging in and Authentication

Before gaining access to the Windows Desktop, you must authenticate (prove your identity) to the system. The authentication process verifies your identity and determines the actions you're allowed to take once logged in. When a Windows system starts, it displays a login screen where a user account must be selected and authenticated with a password, PIN, or another verification method. 

Each user is assigned a set of permission levels that determine their access to files, settings, and system functionality. Windows commonly uses the account types below.
- **Guest**: A restricted account intended for temporary access, with minimal permissions and no ability to change system settings
- **Standard**: A user account for everyday tasks, such as running applications and changing personal settings, without access to system-wide changes
- **Administrator**: A privileged account with full control over the system, including software installation, configuration changes, and user management

---

### The Windows Desktop

You can consider the Desktop to be the airport terminal. After entering, it is the first area you gain access to, and all other subsequent areas branch out from this point. 

Let's have a look at the Windows Desktop and cover some of its core features together. When you first log in, you're presented with two main areas.
- **Desktop**: The main workspace where files, folders, and shortcuts live
- **Taskbar**: A control strip that provides access to applications, system tools, settings, and notifications

Let's break these down further to get a better picture.
1. **Desktop icons**: Shortcuts to items like the Recycle Bin, folders, and frequently used applications. It is fully customizable
2. **Start menu**: Primary way to access applications, settings, and power options. From here, you can log out, restart, or power off your machine
3. **Search**: Quickly find applications, files, folders, and system settings by using keywords
4. **Task View**: Allows you to see all currently open windows and quickly switch between them
5. **Pinned Applications and Folders**: Your most used applications and folders can be pinned here
6. **Network and Audio settings**: This section can be customized to suit your needs
7. **Date and Time**: Opens up to a full calendar. Date and time settings can be accessed here, too
8. **Notifications**: Displays computer or application notifications. Network and other settings can also be accessed

<img width="520" height="457" alt="image" src="https://github.com/user-attachments/assets/5423f4c4-606c-4671-b9b5-0fe83ca96d88" />


#### Start Menu

When using Windows, the Start menu can be accessed by clicking the Windows icon located at the bottom left of the taskbar. It is the area where we see what is available: apps, files, folders, settings, and power options. You can think of it as a quick-access menu.

<img width="495" height="520" alt="image" src="https://github.com/user-attachments/assets/66014994-fe43-4590-943c-e1f5e9978c78" />

---

### Built-in Tools and Apps

Beyond the wide range of settings available to manage your system, Windows also includes simple but powerful tools such as Notepad for editing text files and File Explorer for navigating and managing files. These tools are available immediately and form the foundation of everyday Windows usage. All of them can be accessed via the Start menu and search bar. 

<img width="557" height="247" alt="image" src="https://github.com/user-attachments/assets/b5d3f3fd-d715-4fe7-9cc2-228315dd6a81" />

---

### Getting System Information

Windows includes a built-in Settings application that allows you to configure and view information about your system. To get to know your new work PC better, we’ll start by investigating the machine we’re working with. Within the Settings app, there's a helpful section called About your PC, that provides key details about the system. 

The About your PC page provides an overview of security, device, and operating system information. 

<img width="1351" height="879" alt="image" src="https://github.com/user-attachments/assets/807e84ad-efe9-41da-95b9-f1d4937482c9" />

---

### File Exploration and Management

Let’s take a look at how Windows handles file exploration and management as we access some of the onboarding documents for your new position. 

Windows uses a hierarchical folder structure, meaning folders can contain other folders and files inside them. This structure helps keep data organized and makes it easier to locate information as systems grow larger. Common locations, such as the Desktop, Documents, and Downloads, serve as primary directories for storing files. Within these locations, subfolders are used to group related files together.

You can now open the `TryHatMe Onboarding` folder on the Desktop. Alternatively, you can open the File Explorer application, which is pinned to the Taskbar, or use the Start menu to locate the folder.
1. Open the `TryHatMe Onboarding` folder on your Desktop
2. This opens the folder in the Windows File Explorer
3. Options for viewing, sharing, and editing folders and files
4. Clicking the folder name will show us the full path to the chosen folder `C:\Users\Administrator\Desktop\TryHatMe Onboarding`
5. The displayed contents of our chosen folder
6. We can use the File Explorer's built-in search function to search our folder

<img width="520" height="250" alt="image" src="https://github.com/user-attachments/assets/fa8898a7-0704-43d6-95cc-7dfce07d380c" />

---

### Answer the questions below

1. After opening About your PC, navigate to the Device specifications section. What is the Device name specified?

TryHatMe

<img width="350" height="350" alt="image" src="https://github.com/user-attachments/assets/723df685-3d06-4b5c-9521-86518e8774fd" />


2. Continue looking through the Device specifications. How much RAM is installed on your new work PC?

4.00 GB

3. Scroll down to the Windows specifications section. Which Version of Windows Server 2019 Datacenter is installed?

1809

<img width="300" height="350" alt="image" src="https://github.com/user-attachments/assets/1de556d1-8f11-4a0a-8986-e8dcad82da7f" />


4. Explore the `TryHatMe Onboarding` folder located on your computer's Desktop. What is the flag value found within `Welcome.txt`?

<img width="1000" height="700" alt="image" src="https://github.com/user-attachments/assets/fd16b089-a1fe-4188-a8bd-fd6205dcd8c7" />

## Configuring and Securing Windows

Applications are the programs and tools you use to perform tasks on your computer, from browsing the web and editing photos to managing settings on your PC. We already discussed a few of the built-in applications Windows provides, but knowing how to install, update, and remove applications is a core skill for everyday Windows use. These three processes enable you to make the necessary changes to your system, ensuring you have exactly what you need and that your system remains secure.

### Updating Your Applications

Keeping your operating system and applications up to date is an important part of maintaining a secure and stable system. Updates will often include security patches, performance updates, and bug fixes.

#### Windows Updates

Windows includes a built-in update tool called Windows Update, which keeps the OS and some native applications and security features up to date. Windows Update can be accessed through the Settings app and may install updates automatically, depending on your configuration.

<img width="740" height="254" alt="image" src="https://github.com/user-attachments/assets/3327e327-7abb-40bf-93e3-e47a7ff7747b" />

#### Updating Applications

Application updates work differently depending on how the software is installed.
- Built-in applications may update automatically in the background
- Third-party applications often include their own update mechanisms
- Some applications will prompt you to update upon launch
- Some require you to check for updates or download a new installer manually

---

### Installing Applications

Now that you've seen how updates work within the Windows OS and for applications, let's take a look at installing new ones.
- **Microsoft Store**: Provides a curated and safe option for installing apps to Windows, although it is not available by default on Windows Server
- **From the Internet**: In many environments, apps are installed by downloading an installer directly from a trusted vendor's website. They usually come in an `.exe` or `.msi` file and guide the user through the installation process

<img width="879" height="283" alt="image" src="https://github.com/user-attachments/assets/04152dfa-0c0c-4156-aa21-631aeadef37d" />

---

### Uninstalling Applications

In a Windows environment, there are multiple ways to uninstall programs.
- Using the Microsoft Store for installed applications
- Add or remove programs feature in system settings
- Uninstall a program section of the Control Panel
- Using an application's built-in uninstaller

<img width="408" height="230" alt="image" src="https://github.com/user-attachments/assets/cbdde902-6bb0-49b0-bf07-9488a25a1e7e" />

---

### Diving Into Settings

Now, we will take a closer look at the abundance of configurations available to us. There are two primary ways in which a Windows user can modify their environment. There are existing shortcuts for each of the tools below placed on your Desktop.
- **Windows Settings**: A modern, centralized location for configuring system, device, personalization, and security settings in Windows
- **Control Panel**: A legacy management interface that provides access to older system configuration tools still required for specific administrative tasks

Windows Settings and the Control Panel enable you to view and modify how your Windows system operates. From these two applications, you can manage system preferences, including display and audio settings, user accounts, apps, network options, accessibility features, and security configurations.

<img width="959" height="289" alt="image" src="https://github.com/user-attachments/assets/c4b3e616-82c9-4164-b2b0-4af7f27438db" />

---

### The Task Manager

Task Manager is a built-in Windows tool that allows you to monitor what is happening on your system in real time. It allows you to view running applications and background processes, as well as check system performance, including CPU and memory usage. 

Task Manager has five tabs to help you keep track of your system.
- **Processes**: Currently running apps and background processes, and their resource usage
- **Performance**: Graphs and statistics for system resources such as CPU, memory, and network
- **Users**: Currently logged-in users and used resources 
- **Details**: A more technical view of running processes, including process IDs (PIDs)
- **Services**: Windows services and their current status (running or stopped)

<img width="520" height="400" alt="image" src="https://github.com/user-attachments/assets/10d8fe13-c315-48ee-8188-a0f110e1fded" />

---

### Native Windows Security

Windows offers built-in security tools designed to help protect your system from threats such as malware, insecure applications, and unauthorized network access. These are enabled by default and allow the monitoring and control of your system's security. 

#### Windows Security

The Windows Security application is your central dashboard for managing Windows' built-in protection measures. It is divided into four main sections, each focusing on a different area of system security.
- **Virus & threat protection**: Helps detect and remove malicious software using real-time protection and customizable scans
- **Firewall & network protection**: Controls incoming and outgoing network traffic to help prevent unauthorized access
- **App & browser control**: Protects users from potentially unsafe apps, files, and websites
- **Device security**: Provides hardware-based protections that help secure the system

---

### Windows Defender Firewall

Windows Defender Firewall is a built-in firewall designed to help protect your computer from unauthorized network traffic. It monitors network connections and applies rules that determine whether the connections are allowed or denied. The firewall operates on different network profiles, allowing you to create custom rules or specify applications that are permitted.
- **Domain**: Used when a system is connected to an organization’s domain network
- **Private**: Intended for trusted networks, such as a home or lab environment 
- **Public**: Used for untrusted networks, such as public Wi-Fi

<img width="1048" height="424" alt="image" src="https://github.com/user-attachments/assets/5cecc218-5eb4-463d-a41c-39cf239b6b71" />


Checking out the Advanced settings of Windows Defender Firewall, you can view
- An overview of your firewall's inbound, outbound, and connection rules
- A detailed view of each rule, including name, group, network profile, status, and action
- Create new rules or filter your current view

<img width="520" height="185" alt="image" src="https://github.com/user-attachments/assets/14590098-361e-48f5-9f84-645c97a948b4" />

---

### Answer the questions below

1. Use the `TryHatMeWelcome` installer located within the `TryHatMe Onboarding` folder. What is the flag value you receive after installing and running the application?

<img width="1603" height="889" alt="image" src="https://github.com/user-attachments/assets/c5a26e1d-d2bd-48be-a4ad-e88ff09615b7" />

2. Investigate the Time & Language section of the Windows Settings app. Which country or region is your computer currently set to?

United States

<img width="1268" height="824" alt="image" src="https://github.com/user-attachments/assets/71dbc5f8-ac26-43c8-9740-a02ea8003dda" />

3. Open the Task Manager on your workstation's Desktop and navigate to the Users tab. Which account is currently logged in?

Administrator

<img width="736" height="282" alt="image" src="https://github.com/user-attachments/assets/484d6db8-5a66-4a6d-b933-1642e08b6d73" />

4. After performing your custom scan, click `Virus:DOS/EICAR_Test_File` and select See details. What is the file name shown in the Affected items section?

`tryhatmemaldoc.txt`

<img width="1388" height="826" alt="image" src="https://github.com/user-attachments/assets/b4ad83af-8c72-47b6-acf4-abbc4aff9cee" />

## Conclusion

### Key Terminology

Let’s recap the core terminology and applications you’ve learned about in this room. These definitions will help solidify your understanding before moving on to further learning.
- **Desktop**: The main workspace where files, folders, and shortcuts live
- **Taskbar**: A control strip that provides access to applications, tools, settings, and notifications
- **Start Menu**: The primary way to access applications, settings, and power options, signified by the Windows logo
- **Search**: A quick access method of locating applications, settings, and files by entering search terms
- **File Explorer**: The built-in Windows tool to browse, manage, and organize files and folders
- **Windows Update**: A built-in update tool that helps keep your OS, native apps, and security features up to date
- **Microsoft Store**: The native Windows application for installing trusted applications
- **Windows Settings**: A centralized location for configuring system, device, personalization, and security settings
- **Control Panel**: The legacy management interface that provides access to system configuration options
- **Task Manager**: A Windows tool for monitoring what is happening on your system in real time
- **Windows Security**: The central dashboard for managing Windows built-in security tools
- **Windows Defender Firewall**: The firewall designed to help protect your system from unauthorized network traffic



