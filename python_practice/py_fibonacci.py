def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        yield a

        a, b = b, a + b


a = 7
print(list(fibonacci(a)))

# def fibonacci(n):
#     if n < 0:
#
#         print("In correct input")
#
#     elif n == 0:
#
#         return 0
#
#     elif n == 1:
#
#         return 1
#     else:
#
#         return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(9))
