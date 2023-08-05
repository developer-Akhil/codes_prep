import re

""" match """
# line = "pet:cat i love cats"
#
# match = re.match(r"pet:\w\w\w",line)
#
# print(match)
#
# print(match.group())


# line = "i love cats pet:cat"
#
# var = re.match(r"pet:\w\w\w",line)
#
# print(var)
#
# print(var.group(0))


""" search """

line = "i love cats pet:cat"

var = re.search(r"pet:\w\w\w", line)

print(var)

print(var.group(0))

""" find all """

line = "pet:cat i love cats pet:cow i love cows"

var = re.findall(r"pet:\w\w\w",line)

print(var)