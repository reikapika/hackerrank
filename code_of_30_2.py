# Find the Minimum Number

# Jessica is learning to code and was recently introduced to the  function. This function compares two integers and returns the smaller one. This is what calling the function looks like when comparing two integers  and :

# min(a, b)
# Jessica realizes that she can also find the smallest of three integers , , and  if she puts the  function inside of another  function:

# min(a, min(b, c))
# For four integers she can nest the functions once more:

# min(a, min(b, min(c, d)))
# Jessica is curious about the structure of these function calls and wants to see if she can write a program to construct a string that shows how  number of integers can be compared with nested  functions. Can you help Jessica write this program?

# Input Format

# The input contains a single integer  (the number of integers to be compared).

# Output Format

# Print the string on a single line. Each integer in the string should be written as 'int' and the string must accurately show how  functions can be called to find the smallest of  integers.

# Sample Input -0
# 2
# Sample Output -0
# min(int, int)

# Sample Input -1
# 4
# Sample Output -1

# min(int, min(int, min(int, int)))

# Accepted Solution

##!/bin/python
import sys

n = int(raw_input().strip())

def recur_min(n):
    if n <= 2:
        return 'min(int, int)'
    sub = 'min(int, int)'
    output = ''
    for i in range(1, n - 1):
        output = 'min(int, {})'.format(sub)
        sub = output
    return output

print recur_min(n)
