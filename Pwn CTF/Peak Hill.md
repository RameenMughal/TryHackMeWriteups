# Peak Hill

<img width="953" height="178" alt="image" src="https://github.com/user-attachments/assets/f149f6dd-0177-4d95-a78d-6cda02f9cdeb" />

Doing `nmap` scan to find all the hidden ports also `nmap -p- --min-rate 1000 -T4 MACHINE_IP`

<img width="335" height="110" alt="image" src="https://github.com/user-attachments/assets/2987175b-b6eb-4fbc-ab0f-85226e5520ca" />

There are two known services as FTP and SSH and one unknown or custom service SWX

Doing nmap scan to check the Versions of the services `nmap -sV -sC -p21,22,7321 MACHINE_IP`

<img width="415" height="239" alt="image" src="https://github.com/user-attachments/assets/9837702c-c26c-45ff-9578-5340a389f80a" />

We can check if the FTP Service being able to log in as `Anonymous` with no password. 

`ftp MACHINE_IP`

<img width="191" height="101" alt="image" src="https://github.com/user-attachments/assets/d5fc2472-b520-4215-8ed9-d1e7023fa92d" />

Checking the current files and directories by `ls -a` and see a `.creds` file

<img width="309" height="91" alt="image" src="https://github.com/user-attachments/assets/0714798d-dc2e-4d75-87e4-e9f695aada51" />

Checking the contents of `.creds` by `more .creds` it is a binary file

Downloading the `.creds` file into the local Linux machine to decode this file, `get .creds`

Decoding this file by CyberChef by selecting 






