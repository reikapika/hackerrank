# Candy Replenishing Robot

# Alice is hosting a party! The party lasts for  minutes, and she puts out a bowl of
# candies at the beginning of the party. During each minute , a person comes to the bowl and removes  candies.

# Alice programs the following algorithm into her robot, Bob, to replenish the candy throughout the party:

# If the party is ending (i.e., it's time ), do not refill the bowl.
# If the bowl contains  candies at the end of minute  and , add  candies to the bowl.
# For example, if , , and , then the candy bowl looks like this throughout the party:

# Note that Bob doesn't replenish the bowl at the party's end, so a total of  candies were added during the party.

# Given , , and the number of candies removed from the bowl during each minute, print the total number of new candies Bob adds to the bowl during the party.

# Input Format

# The first line contains two space-separated integers describing the respective values of  and .
# The second line contains  space-separated integers describing the respective values of .

# Output Format

# Print the total number of new candies Bob adds to the bowl during the party.

# Accepted Solution

#!/bin/python

import sys

n,t = raw_input().strip().split(' ')
n,t = [int(n),int(t)]
c = map(int, raw_input().strip().split(' '))
# your code goes here
def add_candy(x,z):
    refills = 0
    remaining = x
    for i in range(len(z)-1):
        remaining -= c[i]
        if i != len(c):
            if remaining < 5:
                refills += (x - remaining)
                remaining = x
            else:
                continue
    return refills


print add_candy(n,c)
