# Regular Expressions

## Introduction

Regular expressions (or Regex) are patterns of text that you define to search documents and match exactly what you're looking for.

For practicing  there is a helpful website [Regexr](https://regexr.com/)

## Charsets

When searching for a specific string in a file or block of text, you can search for it as is, with `grep ‘string’ <file>`

For patterns of text, use charsets.

A charset is defined by enclosing in square brackets the character(s), or range of characters that you want to match.  Then, it finds every occurrence of the pattern you have defined in the file/text you are searching.

### For Matching Specific Characters

`[abc]` will match `a`, `b` and `c` in every string.

`[abc]zz` will match `azz`, `bzz` and `czz` or use `[a-c]zz` that is same as `[abc]zz`.

`[a-cx-z]zz` will match `azz`, `bzz`, `czz`, `xzz`, `yzz`, `zzz`

`[a-zA-Z]` will match any single character (lowercase and uppercase)

`file[1-3]` will match `file1`, `file2` and `file3`

The charset `[abc]` does not match only string, it will match `abc`, `cba` and `ca`.

It doesn't match the string, but rather every occurrence of the specified characters in that string.

### For Excluding Specific Characters

`[^k]ing` will match `ring`, `sing`, `$ing` but not `king`.

`[^a-c]at` will match `hat` and `fat` but not `bat` and `cat`.

### Answer the questions below

1. Match all of the following characters: c, o, g

`[cog]`

2. Match all of the following words: cat, fat, hat

`[cfh]at`

4. Match all of the following words: Cat, cat, Hat, hat

`[CcHh]at`

4. Match all of the following filenames: File1, File2, file3, file4, file5, File7, file9

`[Ff]ile[1-9]`

5. Match all of the filenames of question 4, except "File7" (use the hat symbol)

`[Ff]ile[^7]`

## Wildcards and optional characters

The wildcard that is used to match any single character (except the line break) is the `.` dot. 

`a.c` will match `aac`, `abc`, `a0c` and so on.

`?` sets the character as optional.

`abc?` will match `ab` and `abc` as `c` is optional.

If we want to search `.` in a string then `a\.c` will match only `a.c`

### Answer the questions below

1. Match all of the following words: `Cat`, `fat`, `hat`, `rat`

`.at`

2. Match all of the following words: `Cat`, `cats`

`[Cc]ats?`

3. Match the following domain name: `cat.xyz`

`cat\.xyz`

4. Match all of the following domain names: `cat.xyz`, `cats.xyz`, `hats.xyz`

`[ch]ats?\.xyz`

5. Match every 4-letter string that doesn't end in any letter from n to z

`…[^n-z]`

6. Match `bat`, `bats`, `hat`, `hats`, but not `rat` or `rats` (use the hat symbol)

`[^r]ats?`

## Metacharacters and Repetitions

### For Metacharacters:

`\d` will match any single digit like `9`.

`\D` will match non single digit like `A` or `@`.

`\w` will match alphanumeric characters like `a` or `3` and also underscore `_`. This means that it will match everything in `test_file`.

`\W` will match non alphanumeric characters like `!` or `#`.

`\s` will match whitespace characters (space, tabs or line break).

`\S` will match everthing else except whitespace characters (alphanumeric and symbols)

### For Repetitions:

`{2}` is used to match anything two times a row.

`z{2}` will match `zz`.

`{12}` will match anything 12 times in a row.

`{1, 5}` will match 1 to 5 times in a row.

`{2,}` will match 2 or more times in a row.

`*` will match 0 or more times in a row.

`+` will match 1 or more times in a row.

### Answer the questions below:

1. Match the following word: `catssss`

`cats{4}`

2. Match all of the following words (use the * sign): `Cat`, `cats`, `catsss`

`[Cc]ats*`

3. Match all of the following sentences (use the + sign): `regex go br`, `regex go brrrrrr`

`regex go br+`

4. Match all of the following filenames: `ab0001`, `bb0000`, `abc1000`, `cba0110`, `c0000` (don't use a metacharacter)

`[abc]{1,3}[01]{4}`

5. Match all of the following filenames: `File01`, `File2`, `file12`, `File20`, `File99`

`[Ff]ile\d{1,2}`

6. Match all of the following folder names: `kali tools`, `kali     tools`

`kali\s+tools`

7. Match all of the following filenames: `notes~`, `stuff@`, `gtfob#`, `lmaoo!`

`\w{5}\W`

8. Match the string in quotes (use the * sign and the \s, \S metacharacters): `2f0h@f0j0%!     a)K!F49h!FFOK`

`\S*\s*\S*`

9. Match every 9-character string (with letters, numbers, and symbols) that doesn't end in a "!" sign

`\S{8}[^!]`

10. Match all of these filenames (use the + symbol): `.bash_rc`, `.unnecessarily_long_filename`, and `note1`

`\.?\w+`

## Starts with/ends with, groups, and either/ or

`^` starts with

`$` ends with

If you want to search starting from `abc` then `^abc`.

If you want to search ending with `xyz` then `xyz$`

`^` is also used in charsets but with square brackets.

You can also define groups by enclosing a pattern in (parentheses).

For either/ or pattern, use `|` pipe.

`during the (day | night)` will match `during the day` and `during the night`.

`(no){5}` will match `nonononono`.

### Answer the questions below

1. Match every string that starts with "Password:" followed by any 10 characters excluding "0", irrespective of the position.

`Password:[^0]{10}`

2. Match "username: " in the beginning of a line (note the space!)

`^username:\s`

3. Match every line that doesn't start with a digit (use a metacharacter)

`^\D`

4. Match this string at the end of a line: EOF$

`EOF\$$`

5. Match all lines that start with $, followed by any single digit, followed by $, followed by one or more non-whitespace characters.

`\$\d\$\S+`

6. Match every possible IPv4 IP address (use metacharacters and groups)

`(\d{1,3}\.){3}\d{1,3}`

7. Match all of these emails while also adding the username and the domain name (not the TLD) in separate groups (use\w): `hello@tryhackme.com`, `username@domain.com`, `dummy_email@xyz.com`

`(\w+)@(\w+)\.com`
