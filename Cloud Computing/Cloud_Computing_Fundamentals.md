# Cloud Computing Fundamentals

Room: [Cloud Computing Fundamentals](https://tryhackme.com/room/cloudcomputingfundamentals)

<img width="1863" height="382" alt="image" src="https://github.com/user-attachments/assets/7eb544c0-f0c0-4d35-8336-d8815a0dd8f5" />

## Introduction

Imagine you have a fantastic idea for an app that helps students practice cyber security, and you host it on your own computer in your country. But what can you do when users from other parts of the world try to access it and experience lag? What if many students connect at the same time, or your computer is turned off? These limits make it hard for the app to grow.

That's when cloud computing comes to play and solves these problems!

The cloud is built on top of technologies you already learned, like virtualization and containers. These enable running many applications efficiently on shared infrastructure and quickly creating or changing environments when needed.

In this room, we will explore the basics of cloud computing and how this impacts the way modern applications are built, deployed, and used every day.

## Cloud Computing Overview

Cloud computing is the perfect solution for the challenges in the application you’ve designed, such as moving your files from a single laptop to online storage that you can access anywhere. Instead of running your app on one computer in one country, the cloud lets you use computing resources over the internet. This makes your application easier to access, more reliable, and ready to grow as more students start using it.

### How Servers Evolved to Cloud

It’s helpful to understand that cloud computing did not appear suddenly. It is the result of many years of changes in how servers were used and managed. At each step, businesses looked for ways to reduce costs, use resources more efficiently, and make their applications easier to run and scale. 

The timeline below shows this evolution, from physical servers to the cloud we use today:

<img width="1080" height="1080" alt="image" src="https://github.com/user-attachments/assets/2c2ff21b-4fd2-4757-ac22-82d311993d07" />

---

### Cloud Benefits and Characteristics

The cloud was designed to address common problems, including limited capacity, high costs, and slow growth.

The following benefits and characteristics explain how cloud computing makes applications easier to run, scale, and manage:
- **Scalability**: Easily scale up or down as your application's needs change.
- **On-demand self-service**: Create or remove servers and storage instantly, without waiting for hardware.
- **Pay only for what you use**: You are charged based on usage, not upfront costs.
- **Security**: Cloud providers protect the infrastructure with strong security measures.
- **High availability**: Applications keep running even if part of the system fails.
- **Global access**: Your application can be accessed by users anywhere in the world.

In simple terms, the cloud enables IT resources to be flexible, cost-effective, and easier to manage.

---

### Types of Cloud

The flexibility provided by cloud computing allows applications to be run in different ways, depending on your needs and level of control. Because of this, cloud providers offer multiple models for deploying and using applications, each suited to different scenarios.

Let’s start with the deployment types you can choose for a cloud environment:
- **Public Cloud**: Used by startups, websites, and global apps because it is affordable, easy to scale, and requires no infrastructure management. Public cloud services are preferable for nearly every use case.
- **Private Cloud**: Used by banks, healthcare, and government organizations because it offers greater control, customization, and compliance for sensitive data.
- **Hybrid Cloud**: Used by companies like e-commerce platforms that need to keep sensitive data private while still scaling publicly during high demand.

Just like there are different ways to deploy a cloud environment, there are also different ways to use cloud services. Depending on your experience and needs, you can choose the level of responsibility that fits your application.

Let’s look at the main cloud service models:
- **Infrastructure as a Service (IaaS)**: You rent basic computing resources such as virtual servers, storage, and networking. You are responsible for managing the operating system and your application, while the provider manages the physical hardware.
- **Platform as a Service (PaaS)**: The cloud provider manages the infrastructure and the operating system. You focus on building, deploying, and running your application without worrying about servers.
- **Software as a Service (SaaS)**: You use a complete application over the internet. The provider manages everything, and you access the software through a browser or app, for example, Gmail or Zoom.

---

### Major Cloud Vendors

There are several cloud vendors offering a variety of services, but Amazon Web Services (AWS) is the industry leader, with the most extensive offerings and global reach. 

Other well-known cloud providers include:
- **Microsoft Azure**: A strong competitor, especially in enterprise and hybrid cloud environments.
- **Google Cloud Platform (GCP)**: Known for powerful data analytics, AI, and machine learning tools.
- **Alibaba Cloud**: A major player in Asia, offering competitive cloud services globally.
- **IBM Cloud**: Focuses on hybrid cloud and AI-driven solutions for businesses.
- **Oracle Cloud**: Focuses on enterprise applications and databases.

Each of these vendors offers a range of services, but AWS remains the most popular due to its vast infrastructure and support for businesses of all sizes.

---

### How Companies Are Using the Cloud

- Netflix runs its entire platform on AWS so it can scale globally, stay online during peak demand, and stream content reliably to millions of users at once.
- Spotify uses the cloud to handle millions of songs and users, scaling quickly when new music or features are released.
- Instagram relies on the cloud to store massive amounts of photos and videos and deliver them fast to users around the world.
- Online stores use the cloud to handle traffic spikes during black friday without buying permanent infrastructure.

These companies use the cloud because it lets them scale easily, reduce costs, stay reliable, and focus on improving their products instead of managing hardware.

---

### Answer the questions below

1. What is the characteristic of cloud environments that enables you to handle an unexpected increase in access to your application?

Scalability

2. What is the most common type of cloud deployment used?

Public Cloud

3. Suppose you want to deploy an application to the internet, focusing only on application development and leaving infrastructure to others. What type of cloud service is the best?

PaaS

## Deploying a Cloud Instance

In this exercise, you’ll use a cloud interface similar to the AWS platform. The goal is not to memorize buttons, but to understand how cloud resources are easily created and managed in a real-world scenario.

<img width="954" height="876" alt="image" src="https://github.com/user-attachments/assets/7b187093-f9d1-446e-a7ce-961a46b4086c" />


### Basic Cloud Terminology

To complete this exercise, you only need to understand a few basic concepts from AWS:
- **EC2 (Virtual Computer / Server)**: EC2 represents a virtual computer in the cloud. Just like a real computer, it has a CPU and memory (RAM) and can run applications. Whenever you add an EC2 instance, you are adding a computer to your environment.
- **Instance Type (for example: t2, t3, m5)**: Instance types describe how powerful the virtual computer is. Some have more CPU and RAM and are therefore more expensive. You choose the Instance Type based on your needs, knowing that:
  - Bigger instances = more power + higher cost
  - Minor instances = less power + lower cost

---

### Deploying Your Environment

You will create three virtual computers (EC2 instances) to host your cyber security training application. This aligns with the Infrastructure as a Service (IaaS) model you previously learned, as cyber security practices often require full access to the operating system. This allows you to install tools, configure the system, and safely simulate attacks and defenses, just like in real-world environments!

---

### Answer the questions below

1. What is the total cost of credits of the entire environment if `study-machine-1` and `study-machine-2 ` are stopped?

30

<img width="739" height="544" alt="image" src="https://github.com/user-attachments/assets/9f58b96e-0034-4606-afaf-37cb75be390f" />

2. How many credits does an `m5.large` EC2 instance cost per month?

70

<img width="675" height="149" alt="image" src="https://github.com/user-attachments/assets/3374bb18-3f0c-4b6c-a3e7-c6c5f4729236" />

3. What is the total cost of credits if only the new instances we created are running?

150

<img width="746" height="592" alt="image" src="https://github.com/user-attachments/assets/4936a8f2-2885-4819-bd1e-df9230da82b6" />

<img width="747" height="548" alt="image" src="https://github.com/user-attachments/assets/4d447213-06f7-4276-8293-36f53327729d" />

4. What would be the total running cost of the entire environment you created if you add a third `t3a.small` study machine?

188, by creating new Virtual Machine named as `study-machine-3`

<img width="749" height="661" alt="image" src="https://github.com/user-attachments/assets/21bae5c5-a077-456d-9a47-4a2d3d0072f7" />

<img width="738" height="589" alt="image" src="https://github.com/user-attachments/assets/ca806752-3a46-4b05-9b04-feaf3e1c1f5f" />

## Conclusion

### Key Terminology

Let's quickly review some concepts we learned in this room:
- **Public Cloud**: Cloud services you access over the internet that many people and companies share.
- **Private Cloud**: A cloud built just for one company, so they have more control and security.
- **Hybrid Cloud**: A mix of public and private clouds that can work together and share data.
- **IaaS**: A service where you rent basic computer parts like servers and storage from the cloud.
- **PaaS**: A service that gives you a ready-to-use environment to build and run apps without managing servers.
- **SaaS**: Software you use online without installing anything, like Gmail or Zoom.
- **EC2**: Amazon’s cloud computers that you can quickly create, use, and resize whenever you need them.

We also concluded that the key benefits of cloud computing are:
- Scalability
- On-demand self-service
- Pay only for what you use
- Security
- High availability
- Global access
