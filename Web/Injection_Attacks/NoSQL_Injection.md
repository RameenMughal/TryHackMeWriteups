# NoSQL Injection

Room: [NoSQL Injection](https://tryhackme.com/room/nosqlinjectiontutorial)

Prerequisites:
1. [Burp Suite: Repeater](https://tryhackme.com/room/burpsuiterepeater)
2. [SQL Injection](https://tryhackme.com/room/sqlinjectionlm)

<img width="942" height="206" alt="image" src="https://github.com/user-attachments/assets/465493a8-3d95-49fb-8497-82161aae7f76" />

## Introduction

In this room, you will learn about NoSQL Injection. While SQL-based databases are a popular choice for data storage of web applications, several database options that are not based on SQL also exist. Database solutions such as MongoDB, a NoSQL database solution, have seen a significant rise in popularity in recent years. 

## What is NoSQL

Before we can learn about NoSQL injection, let's first take a look how NoSQL databases work. In this room, we will focus on MongoDB. Although there are other NoSQL solutions, the principles about injection attacks in MongoDB can be applied to any NoSQL database.

---

### MongoDB

Much like MySQL, MariaDB, or PostgreSQL, MongoDB is another database where you can store data in an ordered way. MongoDB allows you to retrieve subsets of data in a quick and structured form. If you are familiar with relational databases, you can assume MongoDB works similarly to any other database. The major exception is that the information isn't stored on tables but rather in documents.

You can think of these documents as a simple dictionary structure where key-value pairs are stored. In a way, they are very similar to what you would call a record on a traditional relational database, but the information is just stored differently. 

For example, let's say we are creating a web application for the HR department, and we would like to store basic employee information. You would then create a document for each employee containing the data in a format that looks like this:

`{"_id" : ObjectId("5f077332de2cdf808d26cd74"), "username" : "lphillips", "first_name" : "Logan", "last_name" : "Phillips", "age" : "65", "email" : "lphillips@example.com" }`

As you see, documents in MongoDB are stored in an associative array with an arbitrary number of fields.

An associative array is a data structure that stores information as key–value pairs instead of using numbered positions like traditional arrays like `array[0]`.

MongoDB allows you to group multiple documents with a similar function together in higher hierarchy structures called collections for organizational purposes. Collections are the equivalent of tables in relational databases. 

Continuing with our HR example, all the employee's documents would be conveniently grouped in a collection called "people" as shown in the diagram below.

<img width="728" height="314" alt="image" src="https://github.com/user-attachments/assets/8b770c4a-bf06-4258-8f49-6dcfc2b22617" />

Multiple collections are finally grouped in databases, which is the highest hierarchical element in MongoDB. In relational databases, the database concept groups tables together. In MongoDB, it groups related collections.

<img width="658" height="274" alt="image" src="https://github.com/user-attachments/assets/c849d1d0-289b-46cb-b219-b5de0d3825db" />

---

### Querying the Database

As with any database, a special language is used to retrieve information from the database. Just as relational databases use some variant of SQL, non-relational databases such as MongoDB use NoSQL. In general terms, NoSQL refers to any way of querying a database that is not SQL, meaning it may vary depending on the database used.

With MongoDB, queries use a structured associative array that contains groups of criteria to be met to filter the information. These filters offer similar functionality to a `WHERE` clause in SQL and offer operators the ability to build complex queries if needed.

To better understand NoSQL queries, let's start by assuming we have a database with a collection of people containing the following three documents:

<img width="591" height="152" alt="image" src="https://github.com/user-attachments/assets/21ab29a1-d5f8-4881-a7ee-6bb526ae7766" />

If we wanted to build a filter so that only the documents where the last_name is "Sandler" are retrieved, our filter would look like this: `['last_name' => 'Sandler']`

As a result, this query only retrieves the second document.

If we wanted to filter the documents where the gender is male, and the last_name is Phillips, we would have the following filter: `['gender' => 'male', 'last_name' => 'Phillips']`

This would only return the first document.

If we wanted to retrieve all documents where the age is less than 50, we could use the following filter: `['age' => ['$lt'=>'50']]`

This would return the second and third documents. Notice we are using the $lt operator in a nested array. Operators allow for more complex filters by nesting conditions.

A complete reference of possible operators can be found on the following link: [Query Predicates](https://www.mongodb.com/docs/manual/reference/mql/query-predicates/)

---

### Answer the questions below

1. What is a group of documents in MongoDB is known as?

Collection

2. Using the MongoDB Operator Reference, what operator is used to filter data when a field isn't equal to a given value?

`$ne`

3. Following the example of the 3 documents given before, how many documents would be returned by the following filter: `['gender' => ['$ne' => 'female'] , 'age' => ['$gt'=>'65'] ]?`

0

## NoSQL Injection

First, let's start the Lab Machine by pressing the Start Lab Machine button at the top of this task.

You may access the VM using the AttackBox or your VPN connection. I am using my Kali Linux as AttackBox and use OpenVPN to connect to TryHackMe Server.

Command: `sudo openvpn FILENAME`

You can check how to connect through OpenVPN by this room: [OpenVPN](https://tryhackme.com/room/openvpn)

Once the machine is ready, navigate to `http://MACHINE_IP` to start the exercise.

---

### Injection is Injection

While it may seem complex to think about NoSQL Injection, when we boil down injection attacks to their very essence, we can understand the similarities between SQL Injection and NoSQL Injection.

The root cause of an injection attack is that improper concatenation of untrusted user input into a command can allow an attacker to alter the command itself. With SQL injection, the most common approach is to inject a single or double quote, that terminates the current data concatenation and allows the attacker to modify the query. The same approach applies to NoSQL Injection. If untrusted user input is directly added to the query, we have the opportunity to modify the query itself. However, with NoSQL Injection, even if we can't escape the current query, we still have the opportunity to manipulate the query itself. 

Therefore, there are two main types of NoSQL Injection:
- **Syntax Injection** - This is similar to SQL injection, where we have the ability to break out of the query and inject our own payload. The key difference to SQL injection is the syntax used to perform the injection attack.
- **Operator Injection** — Even if we can't break out of the query, we could potentially inject a NoSQL query operator that manipulates the query's behaviour, allowing us to stage attacks such as authentication bypasses.

---

### How to Inject NoSQL

When looking at how NoSQL filters are built, bypassing them to inject any payload might look impossible, as they rely on creating a structured array. Unlike SQL injection, where queries were normally built by simple string concatenation, NoSQL queries require nested associative arrays. From an attacker's point of view, this means that to inject NoSQL, one must be able to inject arrays into the application.


