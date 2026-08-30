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



