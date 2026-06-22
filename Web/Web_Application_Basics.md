# Web Application Basics

Room: [Web Application Basics](https://tryhackme.com/room/webapplicationbasics)

<img width="929" height="188" alt="image" src="https://github.com/user-attachments/assets/70dfb3af-4f24-4289-8941-aa0b5f87a1ef" />

## Web Application Overview

We will now explore the various components that make up a web application.

### Front End

The Front End is the part of a web application that users see and interact with, built using technologies like HTML, CSS, and JavaScript.

**HTML (Hypertext Markup Language)** is the basic language used to structure web pages. It tells a web browser what content to display and how it should be organized.

**CSS (Cascading Style Sheets)** controls the appearance of a web page, including colors, fonts, and layouts.

**JavaScript (JS)** adds interactivity and decision-making to a web page. While HTML provides the structure, JavaScript allows the page to respond to user actions and perform dynamic tasks.

---

### Back End

The Back End of a web application is things you don’t see within a web browser but are important for the web application to work.

A **Database** is where information can be stored, modified, and retrieved. A web application may want to store and retrieve information about a visitor's preferences on what to show or not; this would be stored in a database.

There are many other Infrastructure components underpinning Web Applications, such as web servers, application servers, storage, various networking devices, and other software that support the web application.

**WAF (Web Application Firewall)** is an optional component for web applications. It helps filter out dangerous requests away from the Web Server and provides an element of protection. 

---

### Answer the questions below

1. Which component on a computer is responsible for hosting and delivering content for web applications?

Web Server

2. Which tool is used to access and interact with web applications?

Web Browser

3. Which component acts as a protective layer, filtering incoming traffic to block malicious attacks, and ensuring the security of the the web application?

Web Application Firewall

## Uniform Resource Locator

A Uniform Resource Locator (URL) is a web address that lets you access all kinds of online content—whether it’s a webpage, a video, a photo, or other media. It guides your browser to the right place on the Internet.

### Anatomy of a URL

<img width="1140" height="270" alt="image" src="https://github.com/user-attachments/assets/aa7e6599-ba0a-455f-9023-44fdc3eb6e9a" />

Here’s a breakdown of the key components:

#### Scheme

The scheme is the protocol used to access the website. The most common are HTTP (HyperText Transfer Protocol) and HTTPS (Hypertext Transfer Protocol Secure). HTTPS is more secure because it encrypts the connection, which is why browsers and cyber security experts recommend it. Websites often enforce HTTPS for added protection.

#### User

Some URLs can include a user’s login details (usually a username) for sites that require authentication. This happens mostly in URLs that need credentials to access certain resources. However, it’s rare nowadays because putting login details in the URL isn’t very safe—it can expose sensitive information, which is a security risk.

#### Host/Domain

The host or domain is the most important part of the URL because it tells you which website you’re accessing. Every domain name has to be unique and is registered through domain registrars. 

From a security standpoint, look for domain names that appear almost like real ones but have small differences (this is called typosquatting). These fake domains are often used in phishing attacks to trick people into giving up sensitive info.

#### Port

The port number helps direct your browser to the right service on the web server. It’s like telling the server which doorway to use for communication. Port numbers range from 1 to 65,535, but the most common are 80 for HTTP and 443 for HTTPS.

#### Path

The path points to the specific file or page on the server that you’re trying to access. It’s like a roadmap that shows the browser where to go. Websites need to secure these paths to make sure only authorised users can access sensitive resources.

#### Query String

The query string is the part of the URL that starts with a question mark (?). It’s often used for things like search terms or form inputs. Since users can modify these query strings, it’s important to handle them securely to prevent attacks like injections, where malicious code could be added.

#### Fragment

The fragment starts with a hash symbol (#) and helps point to a specific section of a webpage—like jumping directly to a particular heading or table. Users can modify this too, so like with query strings, it’s important to check and clean up any data here to avoid issues like injection attacks.

---

### Answer the questions below

1. Which protocol provides encrypted communication to ensure secure data transmission between a web browser and a web server?

HTTPS

2. What term describes the practice of registering domain names that are misspelt variations of popular websites to exploit user errors and potentially engage in fraudulent activities?

Typosquatting

3. What part of a URL is used to pass additional information, such as search terms or form inputs, to the web server?

Query String

## HTTP Messages

HTTP messages are packets of data exchanged between a user (the client) and the web server. These messages are very important for understanding how web applications work because they show how users' requests and the server's responses are communicated.

Imagine an example of an HTTP Request and an HTTP Response, where you can see key parts like the method, URL, headers, and status codes. These are what make the client-server interaction possible.

There are two types of HTTP messages:
- **HTTP Requests**: Sent by the user to trigger actions on the web application.
- **HTTP Responses**: Sent by the server in response to the user’s request.

<img width="1705" height="393" alt="image" src="https://github.com/user-attachments/assets/d1fb2bc0-0e04-4ae8-9497-13e59e949c20" />

Each message follows a specific format that helps both the user and the server communicate smoothly.

#### Start Line

The start line is like the introduction of the message. It tells you what kind of message is being sent—whether it's a request from the user or a response from the server. This line also gives important details about how the message should be handled.

#### Headers

Headers are made up of key-value pairs that provide extra information about the HTTP message. They give instructions to both the client and the server handling the request or response. These headers cover all sorts of things, like security, content types, and more, making sure everything goes smoothly in the communication.

#### Empty Line

The empty line is a little divider that separates the header from the body. It’s essential because it shows where the headers stop and where the actual content of the message begins. Without this empty line, the message might get messed up, and the client or server could misinterpret it, causing errors.

#### Body

The body is where the actual data is stored. In a request, the body might include data the user wants to send to the server (like form data). In a response, it’s where the server puts the content that the user requested (like a webpage or API data).

---

### Answer the questions below

1. Which HTTP message is returned by the web server after processing a client's request?

HTTP Response

2. What follows the headers in an HTTP message?

Empty Line








