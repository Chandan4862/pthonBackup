menu = '''
1. Length
2. concat
3. Captialize
4. Lower case
5. Upper case
6. Exit
'''
length = lambda x : len(x)
concat = lambda x,y:x+y
capitalize = lambda x: x.capitalize()
upper = lambda x : x.upper()
lower = lambda x: x.lower()

print(menu)
print("Enter Choice")
choice = int(input())

while choice < 6:
    try:
        if choice == 1:
            print("Enter a string")
            a = input()
            print(f"The length of {a} is {length(a)}")
            print(menu)
            print("Enter Choice")
            choice = int(input())
        elif choice == 2:
            print("Enter 2 strings to concat")
            a, b = input(), input()
            print(f"The Concatinated string is {concat(a,b)} ")
            print(menu)
            print("Enter Choice")
            choice = int(input())
        elif choice == 3:
            print("Enter a string")
            a = input()
            print(f"The Captialized string is {capitalize(a)}")
            print(menu)
            print("Enter Choice")
            choice = int(input())
        elif choice == 4:
            print("Enter a string")
            a = input()
            print("The lowercase string is: ",lower(a))
            print(menu)
            print("Enter Choice")
            choice = int(input())
        elif choice == 5:
            print("Enter a string")
            a = input()
            print("The uppercase string is: ",upper(a))
            print(menu)
            print("Enter Choice")
            choice = int(input())
        else:
            break
        
    except:
        print("try again")