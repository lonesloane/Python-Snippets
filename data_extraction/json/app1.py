import json
from difflib import get_close_matches

data = json.load(open('data.json', 'r'))


def get_definition(word_to_define):
    word_to_define = word_to_define.lower()

    if word_to_define in data.keys():
        return data[word_to_define]
    elif word_to_define.upper() in data.keys():
        return data[word_to_define.upper()]
    elif word_to_define.title() in data.keys():
        return data[word_to_define.title()]

    close_word = get_close_matches(word_to_define, data.keys(), 1, 0.6)

    if len(close_word) > 0:
        close_word = close_word[0]
        answer = input('Did you mean {}? Press "Y" if yes, "N" if no. '.format(close_word))
        if answer.lower() == 'y':
            return data[close_word]
        else:
            return 'Bye...'
    else:
        return 'Sorry, no such word found in the dictionary.'


word = str(input('Enter a word: '))
outputs = get_definition(word)

if type(outputs) == list:
    for item in outputs:
        print(item)
else:
    print(outputs)
