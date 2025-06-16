# Linux Modules

## du

`du` is a command in linux (short for disk usage) which helps you identify what files/directories are consuming how much space. 

The folders in their respective folders are listed here with the size they occupy on the disk. 

The size here is shown in KB. 

Note: The files inside a folder are not shown, only the folders are listed by running `du /<directory>` command.

Example: `du ./Desktop` will give space of this specific folder.

### Important Flags:

•	`-a` : Will list files as well with the folder.

•	`-h` : Will list the file sizes in human readable format(B,MB,KB,GB)

•	`-c` : Using this flag will print the total size at the end. you want to find the size of directory you were enumerating

•	`-d <number>` : Flag to specify the depth-ness of a directory you want to view the results for (eg. `-d 2`)

•	`--time` : To get the results with time stamp of last modified.

Example: `du -a /home/` will list every file in the /home/ directory with their sizes in KB.

If there is a lot of output, you can use the `grep` command.

`du -a /home/ | grep user` will list any file/directory whose name is containing the string "user" in it.

The `du` command can alternate the `ls` listing command by: `du –time -d 1`

If you want to know about the owner of each file, you can use the `stat` command.

## Grep, Egrep and Fgrep

The `grep` filter searches a file for a particular pattern of characters, and displays all lines that contain that pattern. 

The pattern that is searched in the file is referred to as the regular expression.

Syntax: `grep “PATTERN” file.txt`

`grep -E` is same as `egrep`.

`grep -F`  is same as `fgrep`.

### Important Flags

•	`-R`: Does a recursive grep search for the files inside the folders(if found in the specified path for pattern search; else grep won't traverse diretory for searching the pattern you specify)

•	`-h`: If you're grepping recursively in a directory, this flag disables the prefixing of filenames in the results.

•	`-c`: This flag won't list you the pattern only list an integer value, that how many times the pattern was found in the file/folder.

•	`-i`: This is what specifies `grep` to search for the PATTERN while IGNORING the case 

•	`-l`: Will only list the filename instead of pattern found in it.

•	`-n`: It will list the lines with their line number in the file containing the pattern.

•	`-v`: This flag prints all the lines that are NOT containing the pattern.

•	`-E`: Will consider the PATTERN as a regular expression to find the matching strings. 

•	`-e`: It can be used to specify multiple patterns and if any string matches with the pattern(s) it will list it.

`grep -r "hello"` will give output like:

`./file1.txt:hello world`

`./dir/file2.txt:hello again`

`grep -r -h "hello"` will give output like:

`hello world`

`hello again`

The difference between the `-E` and `-e` flags is:

- `-e` flag can be used to specify multiple patterns, with multiple use of `-e` flag(`grep -e PATTERN1 -e PATTERN2 -e PATTERN3 file.txt`).
- `-E` can be used to specify one single pattern(You can't use `-E` multiple times within a single `grep` statement).

Other point that you can use to understand the difference is, `-e` works on the BREs(Basic Regular Expressions) and `-E` works on EREs (Extended Regular Expressions).

•	BREs tend to match a single pattern in a file (Simplest examples can be direct words like "sun", "comic")

•	EREs tend to match 2 or more patterns in a file (To select a no of words like (sun sunyon sandston) the pattern could be `"^s.*n$"`). 

### Answer the questions below:

1. Is there a difference between egrep and fgrep? (Yea/Nay)

`Yea`

2. Which flag do you use to list out all the lines NOT containing the 'PATTERN'?

`-v`

3. What user did you find in that file?

`grep -i "user" grep_1611752025618.txt`

Output:

`uxx6x84XZw5VsQTHzVMN7F6fuxx6x84XZw5VsQTHzVMN7F6fuxx6x84XZw5VsQTHzVMN7F6fuxx6x84XZw5VsQTHzVMN7FuSeR:bobthebuilder6fuxx6x84XZw5VsQTHzVMN7F6fuxx6x84XZw5VsQTHzVMN7F6fuxx6x84XZw5VsQTHzVMN7F6f`

User is bobthebuilder.

4. What is the password of that user?

`grep -i "password" grep_1611752025618.txt`

Output:

`qEqbDkrSFzmhRdDSQNWqaMTXqEqbDkrSFzmhRdDSQNWqaMTthispAsSwOrDistoosensitive:'LinuxIsGawd'XqEqbDkrSFzmhRdDSQNWqaMTXqEqbDkrSFzmhRdDSQNWqaMTXqEqbDkrSFzmhRdDSQNWqaMTXqEqbDkrSFzmhRdDSQNWqaMTXqEqbDkrSFzmhRdDSQNWqaMTX`

Password is LinuxIsGawd

5. Can you find the comment that user just left?

`grep -i "comment" grep_1611752025618.txt`

Output:

`8gmdNXTN4gn2u73SuX5cewcM8gmdNXTN4gn2comment:'fs0ciety'u73SuX5cewcM8gmdNXTN4gn2u73SuX5cewcM8gmdNXTN4gn2u73SuX5cewcM8gmdNXTN4gn2u73SuX5cewcM8gmdNXTN4gn2u73SuX5cewcM8gmdNXTN4gn2u73SuX5cewcM`

Comment is fs0ciety

## Did someone said STROPS?

STROPS – STRing OPerationS

Important string operations tools:

•	`tr`

•	`awk`

•	`sed`

•	`xargs`

•	`sort`

•	`uniq`

## tr

`tr` – translate command

For quick operations on strings.

Syntax: `tr [flags] [source]/[find]/[select] [destination]/[replace]/[change]`

`tr` command works in sets of character.

### Important flags:

•	`-d`: To delete a given set of characters

•	`-t`: To concat source set with destination set(destination set comes first; t stands for truncate)

•	`-s`: To replace the source set with the destination set(s stands for squeeze)

•	`-c`: This is the REVERSE card in this game, for eg. If you specify `-c` with `-d` to delete a set of characters then it will delete the rest of the characters leaving the source set which we specified (c stands for complement; as in doing reverse of something)

If you want to convert every alphabet from lowercase to uppercase: `cat file.txt | tr -s '[:lower:]' '[:upper:]'`

You can always see the description of this command by `tr –help`

If you want to see only digits: `cat creds.txt | tr -d '[a-zA-Z: ]'`

This deleted the alphabets, symbol( : ) and a space.

### Answer the questions below

1. Run `tr --help` command and tell how will you select any digit character in the string?

`:digit:` all digits

4. What sequence is equivalent to [a-zA-Z] set?

`:alpha:` all letters

6. What sequence is equivalent to selecting hexadecimal characters?

`:xdigit:` all hexadecimal digits

## awk

`awk` is a scripting language used for manipulating data and generating reports.

The `awk` command programming language requires no compiling, and allows the user to use variables, numeric functions, string functions, and logical operators.

Syntax: `awk [flags] [select pattern/find(sort)/commands] [input file]`

AWK is abbreviated after it's creators (Aho, Weinberger, and Kernighan).

If the commands you wrote are in a script you can execute the script commands by using the `-f` flag and specifying the name of the script file. (`awk -f script.awk input.txt`)

To simply print the contents of a file: `awk ‘{print}’ file.txt`

To search for a pattern inside a file you enclose the pattern in forward slashes `/pattern/`. For instance, if I want to know who all plays CTF competitions the command should be like: `awk '/ctf/' file.txt`

### Built in Variables in awk

Built-in variables include field variables ($1, $2, $3 .. $n)

These field variables are used to specify a piece of data (data separated by a delimeter defaulting to space). 

If I run `awk '{print $1 $3}' file.txt` it will list me the words that are at 1st and 3rd fields. It will give output without spaces.

We can use comma in the parameters to provide space in the output: `awk '{print $1,$3}' file.txt`

The $0 variable points to the whole line.  

Also, make sure to use single quotes('') to specify patterns, awk treats double quotes("") as a raw string. To use double quotes make sure that you escape the ($) sign(s) with a backslash (\) each, to make it work properly.

Example: `awk "{print \$2}"`

NR: (Number Record) is the variable that keeps count of the rows after each line's execution. You can use NR command to number the lines (`awk '{print NR,$0}' file.txt`).

Note that awk considers rows as records.

FS: (Field Separator) is the variable to set in case you want to define the field for input stream. The field separation (defaut to space) that we talked above and can be altered to whatever you want while specifying the pattern. 

FS can be defined to another character(s) at the `BEGIN{command}`.

`awk ‘BEGIN{FS=”o”} {print $2}’ file.txt`

For example “john youtube ctf 52004” will become “hn y”

If you don't know the BEGIN yet, take it as a pattern that we specify and following is the action on that pattern. Similarly, there is END command, this is also a pattern that we specify, following the action to perform on that pattern, and simply, we use them to define actions like Field Separator, Record Separator etc. that are to be performed at the start and at the end of the script, respectively.

`awk "BEGIN {FS='o'} {print $1,$3} END{print 'Total Rows=',NR}"`

RS: (Record Separator): By default it separate rows with '\n', you can specify something else too.

`awk ‘BEGIN{RS=”o”} {print $0}’ file.txt`

It starts new line when it encounters ‘o’

OFS: (Output Field Separator): It is to specify a delimeter while outputing.

`awk ‘BEGIN{OFS=”:”} {print $0}’ file.txt`

The output will be same as the input because it is starting from the first and not separating it into fields

`awk ‘BEGIN{OFS=”:”} {print $1, $2, $3.$4}’ file.txt`

The output will have delimiters between field 1 and 2 and have 3 and 4 concatenated without spaces.

Example: john youtube ctf 50024 will be john:youtube:ctf50024

If it were to be $0,$0 then the lines would be joining their reflection(non-laterally) with a colon(:).

`awk ‘BEGIN{OFS=”:”} {print $0, $0}’ file.txt`

Example: john youtube ctf 50024 will be john youtube ctf 50024:john youtube ctf 50024

ORS: (Output Record Separator): Used to separate each record by specific manner.

`awk ‘BEGIN{ORS=”\n\n”} {print $0}’ file.txt`

This will separate each record by double newline character

### Important Flags:

•	`-F`: With this flag you can specify FIELD SEPARATOR (FS), and thus don't need to use the BEGIN rule

•	`-v`: Can be used to specify variables(like we did in `BEGIN{OFS=":"}`

•	`-D`: You can debug your .awk scripts specifying this flag(`awk -D script.awk`)

•	`-o`: To specify the output file (if no name is given after the flag, the output is defaulted to `awkprof.out`)

### Answer the questions below

1. Download the above given file awk.txt, and use the awk command to print the following output:

ippsec:34024

john:50024

thecybermentor:25923

liveoverflow:45345

nahamsec:12365

stok:1234

`awk 'BEGIN{OFS=":"} {print $1, $4}' awk.txt`

2. How will you make the output as following (there can be multiple; answer it using the above specified variables in BEGIN pattern):

ippsec, john, thecybermentor, liveoverflow, nahamsec, stok,

`awk 'BEGIN{ORS=", "} {print $1}' awk.txt`

## sed

`sed`(Stream EDitor) is a tool that can perform a number of string operations.

You can easily perform operations with sed command by either piping the input or redirecting(<) the input from a file.

Syntax: `sed [flags] [pattern/script] [input file]`

### Important flags:

•	`-e`: To add a script/command that needs to be executed with the pattern/script(on searching for pattern)

•	`-f`: Specify the file containing string pattern

•	`-E`: Use extended regular expressions

•	`-n`: Suppress the automatic printing or pattern spacing

Syntax of mostly sed command:

`‘[condition(s)(optional)] [command/mode(optional)]/[source/to-be-searched pattern(mandatory)]/[to-be-replaced pattern(depends on command/mode you use)]/[args/flags to operate on the pattern searched(optional)]'`

Example: `sed -e '1,3 s/john/JOHN/g' file.txt`

### Modes/Commands:

•	`s`: Substitute mode (find and replace mode)

•	`y`: Works same as substitution; the only difference is, it works on individual bytes in the string provided(this mode takes no arguments/conditions)

### Arguments Args:

•	`/g`: globally(any pattern change will be affected globally, i.e. throughout the text; generally works with s mode)

•	`/i`: To make the pattern search case-insensitive(can be combined with other flags)

•	`/d`: To delete the pattern found(Deletes the whole line; takes no parameter like conditions/modes/to-be-replaced string)

•	`/p`: prints the matching pattern(a duplicate will occur in output if not suppressed with -n flag.)

•	`/1,/2,/3,../n`: To perform an operation on an nth occurrence in a line(works with s mode)

Explaining the previously taken command, (`sed -e '1,3 s/john/JOHN/g' file.txt`)

•	Starting with the sed keyword itself, initializes the `sed` command.

•	With `-e` flag specifying that following is a script command.(you don't need to specify `-e` if it's a single command; as it will be automatically interpreted by sed as a positional argument)

•	Then comes the pattern. Starting with the first portion is the condition (or range selection to be specific), specifying to take range of lines 1,3 (line index starts from 1) and execute the following code on that range of lines. 

•	Following a space comes the mode, specifying that we need to use a substitution mode(as we are substituting a value) by using s. Then we specify / as a delimiter to differentiate between the parts of code. 

•	After the first slash came the pattern we want to operate the substitution on(you may choose to use regex in this region too). 

•	Following the 2nd slash comes the string we want to replace the pattern with. 

•	Finally, after the last slash was an arg/flag, `/g` specifying to operate this operation globally, wherever the pattern was found.

•	Finally was the filename we want to take input from and apply operation/code that we specified beside it.

`sed -n '3,5p' file.txt`

This suppresses the output by the `-n` flag and shows (print) the output from line 3 to 5.

`sed '3,5d' file.txt`

This shows the output except lines 3 to 5

`sed -n -e '1,2p' -e '4,5p' file.txt`

This is used to view multiple ranges of lines

`sed 's/youtube/YOUTUBE/1' file.txt`

This changes the 1st occurrence of youtube in each line to YOUTUBE

If you have log files to view which have trailing white spaces, and it is hard to read them, then you can fix that using regex. `sed 's/ */ /g' file1.txt`

Making every line to start with a bullet point and enclose the digits in square brackets. `sed 's/\(^\b[[:alpha:] ]*\)\([[:digit:]]*\)/\=\> \1\[\2\]/g' file.txt`

This sed substitution command is trying to: Match lines starting with alphabetic words and spaces, followed by digits, and transform them into a format like => name_part[digit_part]

```bash
s/                    # Start substitution
\(
  ^\b[[:alpha:] ]*    # Group 1: beginning of line (^), word boundary (\b), letters or spaces
\)
\(
  [[:digit:]]*        # Group 2: zero or more digits
\)
/\=\> \1[\2]/         # Replacement: '=> ', then Group 1, then digits inside square brackets
g                     # Global replace (for all matches in line)
```

### Answer the questions below

1. You're working in a team and your team leader sent you a list of files that needs to be created ASAP within current directory so that he can fake the synopsis report (that needs to be submitted within a minute or 2) to the invigilator and change the permissions to read-only to only you(Numberic representation). You can find the files list in the "one" folder.

Use the following flags in ASCII order:

•	Verbose

•	Take argument as "files"

`cat file | xargs -I files sh -c "touch files; chmod 400 files"`

It will create each file and set its permission to read only.

2. our friend trying to run multiple commands in one line, and wanting to create a short version of rockyou.txt, messed up by creating files instead of redirecting the output into "shortrockyou". Now he messed up his home directory by creating a ton of files. He deleted rockyou wordlist in that one liner and can't seem to download it and do all that long process again. He now seeks help from you, to create the wordlist and remove those extra files in his directory. You being a pro in linux, show him how it's done in one liner way.

Use the following flags in ASCII order:

•	Take argument as "word"

•	Verbose

•	Max number of arguments should be 1 in for each file

You can find the files for this task in two folder.

`ls | xargs -I word -n 1 -t sh -c 'echo word >> shortrockyou; rm word'`

It goes through each file, then appends its name to shortrockyou and deletes the original file.

3. Which flag to use to specify max number of arguments in one line.

`-n`

4. How will you escape command line flags to positional arguments?

`--`

## sort and uniq

### uniq Command

Unique command filters the output (from either a file or stdin) to remove any duplicates.

uniq command, ONLY, identifies the duplicate lines, if they are adjacent to each other. So we need a command to sort lines first.

Important Flags:

•	`-c`: To count the occurrences of every line in file or stdin

•	`-d`: Will only print the lines that are repeated, not the one which are unique

•	`-u`: Will only print lines that are already uniq

•	`-i`: Ignores case(Default is case-sensitive)

### sort Command

sort command, as the name suggests sorts the lines alphabetically and numerically, automatically. All you got to do is pipe the stdin into sort command. `cat sort.txt | sort`

Important Flags:

•	`-r`: Sorts in reverse order

•	`-c`: This flag is used to check whether the file is already sorted or not(If not, it will list, where the disorder started)

•	`-u`: To sort and removes duplicate lines(does work same as stdin redirected into uniq)

•	`-o save.txt`: To save into a output file

If you want to remove any duplicate lines, a power combo would be sort the lines and then use uniq on the output. `sort file.txt | uniq`

If you're not getting the correct answer for the following question, this could be because of this $LANG variable (that’s set during installation of your linux OS; when you choose the language to install and keyboard layout). The guided solution would be, change the value of `$LANG` variable to `en_US.UTF-8`. Your terminal will then output the results accurately.

`export LANG='en_US.UTF-8'`

### Answer the questions below

1. Download the file given for this task, find the uniq items after sorting the file. What is the 2271st word in the output.

lollol

`sort test_1611747033664.test | uniq > sortedUnique.test`

`sed -n '2271p' sortedUnique.test`

2. What was the index of term 'michele'

2550

`grep -n -w "michele" sortedUnique.test`

## cURL

cURL(stands for crawl URL; It outputs the data of a URLs webpage in a raw format).

Syntax: `curl https://google.com/`

### Important flags

•	`-#`: Will display a progress meter for you to know how much the download has progressed.(or use --silent flag for a silent crawl)

•	`-o`: Saves the file downloaded with the name given following the flag.

•	`-O`: Saves the file with the name it was saved on the server.

•	`-C -`: This flag can resume your broken download without specifying an offset.

•	`--limit-rate`: Limits the download/upload rate to somewhere near the specified range (Units in 100K,100M,100G)

•	`-u`: Provides user authentication (Format: `-u user:password`)

•	`-T`: Helps in uploading the file to some server(In our case php-reverse-shell)

•	`-x`: If you have to view the page through a PROXY. You can specify the proxy server with this flag. (`-x proxy.server.com -u user:password`(Authentication for proxy server))

•	`-I`: Queries the header and not the webpage.

•	`-A`: You can specify user agent to make request to the server

•	`-L`: Tells curl to follow redirects

•	`-b`: This flag allows you to specify cookies while making a curl request(Cookie should be in the format "NAME1=VALUE1;NAME2=VALUE2")

•	`-d`: This flag can be used to POST data to the server(generally used for posting form data).

•	`-X`: To specify the HTTP method on the URL. (GET,POST,TRACE,OPTIONS)

### Answer the questions below

1. Which flag allows you to limit the download/upload rate of a file?

`--limit-rate`

2. How will you curl the webpage of https://tryhackme.com/ specifying user-agent as 'juzztesting'

`curl -A 'juzztesting' https://tryhackme.com/`

3. Can curl perform upload operations?(Yea/Nah)

Yea

## wget

The `wget` (web get) command is a command-line tool used to download files from the internet. It is non-interactive, which means it can work in the background even if you're not logged in.

Syntax: `wget protocol://url.com/`

wget supports ftp, http and https.

### Important Flags

•	`-b`: To background the downloading process

•	`-c`: To continue to the partially downloaded file (It will look for the partially downloaded file in the directory and starts appending; takes no argument)

•	`-t int`: To specify retries to the URL

•	`-O download.txt`: To specify the output name of downloaded file

•	`-o file`: To overwrite the logs into another file

•	`-a file`: To append the logs into already existing file without deleting previous contents

•	`-i file`: Read the list of URLs from a file.

•	`--user=username`: To give a login username(Use `--ftp-user` and `--http-user` if doesn't work)

•	`--password=password`: To give a login password( Use `--ftp-password` and `--http-password` if doesn't work)

•	`--ask-password`: Ask for a password prompt if a login is necessary.

•	`--limit-rate=10k`: Similarly to curl(supports k and m notation for kB and mB respectively)

•	`-w=<int>`: This is to specify the waiting time before the retrieval from a URL.(Takes time in seconds)

•	`-T=<int>`: Timeout the retrieval after a specified amount of time.(Takes time in seconds)

•	`-N`: Enables timestamping

•	`-U`: To specify the user-agent while downloading the file

### Answer the questions below

1. How will you enable time logging at every new activity that this tool initiates?

`-N`

2. What command will you use to download https://xyz.com/mypackage.zip using wget, appending logs to an existing file named "package-logs.txt"

`wget -a 'package-logs.txt' https://xyz.com/mypackage.zip`

3. Write the command to read URLs from "file.txt" and limit the download speed to 1mbps.

`wget -i file.txt –limit-rate=1m`

## xxd

xxd, which is well known for hexdumps or even the reverse.

It will help you handling hex strings and hex digits.

This command can take input from a file or the input can be passed through piping or redirection.

### Important Flags

•	`-b`: Will give binary representation instead of hexdump

•	`-E`: Change the character encoding in the right hand column from ASCII to EBCDIC(Extended Binary Coded Decimal Interchange Code)

•	`-c int`: Sets the number of bytes to be represented in one row. (i.e. setting the column size in bytes; Default to 16)

•	`-g`: This flag is to set how many bytes/octets should be in a group (in one column) i.e. separated by a whitespace (default to 2 bytes; Set -g0 if no space is needed).

•	`-i`: To output the hexdump in C include format ('0xff' integers)

•	`-l`: Specify the length of output(if the string is bigger than the length specified, hex of the rest of the string will not be printed)

•	`-p`: Converts the string passed into plain hexdump style(continuous string of hex bytes)

•	`-r`: Will revert the hexdump to binary(Interpreted as plain text).

•	`-u`: Use uppercase hex letters(default is lower case)

•	`-s`: seek at offset 

`xxd -s 0x10 xxd.txt` This command skips the first 16 bytes of the file (0x10 in hex), and then starts displaying the rest in a hex + ASCII format.

`xxd -s -16 xxd.txt` It starts at the 16th byte from the end, and displays everything from that point to the end of the file (which might be more than 16 bytes, depending on file length and what follows).

`-s +offset` and `-s offset are different`

### Answer the questions below

1. How will you seek at 10th byte(in hex) in file.txt and display only 50 bytes?

`xxd -s 0xa -l 50 -b file.txt`

2. How to display a n bytes of hexdump in 3 columns with a group of 3 octets per row from file.txt? (Use flags alphabetically)

`xxd -c 9 -g 3 file.txt`

3. Which has more precedence over the other `-c` flag or `-g` flag?

`-c`

4. Download the file and find the value of flag.

flag{wh3sdw0lw1gl9oqasad2fs48as}

`xxd -r -p flag_1611749859927.txt`

## Other Modules

### gpg command

GPG(Gnu Privacy Guard) and PGP(Pretty Good Privacy) are 2 different types of encryption. PGP is based on RSA encryption, whereas GPG(open-source) is a re-write of PGP and by default uses AES encryption.

### tar command

Whether if it is a gzip archive or a bzip archive, encrypting and decrypting can be easily done by this tool.

### id/pwd/uname commands

`id` displays information about the current user and their IDs.

`pwd` displays the full path of current working directory.

`uname` displays information about the system (OS by default)

### ps/kill commands

List processes, and kill processes with PID (Process ID)

### netstat commands

lists any network activity on the current system. Any ports that are open/listening/not-established, connection can be listed using this command.

There is an alternate to netstat command which does the pretty much same as netstat, i.e. `ss` (socket statistics) command(lists port activity in real time).

### less/more commands

Offer an alternate to open and read the file.

`more` is an old command and `less` was built to better the more command. `more` on one hand has limited backward scrolling, whereas as `less` has forward and backward navigation including better search options (/).

There is one more command which was created to improve some of less features, `most` command; 

It is not installed by default on some linux distros, you can install it with `sudo apt install most`.

### diff command

This command compares the character byte-by-byte and tries to find what is the difference between 2 files. Though this can ONLY compare 2 files at a time.

There is also another command known as `comm`. This command compares 2 sorted files line by line. As `diff` tries to find any difference between the files, `comm` is more focused to find out what is common in between 2 files.

### base64 command

Decode base32 and base64 encryption in your own terminal.

### tee command

`tee` command reads from stdin and writes to the stdout and files as well.

You can use it with `-a` flag to don't overwrite an existing file instead just append some more.

### file/stat command

`file` command reads the file headers and tells you what the file actually is(inspite of what extension is used). Example: ASCII text

Similarly is `stat` command, which gives you a file's/file system's status.

### export command

This command is used to set the environment variables(The variables that got set whenever a shell/user session is opened).

### reset command

Say if your terminal is not working properly, any problem is occurring, but you can't afford to close the shell, you're just one `reset` command away to get your shell back to normal.

### systemctl/service command

`service` command is a normal command to initialize services present in /etc/init.d, without making an admin worrying too much about the permanent system changes, `systemctl` on the other hand is a heavy command(doing pretty much the same job, just on systemd's level; systemd is a service manager in linux systems) which can hinder with the default settings.

For eg. services initialized by systemctl stays in systemd's directory (directory which holds what program to run when a linux system boots up). Thus the programs initialized by `systemctl` boots up with system.

With service you can only use commands related to that particular service (reload, start, stop, status etc), and with a powerful tool like `systemctl`, you get to control the state of "systemd" system and service manager.

### Answer the questions below

1. It's safe to run `systemctl` command and experiment on your main linux system neither following a proper guide or having any prior knowledge? (Right/Wrong)

Wrong

2. How will you import a given PGP private key. (Suppose the name of the file is key.gpg)

`gpg –import key.gpg`

3. How will you list all port activity if netstat is not available on a machine? (Full Name)

Socket Statistics

4. What command can be used to fix a broken/irregular/weird acting terminal shell?

`reset`
