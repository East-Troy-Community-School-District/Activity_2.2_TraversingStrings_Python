'''
Print Letters
Pawelski
3/26/2023
Python II

Instructions:
Let's start by stepping through the program to see how
it works.

Let's modify the program a bit. Let's change the while
loop into a for loop that uses the range() function.
Again, let's step through the program to see how it works.
Is there any functional difference between the programs?
Which version is easier to read?

Let's try a few things. First, put in the actual starting
number for the range() function. What number should it start
at? Why? Next, let's add 1 to len(user_text). What happens?
Why? What does this tell you about the last index of a string?

Did you know it is possible to print the letters in reverse
order? Modify the program so that it prints the letters in
reverse order.

Finally, let's modify the program again so that the for
loop does not use the range() function. This version of
a traversal loop is often called a for-each loop. Why?
'''

user_text = input("Enter some text >> ")
i = 0
while i < len(user_text):
    print(user_text[i])
    i += 1