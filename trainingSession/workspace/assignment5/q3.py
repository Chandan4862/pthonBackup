menu = '''
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Exit
'''

add = lambda x, y : x+y
subtract = lambda x, y : x-y
multiply = lambda x, y : x*y
divide = lambda x, y : x/y
power = lambda x, y : pow(x,y)

print(menu)
print("Enter Choice")
choice = int(input())
while choice < 6:
    try:
        if choice == 1:
            print("Enter 2 numbers")
            a, b = int(input()), int(input())
            print(add(a,b))
            print(menu)
            print("Enter Choice")
            choice = int(input())
        elif choice == 2:
            print("Enter 2 numbers")
            a, b = int(input()), int(input())
            print(subtract(a,b))
            print(menu)
            print("Enter Choice")
            choice = int(input())
        elif choice == 3:
            print("Enter 2 numbers")
            a, b = int(input()), int(input())
            print(multiply(a,b))
            print(menu)
            print("Enter Choice")
            choice = int(input())
        elif choice == 4:
            print("Enter 2 numbers")
            a, b = int(input()), int(input())
            print(divide(a,b))
            print(menu)
            print("Enter Choice")
            choice = int(input())
        elif choice == 5:
            print("Enter 2 numbers")
            a, b = int(input()), int(input())
            print(power(a,b))
            print(menu)
            print("Enter Choice")
            choice = int(input())
        else:
            break
        
    except:
        print("Try again")