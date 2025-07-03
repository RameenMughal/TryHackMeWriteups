# Linux Strength Training

## Finding your way around Linux – Overview

As a security researcher you will often be required to find specific files/folders on a system based on various conditions ranging from, but not limited to the following:
- filename
- size
- user/group
- date modified
- date accessed
- Its keyword contents

We can do this using the following syntax:

| Description                            | Syntax                                                       | Example                                                                                                                                                   |
|----------------------------------------|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Find files by filename                 | `find [directory path] -type f -name [filename]`             | `find /home/Andy -type f -name sales.txt`                                                                                                                 |
| Find directories by name               | `find [directory path] -type d -name [filename]`             | `find /home/Andy -type d -name pictures`                                                                                                                  |
| Find files by size                     | `find [directory path] -type f -size [size]`                 | `find /home/Andy -type f -size 10c`                                                                                                                       |
|                                        |                                                              | *(c=bytes, k=KB, M=MB, G=GB)*                                                                                                                             |
| Find files by username                 | `find [directory path] -type f -user [username]`             | `find /etc/server -type f -user john`                                                                                                                     |
| Find files by group name               | `find [directory path] -type f -group [group]`               | `find /etc/server -type f -group teamstar`                                                                                                                |
| Find files modified after a date       | `find [directory path] -type f -newermt '[date and time]'`   | `find / -type f -newermt '6/30/2020 0:00:00'`                                                                                                             |
|                                        |                                                              | All dates/times after 6/30/2020 0:00:00 will be considered a condition to look for                                                                        |
| Find files modified within date range  | `find [dir] -type f -newermt [start] ! -newermt [end]`       | `find / -type f -newermt 2013-09-12 ! -newermt 2013-09-14`                                                                                                |
|                                        |                                                              | All dates before 2013-09-12 will be excluded; all dates after 2013-09-14 will be excluded, therefore this only leaves 2013-09-13 as the date to look for. |
| Find files accessed within date range  | `find [dir] -type f -newerat [start] ! -newerat [end]`       | `find / -type f -newerat 2017-09-12 ! -newerat 2017-09-14`                                                                                                |
|                                        |                                                              | All dates before 2017-09-12 will be excluded; all dates after 2017-09-14 will be excluded, therefore this only leaves 2017-09-13 as the date to look for. |
| Find files with specific keyword       | `grep -iRl [directory path/keyword]`                         | `grep -iRl '/folderA/flag'`                                                                                                                               |

**Notes**: Typing CTRL+L allows you to clear the screen quicker rather than typing 'clear' all the time.

Placing: `2>/dev/null` at the end of your find command can help filter your results to exclude files/directories that you do not have permission to.

### Answer the questions below

1. What is the correct option for finding files based on group.

`-group`

2. What is format for finding a file with the user named Francis and with a size of 52 kilobytes in the directory /home/francis/

`find /home/francis -type f -user Francis -size 52k`

3. . SSH as topson using his password topson. Go to the /home/topson/chatlogs directory and type the following: `grep -iRl 'keyword'`. What is the name of the file that you found using this command?

`ssh topson@10.10.187.108` (Your target machine IP address)

Moving to the chatlogs directory

`grep -iRl 'keyword'`

![image](https://github.com/user-attachments/assets/ae783e0c-8eb9-418d-82bf-d74e72a8dbb2)

**Answer**: 2019-10-11

4. Type: `less [filename]` to open the file. Then, before anything, type / before typing: keyword followed by [ENTER]. Notice how that allowed us to search for the first instance of that word in the entire document. For much larger documents this can be useful and if there are many more instances of that word in the document, we would be able to hit enter again to find the next instance in the document.

`less 2019-10-11`

`/keyword` then Enter

5. What are the characters subsequent to the word you found?

ttitor

6. Read the file named 'ReadMeIfStuck.txt'. What is the Flag?

Checking where the ReadMeIfStuck.txt is 

![image](https://github.com/user-attachments/assets/1faee3e3-f512-4545-bbd1-fedcb9179e63)

Finding the additionalHINT file `find / -type f -name additionalHINT 2>/dev/null`

![image](https://github.com/user-attachments/assets/7347715e-54a1-4f66-820a-fb186cf80daa)

Going to the channels directory and checking the content of additionalHINT

![image](https://github.com/user-attachments/assets/f8d744df-6e4b-4b4f-8b85-718a3c6fefc8)

Finding the telephone numbers directory

![image](https://github.com/user-attachments/assets/8e6af2a0-c601-49a9-8679-c270091edf37)

Going to the telephone numbers directory and checking the content of file

![image](https://github.com/user-attachments/assets/1cfc395a-9644-4462-bb0d-ec2f44debd59)

Finding the file in workflow directory of modified date, first finding the workflow directory

`find / -type d -name workflows 2>>/dev/null`

![image](https://github.com/user-attachments/assets/a6acb1d9-1765-4800-9e79-f3fa5cc9bc85)

Now finding the file modified `find / -type f -newermt 2016-09-11 ! -newermt 2016-09-13 2>/dev/null`

![image](https://github.com/user-attachments/assets/dd4ff8fe-f181-4b7b-afb0-0e001bf53616)

The first file is the one, going to the xft directory and get the content with the less command `less eBQRhHvx`

Search `/Flag`, scroll down and you get the flag 

![image](https://github.com/user-attachments/assets/c9faaaef-989a-41b1-94ef-6525192025f0)
