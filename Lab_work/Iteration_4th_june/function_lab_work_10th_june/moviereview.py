# Movie Review Sentiment Analyzer

reviews = [
    "excellent movie",
    "average story",
    "excellent acting",
    "poor direction",
    "excellent visuals",
    "poor screenplay",
    "good music",
    "excellent climax",
    "average performance",
    "good cinematography"
]

# Function to count sentiments
def count_sentiments(reviews):
    excellent = good = average = poor = 0

    for review in reviews:
        if review.startswith("excellent"):
            excellent += 1
        elif review.startswith("good"):
            good += 1
        elif review.startswith("average"):
            average += 1
        elif review.startswith("poor"):
            poor += 1

    return excellent, good, average, poor


# Function to find the most common word
def most_common_word(reviews):
    word_count = {}

    for review in reviews:
        words = review.split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

    max_count = 0
    common_word = ""

    for word in word_count:
        if word_count[word] > max_count:
            max_count = word_count[word]
            common_word = word

    return common_word


# Function to find the longest review
def longest_review(reviews):
    longest = reviews[0]

    for review in reviews:
        if len(review) > len(longest):
            longest = review

    return longest


# Function to display reviews containing a keyword
def reviews_with_keyword(reviews, keyword):
    print(f"Reviews containing '{keyword}':")
    for review in reviews:
        if keyword.lower() in review.lower():
            print(review)


# Main Program
excellent, good, average, poor = count_sentiments(reviews)

print("Excellent Reviews:", excellent)
print("Good Reviews:", good)
print("Average Reviews:", average)
print("Poor Reviews:", poor)

print("\nMost Common Word:")
print(most_common_word(reviews))

print("\nLongest Review:")
print(longest_review(reviews))

print()
reviews_with_keyword(reviews, "excellent")