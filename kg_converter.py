# pound to kg converter

# user information abou his weight in ponds
user_input = input("What is your weight,in terms of pounds? ")

# type casting of user_input to integer
user_input = int(user_input)

# note 1 pound = 0.45kg 

user_weight = user_input * 0.45

print(f"Your weight in terms of kg is: {user_weight}")
