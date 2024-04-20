import re
from collections import Counter

def word_frequency_counter(text):
    # Remove punctuation and convert to lowercase
    cleaned_text = clean_text(text)

    # Split the text into words
    words = split_text(cleaned_text)

    # Count the frequency of each word
    word_counts = count_words(words)

    return word_counts

def clean_text(text):
    # Remove punctuation and convert to lowercase
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    return cleaned_text

def split_text(text):
    # Split the text into words
    words = text.split()
    return words

def count_words(words):
    # Count the frequency of each word
    word_counts = Counter(words)
    return word_counts

def print_word_frequency(word_counts):
    # Sort the words by frequency in descending order
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Print the word frequency
    for word, count in sorted_words:
        print(f'{word}: {count}')

# Sample text
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor."

# Calculate word frequency
word_counts = word_frequency_counter(text)

# Print word frequency
print_word_frequency(word_counts)