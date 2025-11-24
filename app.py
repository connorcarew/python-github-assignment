print("Welcome to my Python program!")
name = input("What is your name? ")
print(f"Hello, {name}! Nice to meet you.")
# Add project folder and initial app.py with welcome message
cats_patted = input("How many cats have you patted today? ")
print(f"You patted {cats_patted} cat{'s' if cats_patted != '1' else ''} today.")
try:
    cats_patted_num = float(cats_patted)
except ValueError:
    print("Couldn't interpret that as a number; using 0.")
    cats_patted_num = 0.0

# Example calculation: project daily pats to a year
cats_per_year = cats_patted_num * 365
print(f"At {cats_patted_num} per day, you'd pat about {cats_per_year:.1f} cats in a year.")