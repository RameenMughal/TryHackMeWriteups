# Burp Suite: Repeater

Room: [Burp Suite: Repeater](https://tryhackme.com/room/burpsuiterepeater)

Prerequisite Room: [SQL Injection](https://tryhackme.com/room/sqlinjectionlm)

<img width="939" height="206" alt="image" src="https://github.com/user-attachments/assets/bc920537-e2ca-41d7-a9a2-c75285238fd8" />

## Introduction

Deploy the target VM attached to this task by pressing the green Start Lab Machine button. Also, start the AttackBox by pressing the blue Start AttackBox button at the top of this room if you are not using your own machine. 

I am using my Kali Linux Machine as an Attack Box and connecting to TryHackMe through OpenVPN.

OpenVPN command: `sudo openvpn <FILENAME>`

## What is Repeater?

In essence, Burp Suite Repeater enables us to modify and resend intercepted requests to a target of our choosing. It allows us to take requests captured in the Burp Proxy and manipulate them, sending them repeatedly as needed. Alternatively, we can manually create requests from scratch, similar to using a command-line tool like cURL.

The ability to edit and resend requests multiple times makes Repeater invaluable for manual exploration and testing of endpoints. It provides a user-friendly graphical interface for crafting request payloads and offers various views of the response, including a rendering engine for a graphical representation.

The Repeater interface consists of six main sections, as depicted in the annotated diagram below:

<img width="1283" height="829" alt="image" src="https://github.com/user-attachments/assets/6f5e377b-185b-47d6-8502-28620fd378c8" />

1. **Request List**: Located at the top left of the tab, it displays the list of Repeater requests. Multiple requests can be managed simultaneously, and each new request sent to Repeater will appear here.
2. **Request Controls**: Positioned directly beneath the request list, these controls allow us to send a request, cancel a hanging request, and navigate through the request history.
3. **Request and Response View**: Occupying the majority of the interface, this section displays the Request and Response views. We can edit the request in the Request view and then forward it, while the corresponding response will be shown in the Response view.
4. **Layout Options**: Located at the top-right of the Request/Response view, these options enable us to customize the layout of the Request and Response views. The default setting is a side-by-side (horizontal) layout, but we can also choose a vertical layout or combine them in separate tabs.
5. **Inspector**: Positioned on the right-hand side, the Inspector allows us to analyze and modify requests in a more intuitive manner than using the raw editor. We will explore this feature in a later task.
6. **Target**: Situated above the Inspector, the Target field specifies the IP address or domain to which the requests are sent. When requests are sent to Repeater from other Burp Suite components, this field is automatically populated.

---

### Answer the questions below

Which sections gives us a more intuitive control over our requests?

Inspector

## Basic Usage

While manual request crafting is an option, it is more common to capture a request using the Proxy module and subsequently transmit it to Repeater for further editing and resending.

Once a request has been captured in the Proxy module, we can send it to Repeater by either right-clicking on the request and selecting Send to Repeater, or by utilizing the keyboard shortcut `Ctrl + R`.

Shifting our focus back to Repeater, we can observe that our captured request is now accessible in the Request view:

Should we wish to modify any aspect of the request, we can simply type within the Request view and press Send once again. This action will update the Response view on the right accordingly. 

Furthermore, we can utilize the history buttons situated to the right of the Send button to navigate through our modification history, allowing us to move forward or backwards as needed.

---

### Answer the questions below

Which view will populate when sending a request from the Proxy module to Repeater?

Request

## Message Analysis Toolbar

Repeater provides us with various request and response presentation options, ranging from hexadecimal output to a fully rendered page.

To explore these options, we can refer to the section located above the response box, where the following four view buttons are available:

<img width="256" height="68" alt="image" src="https://github.com/user-attachments/assets/b1998bf5-1b3c-49b6-836c-3fd635a639e3" />

We are presented with the following display choices:
1. **Pretty**: This is the default option, which takes the raw response and applies slight formatting enhancements to improve readability.
2. **Raw**: This option displays the unmodified response directly received from the server without any additional formatting.
3. **Hex**: By selecting this view, we can examine the response in a byte-level representation, which is particularly useful when dealing with binary files.
4. **Render**: The render option allows us to visualize the page as it would appear in a web browser. While not commonly utilised in Repeater, as our focus is usually on the source code, it still offers a valuable feature.

Adjacent to the view buttons, on the right-hand side, we find the Show non-printable characters button (`\n`). This functionality enables the display of characters that may not be visible with the Pretty or Raw options. 

For example, each line in the response typically ends with the characters `\r\n`, representing a carriage return followed by a new line. These characters play an important role in the interpretation of HTTP headers.

---

### Answer the questions below

Which option allows us to visualize the page as it would appear in a web browser?

Render

## Inspector

Inspector is a supplementary feature to the Request and Response views in the Repeater module. It is also used to obtain a visually organized breakdown of requests and responses, as well as for experimenting to see how changes made using the higher-level Inspector affect the equivalent raw versions.

Inspector can be utilized both in the Proxy and Repeater module. In both instances, it is situated on the far-right side of the window, presenting a list of components within the request and response:

<img width="504" height="518" alt="image" src="https://github.com/user-attachments/assets/bbcb1092-550d-4a68-8cc6-15cfc8178319" />

Among these components, the sections pertaining to the request can typically be modified, enabling the addition, editing, and removal of items. 

For instance, in the Request Attributes section, we can alter elements related to the location, method, and protocol of the request. This includes modifying the desired resource to retrieve, changing the HTTP method from `GET` to another variant, or switching the protocol from `HTTP/1` to `HTTP/2`:

<img width="276" height="155" alt="image" src="https://github.com/user-attachments/assets/f937f759-fdf6-4ba1-9f36-9c742b07bf61" />

Other sections available for viewing and/or editing include:
- **Request Query Parameters**: These refer to data sent to the server via the URL. For example, in a `GET` request like `https://admin.tryhackme.com/?redirect=false`, the query parameter redirect has a value of "false".
- **Request Body Parameters**: Similar to query parameters, but specific to `POST` requests. Any data sent as part of a `POST` request will be displayed in this section, allowing us to modify the parameters before resending.
- **Request Cookies**: This section contains a modifiable list of cookies sent with each request.
- **Request Headers**: It enables us to view, access, and modify (including adding or removing) any headers sent with our requests. Editing these headers can be valuable when examining how a web server responds to unexpected headers.
- **Response Headers**: This section displays the headers returned by the server in response to our request. It cannot be modified, as we have no control over the headers returned by the server. Note that this section becomes visible only after sending a request and receiving a response.

While the textual representation of these components can be found within the Request and Response views, Inspector's tabular format provides a convenient way to visualise and interact with them. Experimenting with header additions, removals, and edits in Inspector helps grasp how the corresponding raw version changes in response.

---

### Answer the questions below

Which section in Inspector is specific to POST requests?

Body Parameters

## Practical Example

Repeater is particularly well-suited for tasks requiring repetitive sending of similar requests, typically with minor modifications. This is particularly useful for activities such as manual testing for SQL Injection vulnerabilities, attempting to bypass web application firewall filters, or adjusting parameters in a form submission.

Let's begin with an exceedingly simple example: Utilizing Repeater to modify the headers of a request sent to a target.

Capture a request to `http://<MACHINE_IP>/` in the Proxy module and send it to Repeater.

<img width="653" height="286" alt="image" src="https://github.com/user-attachments/assets/86793346-d87c-4cbb-99c8-3d1cbd5cc597" />

Take the request from the Proxy section:

<img width="539" height="227" alt="image" src="https://github.com/user-attachments/assets/6c138ac3-6303-4ab6-ace8-b58bd5b134e3" />

Send the request to Repeater:

<img width="797" height="203" alt="image" src="https://github.com/user-attachments/assets/9b57a69f-645d-43bb-bb8f-c5cbb30551ef" />

Send the request once from Repeater, you should see the HTML source code for the page you requested in the Response view.

<img width="628" height="328" alt="image" src="https://github.com/user-attachments/assets/56413bb8-18a6-48a2-9495-c146b2e02c37" />

Try viewing this in one of the other display options (e.g. Hex).

<img width="630" height="359" alt="image" src="https://github.com/user-attachments/assets/b076a333-5c49-4633-a764-cb58cf232727" />

Using Inspector (or manually, if you prefer), add a header called `FlagAuthorised` and set it to have a value of True, as shown below:

<img width="150" height="199" alt="image" src="https://github.com/user-attachments/assets/47d989d5-f4c8-4c13-b4ac-1ea09d598b22" />

<img width="787" height="236" alt="image" src="https://github.com/user-attachments/assets/37e1f1a7-3944-463e-9a38-8776ed4b8061" />

And then send this request.

---

### Answer the questions below

What is the flag you receive?

<img width="961" height="292" alt="image" src="https://github.com/user-attachments/assets/690faaea-4fdf-4aad-b0a7-d67636a92ac4" />

## Challenge

To begin, make sure intercept is disabled in your Proxy module and navigate to `http://<MACHINE_IP>/products/`. Next, try clicking on some of the `See More` links.

<img width="647" height="348" alt="image" src="https://github.com/user-attachments/assets/cce04617-309f-4f6d-8a83-49de71b58132" />

Observe that you are redirected to a numeric endpoint (e.g., `/products/3` or `/products/1`).

<img width="851" height="320" alt="image" src="https://github.com/user-attachments/assets/aae40d42-cde1-4aae-8a3a-457050be448a" />

The objective is to validate the endpoint, confirming the existence of the number you wish to navigate to and ensuring it is a valid integer. However, consider what might occur if this endpoint is not adequately validated.

---

### Answer the questions below

1. Enable intercept again and capture a request to one of the numeric products endpoints in the Proxy module, then forward it to Repeater.

Getting the request of Product No 3 in Proxy section and sending to Repeater.

<img width="626" height="206" alt="image" src="https://github.com/user-attachments/assets/82a26011-bbb3-450e-84b5-c803c08b7800" />

See if you can get the server to error out with a "500 Internal Server Error" code by changing the number at the end of the request to extreme inputs.

2. What is the flag you receive when you cause a 500 error in the endpoint?

I tried to change number 3 from alphabets a or A, or number 0, then I tried -1 number, and got the 500 error.

<img width="1257" height="388" alt="image" src="https://github.com/user-attachments/assets/0b564bb8-c0f9-4f91-bc51-4b5c0d7cec54" />

## Extra-mile Challenge

### Challenge Objective

Your objective in this challenge is to identify and exploit a Union SQL Injection vulnerability present in the ID parameter of the `/about/ID` endpoint. By leveraging this vulnerability, your task is to launch an attack to retrieve the notes about the CEO stored in the database.

---

### Walkthrough

The About page:

<img width="653" height="353" alt="image" src="https://github.com/user-attachments/assets/b5c94ab1-18e0-4a78-a177-a211a34636d4" />

And specific person about page:

<img width="652" height="350" alt="image" src="https://github.com/user-attachments/assets/d5c1da4f-3b4b-466e-93bf-e69349a34717" />

Let's start by capturing a request to `http://<MACHINE_IP>/about/2` in the Burp Proxy. Once you have captured the request, send it to Repeater with`Ctrl + R` or by right-clicking and choosing "Send to Repeater".

Now that we have our request primed, let's confirm that a vulnerability exists. Adding a single apostrophe (`'`) is usually enough to cause the server to error when a simple SQLi is present, so, either using Inspector or by editing the request path manually, add an apostrophe after the "2" at the end of the path and send the request:

<img width="618" height="271" alt="image" src="https://github.com/user-attachments/assets/f2ac9526-593b-46af-8891-f0b8a62a4c59" />

You should see that the server responds with a "500 Internal Server Error", indicating that we successfully broke the query

If we look through the body of the server's response, we see something very interesting at around line 40. The server is telling us the query we tried to execute:

<img width="629" height="203" alt="image" src="https://github.com/user-attachments/assets/bcd48591-20de-469d-97d2-f963534229e7" />

This is an extremely useful error message that the server should absolutely not be sending us, but the fact that we have it makes our job significantly more straightforward.

The message tells us a couple of things that will be invaluable when exploiting this vulnerability:
- The database table we are selecting from is called `people`.
- The query selects five columns from the table: `firstName`, `lastName`, `pfpLink`, `role`, and `bio`. We can guess where these fit into the page, which will be helpful for when we choose where to place our requests.

With this information, we can skip over the query column number and table name enumeration steps.

Although we have managed to cut out a lot of the enumeration required here, we still need to find the name of our target column.

As we know the table name and the number of rows, we can use a union query to select the column names for the `people` table from the `columns` table in the `information_schema` default database.

A simple query for this is as follows:

`/about/0 UNION ALL SELECT column_name,null,null,null,null FROM information_schema.columns WHERE table_name="people"`

This creates a union query and selects our target, then four `null` columns (to avoid the query erroring out). Notice that we also changed the ID that we are selecting from `2` to `0`. By setting the ID to an invalid number, we ensure that we don't retrieve anything with the original (legitimate) query; this means that the first row returned from the database will be our desired response from the injected query.

ooking through the returned response, we can see that the first column name (`id`) has been inserted into the page title:

<img width="527" height="166" alt="image" src="https://github.com/user-attachments/assets/e456774f-0ba3-49a1-b7b8-f6dfd9a56e9e" />

We have successfully pulled the first column name out of the database, but we now have a problem. The page is only displaying the first matching item, we need to see all of the matching items.

Fortunately, we can use our SQLi to group the results. We can still only retrieve one result at a time, but by using the `group_concat()` function, we can combine all of the column names into a single output:

`/about/0 UNION ALL SELECT group_concat(column_name),null,null,null,null FROM information_schema.columns WHERE table_name="people"`

This process is shown below:

<img width="631" height="180" alt="image" src="https://github.com/user-attachments/assets/9ed3a76f-2c4c-415f-b06c-805224f3e95d" />

We have successfully identified eight columns in this table: `id`, `firstName`, `lastName`, `pfpLink`, `role`, `shortRole`, `bio`, and `notes`.

Considering our task, it seems a safe bet that our target column is `notes`.

Finally, we are ready to take the flag from this database — we have all of the information that we need:
- The name of the table: `people`.
- The name of the target column: `notes`.
- The ID of the CEO is `1`.

Let's craft a query to extract this flag:

`/about/0 UNION ALL SELECT notes,null,null,null,null FROM people WHERE id = 1`

---

### Answer the questions below

Exploit the union SQL injection vulnerability in the site.

What is the flag?

<img width="1261" height="378" alt="image" src="https://github.com/user-attachments/assets/dd9c8112-e196-4501-b1ef-867089f3679b" />




























