# Create a program that determines whether a given year is a leap year. A leap year is divisible by 4,
# but not by 100 unless it is also divisible by 400. Use an if-else statement to make this determination.

a = int(input('Enter the year'))
result1 = a % 4
result2= a % 400
result3= a % 100
if(result1 == 0 and result3 !=0) or result2==0 :
    print("leap")
else:
    print('not leap')

