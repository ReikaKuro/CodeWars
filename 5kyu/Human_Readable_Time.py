"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
"""


def make_readable(seconds):
    hour = 0 if int(seconds / 3600) == 0 else int(seconds / 3600)
    minute = 0 if int((seconds - (hour * 3600)) / 60) == 0 else int((seconds - (hour * 3600)) / 60)
    seconds = 0 if int(seconds - (hour * 3600) - (minute * 60)) == 0 else int(seconds - (hour * 3600) - (minute * 60))

    return f'{hour:02d}:{minute:02d}:{seconds:02d}'


print(make_readable(60))
