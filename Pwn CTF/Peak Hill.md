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

Decoding this file by CyberChef by selecting 'From Binary' we get words like ssh and pass

<img width="765" height="413" alt="image" src="https://github.com/user-attachments/assets/3570407d-8584-4b3b-992d-9c3bdaba59b6" />

This type of decoded content hints that the file is a Python pickle serialized object.

Pickle is Python’s built-in way of converting Python objects (like strings, lists, or dictionaries) into a byte stream so they can be stored or transferred, and then reconstructed later. Pickle uses Python-specific opcodes like `N` for `None`, `q` for references, and S'...' for strings, which is why the decoded text shows patterns such as `ssh_pass15q` and `NULL` values. These are strong indicators that the file is a pickle object created using the text-based (protocol 0) serialization format.

So using the `pickle` and `pickletool` library in Python to reverse the code and get the exact information

```
import pickle
import pickletools

with open(".creds", "rb") as f:
    bits = f.read().strip()

# Convert ASCII "0"/"1" to real bytes
data_bytes = int(bits.decode(), 2).to_bytes(len(bits) // 8, byteorder="big")

# (Optional) Disassemble safely first
print("=== Pickle Disassembly ===")
print(pickletools.dis(data_bytes))

# Actually load the object
creds = pickle.loads(data_bytes)
print("\n=== Extracted Credentials ===")
print(creds)
```

<img width="452" height="179" alt="image" src="https://github.com/user-attachments/assets/80d17930-bbd4-4628-9f90-9aaa0a934fa7" />

It’s in an array format and each number represents a character,number or letter and when put together we get a username and password.

Using this information to SSH login in the target machine.

We see a `cmd_service.pyc` which is compiled Python file. We can also see by `nano` command that this file is not readable as it is compiled and contain language that only machine can understand. These type of files are often use to make execution faster so Python does not have to compile the original code file every time.

We can use the `decompyle3` (A native Python cross-version decompiler and fragment decompiler).

Copying the file `cmd_service.pyc` in local Linux machine. `scp gherkin@MACHINE_IP:/home/gherkin/cmd_service.pyc  ~/Downloads/cmd_service.pyc`

De-compiling the `cmd_service.pyc` to get the original code. 








