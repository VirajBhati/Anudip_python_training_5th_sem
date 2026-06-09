message = "Python is awesome and Python is easy to learn"

# 1. Count total characters
total_characters = len(message)

# 2. Count total words
words = message.split()
total_words = len(words)

# 3. Find longest word
longest_word = words[0]
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

# 4. Find shortest word
shortest_word = words[0]
for word in words:
    if len(word) < len(shortest_word):
        shortest_word = word

# 5. Count occurrences of Python
python_count = words.count("Python")

# 6. List of words having more than 4 characters
long_words = []
for word in words:
    if len(word) > 4:
        long_words.append(word)

# 7. Display words starting with a vowel
vowel_words = []
for word in words:
    if word[0].lower() in "aeiou":
        vowel_words.append(word)

# 8. Count vowels and consonants
vowels = 0
consonants = 0

for ch in message:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

# Display results
print("Message:")
print(message)

print("\nTotal Characters:", total_characters)
print("Total Words:", total_words)

print("\nLongest Word:", longest_word)
print("Shortest Word:", shortest_word)

print("\nOccurrences of Python:", python_count)

print("\nWords Longer Than 4 Characters:")
print(long_words)

print("\nWords Starting With a Vowel:")
print(vowel_words)

print("\nVowels:", vowels)
print("Consonants:", consonants)