def get_anagram(str1, str2):
    lst1 = [0] * 26
    lst2 = [0] * 26

    for char in str1:
        lst1[ord(char) - 97] += 1

    for char in str2:
        lst2[ord(char) - 97] += 1

    if lst1 == lst2:

        return True
    else:
        return False

str1 = "abcd"
str2 = "dabc"
print(get_anagram(str1, str2))
