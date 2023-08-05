import sys


def addition(arry_vals):
    if len(arry_vals) == 0:

        return 0

    else:
        return arry_vals[0] + addition(arry_vals[1:])


x = [1, 2, 3, 4]
print(addition(x))

sys.exit()


def fatorial(n):
    if n == 0 or n == 1:

        return 1

    else:

        return n * fatorial(n - 1)


n = int(input("Enter a value "))

result = fatorial(n)

print(result)
