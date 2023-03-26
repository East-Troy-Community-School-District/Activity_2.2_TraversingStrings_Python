'''
Replace First Last Letter
Pawelski
3/26/2023
Python II

Instructions:
What happens when you don't put a number after the colon
in a slicing operation? 

Modify the program so that it will also ask the user to
replace the last letter in the word. What happens when
you don't put a number before the colon in a slicing
operation?
'''

word = input("Enter a word >> ")
first_letter = input("What would you like as the new first letter? >> ")
first_letter_replaced = first_letter + word[1:]

print("Original word:", word)
print("Replaced first letter:", first_letter_replaced)