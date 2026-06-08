# Library Book Availability

books = {
    "Python Basics": 5,
    "Data Structures": 0,
    "Machine Learning": 3,
    "Java Programming": 2,
    "DBMS": 0,
    "Operating Systems": 6,
    "Networking": 4,
    "Cloud Computing": 1,
    "Cyber Security": 0,
    "Web Development": 7
}

# Display books that are currently unavailable
print("Unavailable Books:")
for book, copies in books.items():
    if copies == 0:
        print(book)

# Count the number of available books
available_count = 0
for copies in books.values():
    if copies > 0:
        available_count += 1

print("\nNumber of Available Books:", available_count)

# Find the book with the maximum copies
max_book = ""
max_copies = 0

for book, copies in books.items():
    if copies > max_copies:
        max_copies = copies
        max_book = book

print("\nBook with Maximum Copies:", max_book, "-", max_copies)

# Create a list of books having less than 3 copies
less_than_3 = []

for book, copies in books.items():
    if copies < 3:
        less_than_3.append(book)

print("\nBooks Having Less Than 3 Copies:")
print(less_than_3)

# Calculate the total number of books available
total_books = 0

for copies in books.values():
    total_books += copies

print("\nTotal Number of Books Available:", total_books)