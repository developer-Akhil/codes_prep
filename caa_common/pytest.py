
def fun(n):
    if n==0:
        return 0
    print(n)
    n=fun(n-1)


    # if n==1:
    #     return 0
    print(n)
    fun(n + 1)

    return n

fun(5)