# Bash Scripting
## Introduction

Bash is a scripting language that runs within the terminal on most Linux distros, as well as MacOS. Shell scripts are a sequence of bash commands within a file, combined together to achieve more complex tasks than simple one-liner and are especially useful when it comes to automating sysadmin tasks such as backups.

[Bash Scripting Cheatsheet](https://devhints.io/bash)

## Our first simple bash scripts

A bash script always starts with the following line of code at the top of the script. `#!/bin/bash`

The command “echo” is used to output text to the screen, the same way as “print” in python. 

You can also perform normal Linux commands inside your bash script and it will be executed if formatted right.

Now to run our bash script we must first give it executable permissions `chmod +x yourfile.sh`

### Answer the questions below

1. What piece of code can we insert at the start of a line to comment out our code?

`#`

2. What will the following script output to the screen, echo “BishBashBosh”

BinBashBosh

## Variables

`name="Jammy"`

Where we give the value of Jammy and assign it to the variable name.

Please note that for variables to work you cannot leave a space between the variable name, the ”=” and the value. They cannot have spaces in.

We have to add a $ onto front of our variable name in order to use it. `echo $name`

Debugging is a very important part of programming so we should get used to problem solving and fixing errors as early as possible. And bash has a few built in features that make our life simple.
When running at the command line you can do: `bash -x ./file.sh`

If you want to debug at a certain point you can insert `set -x` into your script and `set +x` to end the section like the following:

```
echo "hi"
set -x
# This section of code will be checked for debugging
set +x
```

If there was an error it would output a - on that line this makes it easy to spot where you have gone wrong so you can fix them.

We can also use multiple variables in something like an echo statement

```
name=Jammy
age=21
echo "$name is $age years old"
```

### Answer the questions below

1. What would this code return?

Jammy is 21 years old

2. How would you print out the city to the screen?

`echo $city`

3. How would you print out the country to the screen?

`echo $country`

## Parameters

We will firstly  look at parameters specified using the command line when running the file. These come in many forms but often have the "$" prefix because a parameter is still a variable.

```
name=$1
echo $name
```

We now run our script with `./example.sh Alex`

And sure enough we get returned with “Alex”

So what if we wanted the 2nd argument? Well the process is very simple and we simply add a `$2` instead of `name=$1`

Then run with `./example.sh Alex Tony`

It would return Tony

What if we didn't want to supply them like this however, and instead it would let us type in our name in a more interactive way, we can do this using read.

```
echo Enter your name
read name
echo "Your name is $name"
```

### Answer the questions below

1. How can we get the number of arguments supplied to a script?

`$#`

2. How can we get the filename of our current script(aka our first argument)?

`$0`

3. How can we get the 4th argument supplied to the script?

`$4`

4. If a script asks us for input how can we direct our input into a variable called ‘test’ using “read”

`read test`

5. What will the output of “echo $1 $3” if the script was ran with "./script.sh hello hola aloha"

hello aloha

## Arrays

Arrays are used to store multiple pieces of data in one variable, which can then be extracted by using an index. Most commonly notated as `var[index_position]`.

Arrays use indexing meaning that each item in an array stands for a number.

In the array ['car', 'train', 'bike', 'bus'] each item has a corresponding index.

All indexes start at position 0

The syntax is as follows: `transport=('car' 'train' 'bike' 'bus')`

We can then echo out all the elements in our array like this: `echo "${transport[@]}"`

Where the "@" means all arguments, and the [] wrapped around it specifies its index.

If we wanted to remove an element we would use the unset utility. `unset transport[1]`

Now lets set it to something else. We can do: `transport[1]='trainride'`

### Answer the questions below

1. What would be the command to print audi to the screen using indexing.

`echo "${cars[1]}"`

2. If we wanted to remove tesla from the array how would we do so?

`unset cars[3]`

3. How could we insert a new value called toyota to replace tesla?

`cars[3]='toyota'`

## Conditionals

When we talk about conditionals it means that a certain piece of code relies on a condition being met, this is often determined with relational operators, such as equal to, greater than, and less than.

```
#!/bin/bash
count=10
if [ $count -eq 10 ]
then
        echo "true"
else
        echo "false"
fi
```

If statements always use a pair of brackets and in the case of the [] we need to leave a space on both sides of the text(the bash syntax). We also always need to end the if statement with `fi`

The `-eq` is one way of doing this, you could also use “=”

Description of some operators:
- `-eq`: Checks if the value of two operands are equal or not; if yes, then the condition becomes true.
- `-ne`: Checks if the value of two operands are equal or not; if values are not equal, then the condition becomes true.
- `-gt`: Checks if the value of left operand is greater than the value of right operand; if yes, then the condition becomes true.
- `-lt`: Checks if the value of left operand is less than the value of right operand; if yes, then the condition becomes true.
- `-ge`: Checks if the value of left operand is greater than or equal to the value of right operand; if yes, then the condition becomes true.

We want to make a script that we will perform on a file given by a parameter.

We then check if it exists and if it has write permissions. If it has write perms then we echo “hello” to it. If it is either non-accessible or doesn't exist we will create the file and echo “hello” to it.

```
#!/bin/bash
filename=$1
if [ -f "$filename" ] && [ -w "$filename" ]
then
        echo "hello" > $filename
else
        touch "$filename"
        echo "hello" > $filename
fi
```

### Answer the questions below

1. What is the flag to check if we have read access to a file?

`-r`

2. What is the flag to check to see if it's a directory?

`-d`
