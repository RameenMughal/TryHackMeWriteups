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

## What is SQL Injection?

The point wherein a web application using SQL can turn into SQL Injection is when user-provided data gets included in the SQL query.

**What does it look like?**

Take the following scenario where you've come across an online blog, and each blog entry has a unique ID number. The blog entries may be either set to public or private, depending on whether they're ready for public release. The URL for each blog entry may look something like this: `https://website.thm/blog?id=1`

From the URL above, you can see that the blog entry selected comes from the id parameter in the query string. The web application needs to retrieve the article from the database and may use an SQL statement that looks something like the following: `SELECT * from blog where id=1 and private=0 LIMIT 1;`

The SQL statement above is looking in the blog table for an article with the id number of 1 and the private column set to 0, which means it's able to be viewed by the public and limits the results to only one match.

SQL Injection is introduced when user input is introduced into the database query. In this instance, the id parameter from the query string is used directly in the SQL query.

Let's pretend article ID 2 is still locked as private, so it cannot be viewed on the website. We could now instead call the URL: `https://website.thm/blog?id=2;--`

Which would then, in turn, produce the SQL statement: `SELECT * from blog where id=2;-- and private=0 LIMIT 1;`

The semicolon in the URL signifies the end of the SQL statement, and the two dashes cause everything afterwards to be treated as a comment. By doing this, you're just, in fact, running the query: `SELECT * from blog where id=2;--`

Which will return the article with an ID of 2 whether it is set to public or not.

This was just one example of an SQL Injection vulnerability of a type called In-Band SQL Injection; there are three types in total: In-Band, Blind and Out-of-Band.

---

### Answer the questions below

What character signifies the end of an SQL query?

`;`

## In-Band SQLi

### In-Band SQL Injection

In-Band SQL Injection is the easiest type to detect and exploit; In-Band just refers to the same method of communication being used to exploit the vulnerability and also receive the results, for example, discovering an SQL Injection vulnerability on a website page and then being able to extract data from the database to the same page.

---

### Error-Based SQL Injection

This type of SQL Injection is the most useful for easily obtaining information about the database structure, as error messages from the database are printed directly to the browser screen. This can often be used to enumerate a whole database. 

---

### Union-Based SQL Injection

This type of Injection utilises the SQL UNION operator alongside a SELECT statement to return additional results to the page. This method is the most common way of extracting large amounts of data via an SQL Injection vulnerability.

---

### Practical

Level one of the practice lab contains a mock browser and website featuring a blog with different articles, which can be accessed by changing the id number in the query string.

The key to discovering error-based SQL Injection is to break the code's SQL query by trying certain characters until an error message is produced; these are most commonly single apostrophes (') or a quotation mark (").

Try typing an apostrophe (') after the id=1 and press enter. And you'll see this returns an SQL error informing you of an error in your syntax. The fact that you've received this error message confirms the existence of an SQL Injection vulnerability. We can now exploit this vulnerability and use the error messages to learn more about the database structure. 

<img width="1881" height="743" alt="image" src="https://github.com/user-attachments/assets/258f0f92-c32e-444a-8501-d2b011314160" />

The first thing we need to do is return data to the browser without displaying an error message. Firstly, we'll try the UNION operator so we can receive an extra result if we choose it. Try setting the mock browsers id parameter to: `1 UNION SELECT 1`

<img width="1883" height="720" alt="image" src="https://github.com/user-attachments/assets/c66a9247-514a-47ac-8234-3911173bc913" />

This statement should produce an error message informing you that the UNION SELECT statement has a different number of columns than the original SELECT query. So let's try again but add another column: `1 UNION SELECT 1,2`

<img width="1865" height="730" alt="image" src="https://github.com/user-attachments/assets/d9984f9f-7d15-4970-b562-9f92897f7402" />

Same error again, so let's repeat by adding another column: `1 UNION SELECT 1,2,3`

<img width="1874" height="764" alt="image" src="https://github.com/user-attachments/assets/a0485c63-aeda-4a71-9016-129da5365875" />

Success, the error message has gone, and the article is being displayed, but now we want to display our data instead of the article. The article is displayed because it takes the first returned result somewhere in the website's code and shows that. To get around that, we need the first query to produce no results. This can simply be done by changing the article ID from 1 to 0: `0 UNION SELECT 1,2,3`

<img width="1873" height="771" alt="image" src="https://github.com/user-attachments/assets/fc81e322-b9a3-45a6-977a-a6ff1ab19bd5" />

You'll now see the article is just made up of the result from the UNION select, returning the column values 1, 2, and 3. We can start using these returned values to retrieve more useful information. First, we'll get the database name that we have access to: `0 UNION SELECT 1,2,database()`

<img width="1873" height="756" alt="image" src="https://github.com/user-attachments/assets/4c2f1ecd-9857-400b-a37f-44f7c0440f00" />

You'll now see where the number 3 was previously displayed; it now shows the name of the database, which is sqli_one.

Our next query will gather a list of tables that are in this database: `0 UNION SELECT 1,2,group_concat(table_name) FROM information_schema.tables WHERE table_schema = 'sqli_one'`

<img width="1128" height="653" alt="image" src="https://github.com/user-attachments/assets/5dfff380-9248-41db-8132-5759a151de2b" />

There are a couple of new things to learn in this query. Firstly, the method group_concat() gets the specified column (in our case, table_name) from multiple returned rows and puts it into one string separated by commas. The next thing is the information_schema database; every user of the database has access to this, and it contains information about all the databases and tables the user has access to. In this particular query, we're interested in listing all the tables in the sqli_one database, which is article and staff_users. 

As the first level aims to discover Martin's password, the staff_users table is what interests us. We can utilise the information_schema database again to find the structure of this table using the below query: `0 UNION SELECT 1,2,group_concat(column_name) FROM information_schema.columns WHERE table_name = 'staff_users'`

<img width="1064" height="675" alt="image" src="https://github.com/user-attachments/assets/5bba9ec2-a7c6-4263-a4b6-459cfd7fa07d" />

This is similar to the previous SQL query. However, the information we want to retrieve has changed from table_name to column_name, the table we are querying in the information_schema database has changed from tables to columns, and we're searching for any rows where the table_name column has a value of staff_users.

The query results provide three columns for the staff_users table: id, password, and username. We can use the username and password columns for our following query to retrieve the user's information: `0 UNION SELECT 1,2,group_concat(username,':',password SEPARATOR '<br>') FROM staff_users`

<img width="1054" height="716" alt="image" src="https://github.com/user-attachments/assets/2707ccf3-8efe-41ad-8414-25670bc18955" />

Again, we use the group_concat method to return all of the rows into one string and make it easier to read. We've also added ,':', to split the username and password from each other. Instead of being separated by a comma, we've chosen the HTML <br> tag that forces each result to be on a separate line to make for easier reading.

---

### Answer the questions below

What is the flag after completing level 1?

<img width="1129" height="618" alt="image" src="https://github.com/user-attachments/assets/953a6c5f-2216-47b5-b07f-ffe0754362cc" />

## Blind SQLi - Authentication Bypass

### Blind SQLi

Unlike In-Band SQL injection, where we can see the results of our attack directly on the screen, blind SQLi is when we get little to no feedback to confirm whether our injected queries were, in fact, successful or not, this is because the error messages have been disabled, but the injection still works regardless. It might surprise you that all we need is that little bit of feedback to successfully enumerate a whole database.

---

### Authentication Bypass

One of the most straightforward Blind SQL Injection techniques is when bypassing authentication methods such as login forms. In this instance, we aren't that interested in retrieving data from the database; We just want to get past the login. 

Login forms that are connected to a database of users are often developed in such a way that the web application isn't interested in the content of the username and password but more in whether the two make a matching pair in the users table. In basic terms, the web application is asking the database, "Do you have a user with the username bob and the password bob123?" the database replies with either yes or no (true/false) and, depending on that answer, dictates whether the web application lets you proceed or not. 

Taking the above information into account, it's unnecessary to enumerate a valid username/password pair. We just need to create a database query that replies with a yes/true.

---

### Practical

Level Two of the SQL Injection examples shows this exact example. We can see in the box labelled "SQL Query" that the query to the database is the following: `select * from users where username='%username%' and password='%password%' LIMIT 1;`

To make this into a query that always returns as true, we can enter the following into the password field: `' OR 1=1;--`

Which turns the SQL query into the following: `select * from users where username='' and password='' OR 1=1;`

Because 1=1 is a true statement and we've used an OR operator, this will always cause the query to return as true, which satisfies the web applications logic that the database found a valid username/password combination and that access should be allowed.

---

### Answer the questions below

What is the flag after completing level two? (and moving to level 3)

<img width="1878" height="855" alt="image" src="https://github.com/user-attachments/assets/2507a334-0488-4641-a0b5-38c6d56fc095" />

## Blind SQLi - Boolean Based

### Boolean Based

Boolean-based SQL Injection refers to the response we receive from our injection attempts, which could be a true/false, yes/no, on/off, 1/0 or any response that can only have two outcomes. That outcome confirms that our SQL Injection payload was either successful or not. On the first inspection, you may feel like this limited response can't provide much information. Still, with just these two responses, it's possible to enumerate a whole database structure and contents.

---

### Practical

On level three of the SQL Injection Examples Machine, you're presented with a mock browser with the following URL: `https://website.thm/checkuser?username=admin`

<img width="891" height="710" alt="image" src="https://github.com/user-attachments/assets/b9a6f0c8-64e7-441d-bad5-e7482a4f7c29" />

The browser body contains  {"taken":true}. This API endpoint replicates a common feature found on many signup forms, which checks whether a username has already been registered to prompt the user to choose a different username. Because the taken value is set to true, we can assume the username admin is already registered. We can confirm this by changing the username in the mock browser's address bar from admin to admin123, and upon pressing enter, you'll see the value taken has now changed to false.

<img width="840" height="571" alt="image" src="https://github.com/user-attachments/assets/e483d71a-23c4-46e1-a15d-19773c4bfbaf" />

The SQL query that is processed looks like the following: `select * from users where username = '%username%' LIMIT 1;`













