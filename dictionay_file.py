import json
import difflib

data = json.load(open("data.json"))
# data is a dictionary


def find_word(word1):
    word = word1.lower()

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(difflib.get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead", difflib.get_close_matches(word, data.keys())[0])
        decide = input("If yes press y or n for no : ")
        if decide == "y" or decide == "Y":
            return data[difflib.get_close_matches(word, data.keys())[0]]
        elif decide == "n" or decide == "N":
            return "No such word found"
        else:
            return "you have entered the wrong input"
    else:
        return "Word not found"


word = input("Enter the word to be searched: ")
result = find_word(word)

if type(result) == list:
    for i in result:
        print(i)
else:
    print(result)