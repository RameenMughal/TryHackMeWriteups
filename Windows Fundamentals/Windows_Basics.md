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










