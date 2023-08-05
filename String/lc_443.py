def getCompressStr(StrVal: str):
    res = ""
    cnt = 1

    for i in range(1, len(StrVal)):

        if StrVal[i - 1] == StrVal[i]:

            cnt += 1

        else:
            res = res + StrVal[i - 1]

            if cnt > 1:
                res += str(cnt)

            cnt = 1

    res = res + StrVal[-1]

    if cnt > 1:
        res += str(cnt)

    return res


# def getCompressStr(Strval: str):
#     ch = Strval[0]
#
#     result = ""
#     count = 0
#     Strval = Strval+" "
#
#     for x in Strval:
#
#         if ch == x:
#             count += 1
#         else:
#
#             if count > 1:
#                 result = result + str(ch) + str(count)
#             ch = x
#             count = 1
#
#     print(result)
#     print(Strval)
#
#     if len(result) > len(Strval) or result == Strval:
#
#         return Strval
#     else:
#
#         return result


print(getCompressStr("abbbcdddd"))
