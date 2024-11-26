def check(func):
    def inside(a, b):
        if b == 0:
            print("Can't devide by 0")

            return

        func(a, b)

    return inside


@check
def div(a, b):
    c = a//b
    # print(c)
    return c

#
# def div(a, b):
#     return a // b
#
#
# div = check(div)

print(div(10, 0))

# print(div(10, 2))

