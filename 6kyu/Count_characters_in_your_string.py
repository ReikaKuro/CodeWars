"""
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.

"""


def count(string):
    dict = {}
    for character in string:
        if character in dict:
            dict.update({character: dict[character] + 1})
        else:
            dict[character] = 1
    return dict


print(count('rafalgronkowski'))
