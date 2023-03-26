'''
Count Letter
Pawelski
3/26/2023
Python II

Instructions:
Why was a function used in this program? Could this
function be better? 

Modify the function so that it can search for any letter
by accepting it as a parameter. Why is this a better
version of the function?
'''

def count_a(string):
    '''
    Counts the number of "a"s in the string. Counts
    both upper- and lower-case.
    '''
    count = 0
    for character in string:
        if character.lower() == "a":
            count += 1
    return count

user_text = input("Enter some text >> ")
number_a = count_a(user_text)
print(number_a)