

def faboniac(n):

    if n == 0 or n == 1:
        return 1
    else:
        fab = faboniac(n-1) + faboniac(n-2)

        # fab = faboniac(4) + faboniac(n-2)
    return fab

print(faboniac(5))

#        ll  l  next
# 0, 1 , 1,  2,  3 , 5 , 8


# next = ll + l