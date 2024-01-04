char = input()

if char.islower():
    char = char.upper()
elif char.isupper():
    char = char.lower()

print(char)
