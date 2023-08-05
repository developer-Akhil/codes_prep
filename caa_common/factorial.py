
# Function to find factorial of given number
def factorial(n):
    ##Bascase
    if n == 0:
        return 1
    fact = n * factorial(n - 1)
    print(fact)
    return fact
    #return n * factorial(n - 1)

factorial(5)
# 5* factorial(4)
#
# 5*4 *factorial(3)
# 5*4*3 *factorial(2)
#
# 5*4*3*2 * factorial(1)
# 5*4*3*2*1 *factorial(0)
# 5*4*3*2*1*1=120


# 5= 5*4*3*2*1
#
# 5!= 5

# 0! = 1
# j=1

# for i in range(1,5):
#
#     j = j*i  = 1*1    =1
#
#     j = j*2 = 1*2

