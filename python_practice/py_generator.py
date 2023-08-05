def count_up_to(n):
    i = 1
    while i <= n:
        yield i

        i += 1


generator = count_up_to(5)

print(next(generator))
print(next(generator))
print(next(generator))
# for number in generator:
#
#     print(number)