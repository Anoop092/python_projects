# Based on user choice this program coverts weight from kg to pounds or vice versa

user_input = int(input("Enter the weight: "))
user_choice = input("(L)bs or (K)g,Enter only K or k for kg L or l for pounds : ").lower()

# note 1 pounds = 0.45 kg

weight = 0

if user_choice == "l":
    weight = 0.45 * user_input
    print(f"Your weight is {weight} kg")
elif user_choice == "k":
    weight = round(user_input/0.45,1)
    print(f"Your weight is {weight} pounds")
else:
    print("Invalid SI unit")


