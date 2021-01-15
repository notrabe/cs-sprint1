"""

#task 1 of 9

def csReverseString(chars):
    chars.reverse()
    print(chars)
    return chars

csReverseString(['l', 'a', 'm', 'b', 'd', 'a'])

"""
#task 4 of 9

"""

def csCheckPalindrome(input_str):
    toLst = list(input_str)
    revLst = toLst[::-1]

    if toLst == revLst:
        print('True')
        return True
    else:
        print('False')
        return False


csCheckPalindrome('racecar')

"""

"""

#task 4 of 9 alt solution

def csCheckPalindrome(input_str):
    if input_str == input_str[::-1]:
        print('true')
        return True
    else:
        print('false')
        return False


csCheckPalindrome('false')

"""

#task 7 of 9

import re

def csRemoveDuplicateWords(input_str):
    emptyLst = []                                                  # init empty list
    print(input_str)
    toLst = re.sub("[^\w]", " ",  input_str).split()               # use regex to turn the input string into a list of words
    print(toLst)
    for i in toLst:                                                # if a word in the list is not in the empty list, append that word to the empty list. This prevents duplicates.
        if i not in emptyLst:
            emptyLst.append(i)
    print(' '.join(emptyLst))
    return ' '.join(emptyLst)
csRemoveDuplicateWords('my dog is my dog is super smart')