# Compiled

If you see the file through nano it is a binary file.

Give execution permission to the Compiled file `chmod +x ./Compiled-1688545393558.Compiled`

When we run this file it asks us a password

![image](https://github.com/user-attachments/assets/920d2bd2-6952-4869-b16d-0081d20e4c75)

The string command gives us readable characters but using these also gives Try again.

![image](https://github.com/user-attachments/assets/71655272-c779-49a1-aa41-aa30dfaa9efe)

![image](https://github.com/user-attachments/assets/81c3b5c7-b62f-4872-986a-1002df6a8ac5)

As it is a binary file so we need to obtain a readable source code to understand the program and get the password which will be done by Reverse Engineering.

Ghidra is a powerful, open-source software reverse engineering (SRE). It's used to analyze compiled programs (binaries) when the source code is not available.

Open Ghidra, choose File with new Project

Name your project, I am naming GhidraCompiled

Move the Compiled file into the project and analyze the file

Check the Functions in the left side, click the main function

![image](https://github.com/user-attachments/assets/1a556d20-984c-47a9-b597-c6bf7c314f7d)

You will see the code in C language, by checking the code, we see that any string is accepted with "_init"

![image](https://github.com/user-attachments/assets/60f046d2-e684-4ee0-a01d-b1c953a43aaf)

So when using any string, I am using DoYouEven_init, its accepts!

![image](https://github.com/user-attachments/assets/bca7ab01-c437-4269-bc67-d43c2781b985)
