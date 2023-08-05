#T. C. = O(n)
#S. C. = 1(n)



l=[1,None,2,3,None,None,5 ,None]

#l=[1,1,2,3,None,None,5 ,None]

# l=[None,8,None]
#output will be [1,1,2,3,3,3,5 ,5]


for i in range(0,len(l)-1):

    if l[i] and l[i+1]==None:

        l[i+1]=l[i]

print(l)

