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

<img width="1132" height="883" alt="image" src="https://github.com/user-attachments/assets/80ec0119-cbfc-4566-b087-4575c898d701" />


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
