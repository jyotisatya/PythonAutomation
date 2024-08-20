x = input('Enter first number: ')
y = input('Enter second number: ')

try:
    x = int(x)
    y = int(y)

    if x > y:
        print(f"Number {x} is greater.")
    elif x < y:
        print(f"Number {y} is greater.")
    else:
        print("Both numbers are equal.")

except ValueError:
    print('Error: One or both inputs are not valid integers.')