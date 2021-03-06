import json
from colorama import Fore, Back, Style
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean {} instead? Enter Y - for yes, N- for no: ".format(get_close_matches(word, data.keys())[0]))
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word does not exist. Please, double check it."
        else:
            return "We didn`t undertand your entry."
    else:
        return "The word does not exist. Please, double check it."

word = input(Fore.GREEN + "Enter word: ")
print(Fore.BLUE + "Meaning:" + Style.RESET_ALL)

output = translate(word)

if type(output) == list:
    for item in output:
        print(Fore.MAGENTA + item + Style.RESET_ALL)
else:
    print(Fore.MAGENTA + output + Style.RESET_ALL)