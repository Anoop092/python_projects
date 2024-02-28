# Check weather given number is even or odd

user_input = int(input("Enter the number: "))

# logic here is every Even number when divided by 2 it's reminder is always a zero

if user_input%2 == 0:
    print("It is Even Number")
else:
    print("It is Odd Number")