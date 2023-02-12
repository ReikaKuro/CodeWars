"""
Define a function that takes in two non-negative integers aaa and bbb and returns the last decimal digit of aba^bab. Note that aaa and bbb may be very large!

For example, the last decimal digit of 979^797 is 999, since 97=47829699^7 = 478296997=4782969. The last decimal digit of (2200)2300({2^{200}})^{2^{300}}(2200)2300, which has over 109210^{92}1092 decimal digits, is 666. Also, please take 000^000 to be 111.

You may assume that the input will always be valid.
Examples

last_digit(4, 1)                # returns 4
last_digit(4, 2)                # returns 6
last_digit(9, 7)                # returns 9
last_digit(10, 10 ** 10)        # returns 0
last_digit(2 ** 200, 2 ** 300)  # returns 6
"""

import gmpy2

def last_digit(n1, n2):
    return pow(n1, n2, 10)

# def last_digit(n1, n2):
#     return int(str(gmpy2.powmod(n1, n2, 10))[-1:]) if n1 > 0 else 1


print(last_digit(0, 0))  # returns 1
print(last_digit(1, 0))  # returns 1
print(last_digit(2, 0))  # returns 1
print(last_digit(3, 0))  # returns 1
print(last_digit(4, 0))  # returns 1
print(last_digit(5, 0))  # returns 1
print(last_digit(6, 0))  # returns 1
print(last_digit(7, 0))  # returns 1
print(last_digit(8, 0))  # returns 1
print(last_digit(9, 0))  # returns 1
print(last_digit(4, 1))  # returns 4
print(last_digit(4, 2))  # returns 6
print(last_digit(10, 10 ** 10))  # returns 0
print(last_digit(2 ** 200, 2 ** 300))  # returns 6
print(last_digit(3715290469715693021198967285016729344580685479654510946723,
                 68819615221552997273737174557165657483427362207517952651))  # returns 7
