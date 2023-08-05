# def findTotalPower(power): l=[]
#     result=0
#     for i in power:
#
#         for j in range(len(power)-i):
#             l=l.append(j)
#         result=min( l) * sum(l)


def fib(n):
    if n == 1 or n == 0:
        return n

    f1 = fib(n-1)
    f2 = fib(n - 2)

    ffib = f1 + f2

    return ffib


print(fib(3))
