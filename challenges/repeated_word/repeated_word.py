import re

def repeated_word(string):
    '''replaces all punctuations in a string with space and make it lower case'''
    string = re.sub(r'[^\w\s]','',string).lower()
    '''creates a list to hold the words in the string'''
    processed = []
    '''split the string into words & append it to the list. If it is already on the list, return the repeared word'''
    for word in string.split():
        if word in processed:
            return word
        processed.append(word)
    raise ValueError('no repeated word found')
