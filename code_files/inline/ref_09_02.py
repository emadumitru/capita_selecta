import re
from collections import Counter

def calculate_word_frequency(text):
    def clean_text(text):
        # Remove punctuation and convert to lowercase
        cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
        return cleaned_text

    def split_text_into_words(cleaned_text):
        # Split the text into words
        words = cleaned_text.split()
        return words

    def count_word_frequency(words):
        # Count the frequency of each word
        word_counts = Counter(words)
        return word_counts

    def print_word_frequency(word_counts):
        # Sort the words by frequency in descending order
        sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

        # Print the word frequency
        for word, count in sorted_words:
            print(f'{word}: {count}')

    # Clean the text
    cleaned_text = clean_text(text)

    # Split the text into words
    words = split_text_into_words(cleaned_text)

    # Count the frequency of each word
    word_counts = count_word_frequency(words)

    # Print word frequency
    print_word_frequency(word_counts)

# Sample text
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor."

# Calculate and print word frequency
calculate_word_frequency(text)