import re
from collections import Counter

def count_words(text):
    # Remove punctuation and convert to lowercase
    cleaned_text = clean_text(text)
    
    # Split the text into words
    words = split_text(cleaned_text)
    
    # Count the frequency of each word
    word_counts = count_frequency(words)
    
    return word_counts

def clean_text(text):
    return re.sub(r'[^\w\s]', '', text.lower())

def split_text(text):
    return text.split()

def count_frequency(words):
    return Counter(words)

def print_word_counts(word_counts):
    for word, count in word_counts.items():
        print(f'{word}: {count}')

def main():
    # Sample text
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed semper nisl. Sed euismod, nunc id aliquam lacinia, nunc nunc tincidunt sem, nec lacinia nisl nunc id nunc."
    
    # Count the words
    word_counts = count_words(text)
    
    # Print the word counts
    print_word_counts(word_counts)

if __name__ == "__main__":
    main()