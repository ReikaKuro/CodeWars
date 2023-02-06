"""
Task

You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
Examples

[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
"""


def is_odd(number):
    if not number % 2 == 0 or number == 1:
        return True
    return False


def sort_array(source_array):
    new_array = []
    index_array = []
    for index, number in enumerate(source_array):
        if is_odd(number):
            new_array.append(number)
            index_array.append(index)
    new_array.sort()
    index_array.sort()

    for x, y in enumerate(index_array):
        source_array[y] = new_array[x]

    return source_array


print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
print(sort_array([1, 111, 11, 11, 2, 1, 5, 0]))
