# Dynamic_Programming_Number_of_passwords

# Question
It is the year 11984 (yes, 11984), and the world is a dystopian society.
After decades of searching, the resistance has finally found Rick Sanchez’s Portal Gun which
lets them open portals to anywhere in the universe. This will be their key to winning the "war".
Unfortunately, the Portal Gun is password protected, and they need your help to crack the password.
You know that the password is obtained by deleting some digits from the password file which
you obtained from the Portal Gun’s Persistent Random Access Memory (PRAM). The password
file is just a list of decimal digits. Note that the password cannot be empty!
As a first step, you would like to find the total number of possible passwords. Write a program
that computes the number of passwords.
Full credit only for the most efficient solution

# Examples:

>>> num_passwords([1, 2, 1, 3])

Output : 13

The different possible passwords are {1, 2, 3, 12, 11, 13, 21,23, 121, 123, 113, 213, 1213}.

>>> num_passwords([9, 9, 9, 9])

Output : 4

The different possible passwords are {9, 99, 999, 9999}
