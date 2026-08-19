# SQL Injection

Room: [SQL Injection](https://tryhackme.com/room/sqlinjectionlm)

<img width="949" height="210" alt="image" src="https://github.com/user-attachments/assets/ea6ed820-2d87-4269-a2db-8569be40c94f" />

## Brief

SQL (Structured Query Language) Injection, mostly referred to as SQLi, is an attack on a web application database server that causes malicious queries to be executed. When a web application communicates with a database using input from a user that hasn't been properly validated, there runs the potential of an attacker being able to steal, delete or alter private and customer data and also attack the web application authentication methods to private or customer areas. This is why SQLi is one of the oldest web application vulnerabilities, and it can also be the most damaging.

---

### Answer the questions below

What does SQL stand for?

Structured Query Language

## What is Database?

### Answer the questions below

1. What is the acronym for the software that controls a database?

DBMS

2. What is the name of the grid-like structure which holds the data?

Table

## What is SQL?

SQL (Structured Query Language) is a feature-rich language used for querying databases. These SQL queries are better referred to as statements.

### SELECT 

The following query, returns all the columns by using the * selector, and then the "LIMIT 1" clause forces the database to return only one row of data. Changing the query to "LIMIT 1,1" forces the query to skip the first result, and then "LIMIT 2,1" skips the first two results, and so on. You need to remember the first number tells the database how many results you wish to skip, and the second number tells the database how many rows to return.

`select * from users LIMIT 1;`

| **id** | **username** | **password** |
|--------|--------------|--------------|
| 1      | jon          | pass123      |

---

### UNION

The UNION statement combines the results of two or more SELECT statements to retrieve data from either single or multiple tables; the rules to this query are that the UNION statement must retrieve the same number of columns in each SELECT statement, the columns have to be of a similar data type, and the column order has to be the same.

We have one table called customers with the following contents:

| **id** | **name**         | **address**         | **city**    | **postcode** |
|--------|------------------|---------------------|-------------|--------------|
| 1      | Mr John Smith    | 123 Fake Street     | Manchester  | M2 3FJ       |
| 2      | Mrs Jenny Palmer | 99 Green Road       | Birmingham  | B2 4KL       |
| 3      | Miss Sarah Lewis | 15 Fore Street      | London      | NW12 3GH     |

And another called suppliers with the following contents:

| **id** | **company**         | **address**                   | **city**   | **postcode** |
|--------|---------------------|-------------------------------|------------|--------------|
| 1      | Widgets Ltd         | Unit 1a, Newby Estate         | Bristol    | BS19 4RT     |
| 2      | The Tool Company    | 75 Industrial Road            | Norwich    | N22 3DR      |
| 3      | Axe Makers Ltd      | 2b Makers Unit, Market Road   | London     | SE9 1KK      |

Using the following SQL Statement, we can gather the results from the two tables and put them into one result set:

`SELECT name,address,city,postcode from customers UNION SELECT company,address,city,postcode from suppliers;`

| **name**         | **address**                   | **city**    | **postcode** |
|------------------|-------------------------------|-------------|--------------|
| Mr John Smith    | 123 Fake Street               | Manchester  | M2 3FJ       |
| Mrs Jenny Palmer | 99 Green Road                 | Birmingham  | B2 4KL       |
| Miss Sarah Lewis | 15 Fore Street                | London      | NW12 3GH     |
| Widgets Ltd      | Unit 1a, Newby Estate         | Bristol     | BS19 4RT     |
| The Tool Company | 75 Industrial Road            | Norwich     | N22 3DR      |
| Axe Makers Ltd   | 2b Makers Unit, Market Road   | London      | SE9 1KK      |

---

### DELETE

The DELETE statement tells the database we wish to delete one or more rows of data. Apart from missing the columns you wish to return, the format of this query is very similar to the SELECT. You can specify precisely which data to delete using the where clause and the number of rows to be deleted using the LIMIT clause.

---

### Answer the questions below

1. What SQL statement is used to retrieve data?

SELECT

2. What SQL clause can be used to retrieve data from multiple tables?

UNION

3. What SQL statement is used to add data?

INSERT



