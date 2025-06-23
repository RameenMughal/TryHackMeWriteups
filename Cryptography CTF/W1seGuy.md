# W1seGuy

Lets check the source code that is given in Task file.

This challenge involves breaking a simple XOR encryption scheme. The source is about When a client connects, the server encrypts a known flag using a randomly generated 5-character key and sends the result in hexadecimal.

Target IP address at my time is `10.10.194.94`

Now connecting by the netcat command `nc 10.10.194.94 1337`

![image](https://github.com/user-attachments/assets/2b2c6237-d0fa-4fe5-b11b-d8704e8e74c7)

It gives a encrypted hex code of the flag and asks for the encrypted key to get the second flag.

**Note:** The encrypted is different everytime we connect to the server so yours might be different

We have to reverse the XOR code to get the decoded flag and the key to get the second flag that is also the final flag which will we do by the CyberChef website

As we know that our flag will start from "THM{" and end with "}" so in the hex format of "THM{" we can see that it is eight value number so we will take eight values of the given encoded flag and get the partial key.

![image](https://github.com/user-attachments/assets/62eb6cb9-bce8-42b1-a41f-ae3133498c8b)

Now get the eight values of the encoded key and place it in the XOR key so you get the partial key for "THM{".

![image](https://github.com/user-attachments/assets/ecf4ac4d-25c6-4351-92d7-ee9c6fdcc8dd)

Now place the partial key in the XOR key.

![image](https://github.com/user-attachments/assets/02da264e-3629-4691-9c40-e716054c3209)

Place the entire encoded flag in the input field, change the HEX form to UTF8 in the XOR and we will get the output starting from "THM{" so we would need to bruteforce to add one more character in the key so we get the flag ending with "}". Start adding digits, lowercase alphabets and uppercase alphabets.

![image](https://github.com/user-attachments/assets/ea937439-a45a-4a2d-8cf9-c046f3161632)

With adding 7, we get the first flag and the key!

![image](https://github.com/user-attachments/assets/320e8994-151f-4adf-8e0d-949e2626e400)

Now writing the key in the terminal and we get the second flag!

![image](https://github.com/user-attachments/assets/c8b13d9e-94de-451d-b473-b675b04e8689)


