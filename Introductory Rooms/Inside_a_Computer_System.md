# Inside a Computer System

Room: [Inside a Computer System](https://tryhackme.com/room/insideacomputer)

<img width="937" height="197" alt="image" src="https://github.com/user-attachments/assets/0e15ab2e-b6cc-436d-b4c5-17d9eaf4b37d" />

## Introduction

After completing this room, you will have a general idea of how the components of a computer system interact with each other to provide services to its users. 

## Inside a Computer System

Nearly every computer system that you can think of includes, in one way or another, the same building blocks. Each part has its own job, and together they make the computer work. Let's have a look at each of these building blocks.

<img width="839" height="559" alt="image" src="https://github.com/user-attachments/assets/aa1f637b-04b4-49ed-9dd9-3481d4023db4" />

PSU: Power Supply Unit

The image above shows the different PC components and its human counterpart. 

### Motherboard

The motherboard is like our body's skeleton and nervous system. It holds all the different components in place and connects them. On a typical desktop motherboard, you'll see different connectors that house all your components - CPU socket, RAM slots, expansion slots, and various ports. Every other component plugs into or connects through the motherboard. The image below shows a typical desktop motherboard.

#### Motherboard Inspection

<img width="936" height="528" alt="image" src="https://github.com/user-attachments/assets/6b4926e5-0f87-47f5-9682-bd75c697bed3" />

<img width="917" height="184" alt="image" src="https://github.com/user-attachments/assets/b519279e-14ea-463c-a224-2f037f2d2a11" />

<img width="918" height="191" alt="image" src="https://github.com/user-attachments/assets/78430eb9-834c-4b48-a984-e015d72c2933" />

A **DIMM** (Dual In-line Memory Module) is the primary type of RAM module used in desktop computers, consisting of a circuit board with memory chips that plugs into a motherboard slot.

RAM (Random Access Memory) is the volatile, temporary data storage used by a computer while it runs, whereas a RAM module (or memory stick) is the physical circuit board containing memory chips that plugs into the motherboard. Essentially, RAM is the technology/concept, and the module is the physical hardware containing that memory

<img width="921" height="192" alt="image" src="https://github.com/user-attachments/assets/77e7a760-b872-4073-9c00-6c80ff1e3ab9" />

<img width="915" height="184" alt="image" src="https://github.com/user-attachments/assets/78aadf59-0f92-46ff-8e0c-213967e0e76e" />

<img width="922" height="169" alt="image" src="https://github.com/user-attachments/assets/b07bbc1d-5eb1-4d6f-8d3b-6c46c770f249" />

<img width="914" height="188" alt="image" src="https://github.com/user-attachments/assets/4a8b5f97-8f22-461e-9726-cbcf3f56dcb7" />

### CPU

The CPU (Central Processing Unit), often called the processor, is comparable to a part of our brain. Just like our brain continuously executes instructions (add numbers, pour milk in a bowl, and so on), a CPU does the same for a computer. Modern CPUs have multiple cores that handle instructions in parallel. The CPU connects to the motherboard via the CPU socket. The image below shows a typical CPU for a desktop.

### RAM

RAM (Random Access Memory) is comparable to our brain's short-term or working memory. When working on a task, we keep relevant information in mind temporarily. RAM does the same - it holds data that the CPU needs quick access to. RAM is volatile: when power is lost, all contents are gone. Modern RAM modules use technologies like DDR5 or DDR6 for increased speed and performance. 

**DDR5**: 5th generation of Double Data Rate SDRAM, offering significantly higher speeds starting at 4800MT/s

**DDR6**: Next-generation SDRAM standard designed to succeed DDR5, expected to arrive around 2027 with speeds ranging from 8,800 to 17,600 MT/s

**SDRAM**: Synchronous Dynamic Random-Access Memory. It is a type of DRAM that synchronizes itself with the CPU's system clock, allowing it to operate faster and more efficiently than older, asynchronous DRAM by coordinating data transfers.

### Storage (SSD/HDD)

SSDs and HDDs are storage devices, comparable to our long-term memory. Just like fond memories are remembered permanently, data is saved long-term on storage devices. HDDs use older technology with moving parts, limiting performance. SSDs have no moving parts and use memory chips, allowing much faster speeds. HDDs remain popular for their large capacity at low cost. Storage connects via SATA cables or PCI Express slots. The image below shows an HDD on the left-hand side and an SSD on the right-hand side.

<img width="937" height="559" alt="image" src="https://github.com/user-attachments/assets/889024d5-2be2-45c4-a5be-1d4c6574dd98" />

**SSD**: Solid State Drive (SSD) is a high-speed, durable storage device that uses flash memory (NAND) instead of moving magnetic platters

**NAND** flash is a type of non-volatile storage technology used in SSDs to retain data without power

**HDD**: A Hard Disk Drive (HDD) is a non-volatile, electro-mechanical data storage device used in computers for storing operating systems, software, and files.

**SATA**: SATA (Serial Advanced Technology Attachment) cables connect internal storage drives (HDD/SSD) and optical drives to a computer's motherboard.

**PCI Express**: PCI Express (PCIe) slots are high-speed expansion interfaces on a motherboard used to connect components like graphics cards, sound cards, and SSDs.

### Network Adapter

A network adapter lets computers communicate with other systems. Network adapters come in wireless and wired variants. Often they're embedded in the motherboard, but they can also be added as expansion cards. Network cards typically connect via PCI Express ports. The image below shows a plugin network card, typically used in desktops.

<img width="839" height="559" alt="image" src="https://github.com/user-attachments/assets/a9d07933-2be1-4763-b442-4e9dbf4bf96e" />

### Power Supply (PSU)

A PSU supplies energy to all system components. The PSU is essential and requires careful consideration - if components need more power than the PSU can provide, the system will fail. The PSU takes power from an outlet and distributes it via various connectors like the main motherboard connector and Molex connectors.

A **Molex connector** is a standardized, often 4-pin, pin-and-socket interconnect system widely used in computers and electronics to supply power to peripheral devices like hard drives, fans, and lighting

### Graphics Card

The graphics card receives information from the operating system and programs, then outputs processed visual data to a monitor. Graphics cards connect to PCI Express slots on the motherboard.

### Input/Output

Just like we have senses to obtain information for our brains to process and then act on, computers have input and output devices. Input devices include keyboards, microphones, mice, and scanners. Output devices include monitors, printers, and speakers. Common connectors for these peripherals include USB, HDMI, and DisplayPort. 

### Answer the questions below

Give in the flag you received after completing the exercise on the static site.

<img width="300" height="350" alt="image" src="https://github.com/user-attachments/assets/2e8e7187-1a89-42e0-b44d-b17cdc7fe551" />

## What Happens When You Press the Start Button?

Now that the core components are installed in the computer system, it is time to boot up the system.

The image below shows the steps a computer system goes through before it shows you a working interface (in the form of an Operating System).

<img width="761" height="61" alt="image" src="https://github.com/user-attachments/assets/4212900f-7c5c-41b3-8557-90718072b968" />

### Step 1: Press the Power Button

When we press the power button on our computer system, a signal is sent to the PSU to allow power to flow.

### Step 2: Firmware starts

Continuing our analogy from step 1, once the body has started up, our core components are up and running, but our brain is not yet conscious. Like our bodies, a computer system contains firmware that allows all its components to start up. The central system that manages this is called the Unified Extensible Firmware Interface (UEFI). 

**Note**: We will often see the term BIOS mentioned instead of UEFI. BIOS does the same as UEFI, but has mainly been replaced by UEFI

### Step 3: Power-On Self Test

Now that our body is up and running, it is time to test if everything is functioning as it should. If something isn't, there will be some alarm signals. One of the routines that the UEFI loads is the Power-On Self Test, which tests if every required component is present, configured correctly, and functioning.

### Step 4: Select Boot Device

Once our body is up and running, configured correctly and fully functional, our system searches for the location of our bootup routine to start our consciousness. In our computer system the UEFI holds an ordered list which prioritizes on which device to look first for the boot up routine for the Operating System.

### Step 5: Initiate Bootloader

Now that our system knows the part of our brain where our consciousness is located, it initiates the "load routine" to start it. Our computer systems follow a similar process: On the selected boot device, the bootloader is initiated. This bootloader transfers the Operating System from the selected boot device to the Random Access Memory. Once the OS is transferred, the UEFI gives control over the different components to the OS.

### Answer the questions below

What is the flag that you received after completing the exercise?

<img width="300" height="350" alt="image" src="https://github.com/user-attachments/assets/a178a27a-14ab-489c-b4fd-2beacafa87c9" />
