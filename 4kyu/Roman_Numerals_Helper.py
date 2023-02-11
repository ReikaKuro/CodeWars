"""
Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").
Examples

RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000

Help
Symbol 	Value
I 	1
IV 	4
V 	5
X 	10
L 	50
C 	100
D 	500
M 	1000
"""


class RomanNumerals:

    @staticmethod
    def to_roman(val):
        # Key = index of digit in number (1935: 1=4, 9=3, 3=2, 5=1
        # Value = list of roman numbers that can be created for that index
        numeric_to_roman = {
            4: [[1, 'M']],
            3: [[10, 'M'], [5, 'D'], [1, 'C']],
            2: [[10, 'C'], [5, 'L'], [1, 'X']],
            1: [[10, 'X'], [5, 'V'], [1, 'I']]
        }
        output = ''

        # Separate each digit and iterate over it
        for digit_index, digit in enumerate(reversed(list(str(val)))):
            digit_to_roman = ''
            # For chosen digit iterate over list of roman numbers.
            for counter, mapped_digit in enumerate(numeric_to_roman[digit_index + 1]):
                while int(digit) > 0:
                    # Catching number that will require to combine two romanian numbers
                    if (int(digit) % mapped_digit[0] == 9 and str(mapped_digit)[1] == '1') or (
                            int(digit) % mapped_digit[0] == 4 and str(mapped_digit)[1] == '5'):
                        digit = int(digit) - int(digit) % mapped_digit[0]
                        digit_to_roman += str(numeric_to_roman[digit_index + 1][len(numeric_to_roman[digit_index + 1]) - 1][1]) + mapped_digit[1]
                    else:
                        if counter == 0 or counter == 2:
                            quotient, remainder = divmod(int(digit), mapped_digit[0])
                            digit = remainder
                            digit_to_roman += (mapped_digit[1] * quotient)
                            break
                        else:
                            quotient, remainder = divmod(int(digit), mapped_digit[0])
                            digit = remainder
                            digit_to_roman += mapped_digit[1] * quotient
                            break
            output = digit_to_roman + output

        return output

    @staticmethod
    def from_roman(roman_num):
        roman_to_numeric = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        output = 0
        for counter, letter in enumerate(roman_num):
            # if it is not a last character
            if not counter + 1 >= len(roman_num):
                # If next character larger than the current one
                if roman_to_numeric[roman_num[counter + 1]] > roman_to_numeric[letter]:
                    output += roman_to_numeric[roman_num[counter + 1]] - roman_to_numeric[letter]
                else:
                    # Check if that's a first character
                    if counter == 0:
                        output += roman_to_numeric[letter]
                    # If not then check if previous character was smaller than the current one
                    elif roman_to_numeric[roman_num[counter - 1]] >= roman_to_numeric[letter]:
                        output += roman_to_numeric[letter]
                continue
            # If last character then check if the previous one was smaller
            if roman_to_numeric[roman_num[counter - 1]] >= roman_to_numeric[letter]:
                output += roman_to_numeric[letter]

        return output


print(RomanNumerals.to_roman(2008))  # should return 'MMVIII'
print(RomanNumerals.from_roman('MCMXXXV'))  # should return 1935
