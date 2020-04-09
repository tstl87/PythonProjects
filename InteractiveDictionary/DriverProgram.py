# -*- coding: utf-8 -*-
"""
The purpose of this program is to create an interactive dictionary that works
by prompting the user for a string input and then the program searches a .json
data file to for a matching word.
"""
import json
from difflib import get_close_matches

# Function that returns the value of the dictionary 

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

if __name__ == "__main__":

    data = json.load(open("data.json"))
    # Prompt user for input.
    word = input("Enter word: ")
    # Search database for word.
    
    output = translate(word)
    if type(output) == list:
        print(word + ':')
        index = 1
        for item in output:
            print(str(index)+'. '+item)
            index += 1
    else:
        print(output)