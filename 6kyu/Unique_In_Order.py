"""
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

"""


def unique_in_order(sequence):
    list = []
    for _, item in enumerate(sequence):
        try:
            if not item == list[len(list) - 1]:
                list.append(item)
        except IndexError:
            list.append(item)
    return list


print(unique_in_order('AAAABBBCCDAABBB'))
