'''
Blanks
Pawelski
3/26/2023
Python II

Instructions:
This program uses a technique called building a string.
What do you think that means? How might this code be
useful when writing a hangman program?

When should you traverse a string?
'''

word = input("Enter a word >> ")

blanks = ""
for letter in word:
    blanks += "_ "
print(blanks)