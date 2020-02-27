# '''
#  Multiplication table of an input number in a list.
#     Input => 2
#     Output=> [2, 4, 6, ..... 22, 24]

# '''

def table(num):
    return lambda a: a*num

num = int(input("Enter any Number: "))
tab = table(num)


for i in range(1, 13):
    print(num, "x", i, "=", tab(i))