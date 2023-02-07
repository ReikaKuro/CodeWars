"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
Examples

"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""


def to_camel_case(text):
    new_text = ''
    camel = False
    for index, character in enumerate(text):
        if not character == '-' and not character == '_':
            if camel:
                new_text += character.upper()
                camel = False
            else:
                new_text += character
        else:
            camel = True

    return new_text


print(to_camel_case('The_stealth_warrior'))
