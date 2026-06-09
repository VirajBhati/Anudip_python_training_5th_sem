name = input("Enter Your Name: ")

# 1. Remove spaces
username = name.replace(" ", "")

# 2. Convert to lowercase
username = username.lower()

# 3. Append current year
username = username + "2026"

# Store generated username before truncation
generated_username = username

# 4. If username length exceeds 12, keep only first 12 characters
if len(username) > 12:
    username = username[:12]

# 5 & 6. Count vowels and consonants
vowels = 0
consonants = 0

for ch in generated_username:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

# 7. Display statistics
print("\nOriginal Name:", name)

print("\nGenerated Username:")
print(generated_username)

print("\nUsername Length:", len(generated_username))

print("\nVowels:", vowels)
print("Consonants:", consonants)

print("\nStatus: Username Generated Successfully")