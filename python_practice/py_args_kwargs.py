# def func(*args):
#     for arg in args:
#         print(arg)
#
#   
# func(11, 3, 4, 5, 6, 6)


def func(**args):
    for k, v in args.items():
        print(k, v)

# a={'a':1,'b':2,'c':3}

func(a=1, b=2, c=3, d=4)
