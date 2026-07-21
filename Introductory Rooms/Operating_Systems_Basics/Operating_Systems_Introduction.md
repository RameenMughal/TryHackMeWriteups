# Operating Systems: Introduction

Room: [Operating Systems: Introduction](https://tryhackme.com/room/operatingsystemsintroduction)

<img width="1880" height="395" alt="image" src="https://github.com/user-attachments/assets/c15f1a50-072e-4c1a-9875-6a728caa11dc" />

## The Invisible Manager

An operating system (OS) is the core software that coordinates everything happening on a computer. It sits between the user, applications, and the system’s physical hardware, acting as the invisible manager that keeps the entire machine running as one unified system.

<img width="358" height="255" alt="image" src="https://github.com/user-attachments/assets/bc26da0a-42be-498c-887c-8de619fd2bf8" />


A helpful analogy is to think of your computer as a busy airport, with all its components functioning together.
- **Your hardware (CPU, RAM, storage, connected devices)**: The runways, airplanes, fuel systems, radar, and other physical infrastructure.
- **Your applications (web browser, game launcher)**: The various airlines and their passengers, all trying to take off, land, and request services.
- **Your operating system (Windows, Linux, macOS)**: The entire air traffic control system, directing all of this activity. It schedules resources, manages traffic, resolves conflicts, and ensures safety.

We need an operating system because it provides this all-important job of coordination and structuring that makes modern computing possible. Without an OS, each application would need direct control over the CPU, memory, files, devices, and security. This would quickly cause conflicts, and the OS handles this by acting as the central organizer.

---

### System Privilege Layers

Inside a modern computer, different parts of the system operate at various permission levels. Some components can communicate directly with the hardware, while regular applications run in a safer, restricted environment. This separation is intentional and helps prevent conflicts and security issues.
- **Kernel space**: The privileged, locked-down core of the OS. This is where the kernel, the part of the operating system that directly manages hardware and system resources, runs. It has unrestricted access to the CPU, memory, storage, and all hardware components.
- **User space**: Where all standard applications run. Applications in the user space are deliberately prevented from accessing hardware directly. Whenever they need to open or save a file, play a sound, or connect to Wi-Fi, they must make a system call and request that the kernel act on their behalf.

---

### Operating System Duties

Now that you know what an operating system is and how system privilege is separated, let’s look at what it actually does behind the scenes. Every OS is responsible for a few core duties that allow your computer to run safely, efficiently, and predictably.

<img width="1800" height="767" alt="image" src="https://github.com/user-attachments/assets/2d17344f-850c-4ab8-9666-5dac725d1a91" />

---

### Operating System Security

It is important to understand that every OS also acts as a security foundation. Before any antivirus, firewall, or security tool is introduced, the OS is already enforcing protections in the background, some of which we covered above.

At a basic level, your operating system handles
- **Authentication**: Verifies who you are through login passwords and biometrics
- **Permissions**: Controls exactly what each user and app is allowed to read, write, or execute
- **Isolation**: Keeps every process in its own protected box (kernel/user space separation)
- **System Protection**: Safeguards critical system files and settings from unauthorized changes

---

### Getting Hands-on

<img width="1919" height="882" alt="image" src="https://github.com/user-attachments/assets/4e6357d6-7a08-4cd6-921f-fd1e25218021" />


### Answer the questions below

1. Which OS space has unrestricted access to your computer's hardware?

Kernel Space

2. Which OS responsibility manages user accounts, authentication, and permissions?

User Management

3. After opening the `About This Computer` shortcut, you are greeted with an overview of the system's specifications. What version of Ubuntu Mate is your computer running?

1.26.2

<img width="1081" height="690" alt="image" src="https://github.com/user-attachments/assets/95cb5eff-ad3d-4c52-8732-2964302b1c18" />

4. Check out the `Hardware` section of the System tab. How much memory is allocated to your machine?

1.9 GiB

## OS Interaction and Landscape

### OS Interfaces

Let's look at how we interact with the OS. Interaction with the OS can be divided into two main parts: the graphical user interface (GUI) and the command-line interface (CLI).

#### Graphical User Interface

The GUI is what you're most likely used to interacting with. It provides a graphical representation of all the information you want to access on your computer. Think of folder icons, windows for your applications, and menus for settings.

#### Command-line Interface

The CLI is where you enter specific text-based commands to retrieve or manipulate information. Instead of clicking on icons, you tell the computer exactly what you want using words and syntax that the system understands. This gives you far more precision, control, and speed, especially for advanced tasks, but it requires familiarity with the commands. 

In the screenshot below, you can see that the GUI and CLI are both used to retrieve the same information. In this case, to display the contents of the ubuntu user's `home` directory. The GUI requires a few clicks for folder navigation, whereas the CLI requires a command to list the directory contents.

<img width="1816" height="485" alt="image" src="https://github.com/user-attachments/assets/dfc33d5d-d0ac-4019-8102-1494e60e566d" />

---

### The Operating System Landscape

<img width="1806" height="599" alt="image" src="https://github.com/user-attachments/assets/7b64665d-c40b-46ad-973c-76ac4bc2f1b1" />

---

### Real World Operating Systems

To keep things organized, we’ll highlight the common versions or distributions you’ll see in each and follow the same categories as above: Desktop, Server, Mobile, Embedded, and Virtual/Cloud.

#### Desktop

- **Windows**: The most widely used operating system on personal computers
  - Windows 10 (end-of-life), Windows 11
- **macOS**: Apple's desktop OS, known for its polished GUI and integration with other Apple devices
  - Sonoma (14), Sequoia (15), Tahoe (26)
- **Linux**: Not a single OS but a family of open-source operating systems called distributions
  - Ubuntu, Debian, Fedora

#### Server

- **Windows**: Used in large networks, data centers, and corporate environments
  - Server 2016, 2019, 2022, 2025
- **Linux**: The vast majority of web servers, trusted for its reliability and open-source nature
  - Ubuntu Server, Debian, CentOS, Red Hat
- **Unix**: Large enterprises, finance, telecom, government
  - IBM AIX, Oracle Solaris

#### Mobile

- **Android**: The most widely used mobile OS, which runs on phones, tablets, and smart devices
  - Android 14 - 16, Manufacturer versions
- **iOS**: Apple's mobile OS running on iPhones, iPads, and other devices
  - iOS 17, 18, 26

#### Embedded and IoT Devices

- **Embedded Linux**: Specialized OS built into devices with dedicated functions
  - OpenWrt, Ubuntu Core, Yocto Project
- **Real-Time OS**: Designed for apps where tasks need guaranteed response times (aircraft controls)
  - FreeRTOS, VxWorks, QNX

#### Virtual and Cloud

- **Cloud/VM**: Massive data centers that host websites, apps, and streaming services
  - Ubuntu LTS, Amazon Linux, Rocky Linux
- **Container-optimized**: Lightweight alternatives to VMs that package just the app and its dependencies
  - Alpine Linux, Bottlerocket AWS, Flatcar Linux

---

### Why So Many Operating Systems?

Different devices and environments require different capabilities from an OS. A laptop must be user-friendly and support multitasking. Servers require stability, security, and must be able to run continuously without interruption. Mobile devices need power efficiency and hardware integration to extend battery life. Embedded systems use lightweight operating systems designed for a specialized purpose.

The companies and communities that develop these operating systems also have their own goals. Some focus on ease of use, performance, security, openness, or customization. Because each environment values different capabilities, no single OS is the perfect fit for every situation. Instead, an ecosystem of operating systems has evolved.

---

### Answer the questions below

1. Open the `File Systems` tab in `System Monitor`. What `Type` is listed for the `/dev/root` device?

`ext4`

<img width="1645" height="269" alt="image" src="https://github.com/user-attachments/assets/83c6c8f4-8990-4efa-b2d3-28048a31d8f4" />

2. After opening the `Home` directory on the Desktop, how many user directories exist?

3

<img width="756" height="219" alt="image" src="https://github.com/user-attachments/assets/58e9ae01-2652-442c-ac55-ef9d5c26efef" />

3. Navigate to Alex's `home` directory and explore the Documents folder. What is the flag value contained in `note.txt`?

<img width="979" height="331" alt="image" src="https://github.com/user-attachments/assets/1ebc4f22-5e15-4cb8-b3dd-5bd314a250bc" />

## Conclusion

### Key Terminology

- **Operating system (OS)**: The core software that manages hardware, applications, and all system resources.
- **Kernel space**: The OS’s highly privileged area with direct hardware access, and the home of the kernel, which directly manages hardware and system resources.
- **User space**: The area where regular applications run with limited permissions for safety and system stability.
- **Graphical user interface (GUI)**: The visual part of the OS, windows, icons, and menus, that lets you interact through clicking and tapping.
- **Command-line interface (CLI)**: A text-based interface where you type commands to control the system with precision and speed.

