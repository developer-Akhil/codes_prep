import math

number = 456789


# Method 1

def get_len(num):
    digit = int(math.log10(num)) + 1

    return digit


# Method 2

def get_len1(num):
    count = 0

    while num > 0:
        num = num // 10

        count = count + 1

    return count


# Method 3

def get_len2(num):
    length = len(str(abs(num)))

    return length


print(get_len2(number))
