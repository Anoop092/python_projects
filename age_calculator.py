# storing user age. 
birth_year = input("What is yourbirth year?: ")
# Note input function always returns the string.

birth_year = int(birth_year)
current_year = 2024

age = current_year-birth_year

print(f"your age is: {age}")
