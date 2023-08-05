l = ['a', .90, 3, "how", "sjla2"]
# t = ('a',.90,3,"how","sjla2",'a')

t = ()

for item in l:
    t = t + (item,)

print(t)

t += (21,)

print(t)
# x = [i for i in range(5)]
#
# print(x)
# [[0:2],[1:3],[2:4],[3:5],[4:6]]
