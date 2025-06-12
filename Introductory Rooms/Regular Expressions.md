# Regular Expressions

## Introduction

Regular expressions (or Regex) are patterns of text that you define to search documents and match exactly what you're looking for.

For practicing  there is a helpful website [Regexr](https://regexr.com/)

## Charsets

When searching for a specific string in a file or block of text, you can search for it as is, with grep ‘string’ <file>

For patterns of text, use charsets.

A charset is defined by enclosing in square brackets the character(s), or range of characters that you want to match.  Then, it finds every occurrence of the pattern you have defined in the file/text you are searching.

[abc] will match a, b and c in every string.

[abc]zz will match azz, bzz and czz or use [a-c]zz that is same as [abc]zz.

[a-cx-z]zz will match azz, bzz, czz, xzz, yzz, zzz

[a-zA-Z] will match any single character (lowercase and uppercase)

file[1-3] will match file1, file2 and file3

The charset [abc] does not match only string, it will match abc, cba and ca.

It doesn't match the string, but rather every occurrence of the specified characters in that string.

If to exclude any character:

[^k]ing will match ring, sing, $ing but not king.

[^a-c]at will match hat and fat but not bat and cat.
