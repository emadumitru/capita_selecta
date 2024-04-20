import re
from collections import Counter

def count_words(text):
    # Remove punctuation and convert to lowercase
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    
    # Split the text into words
    words = cleaned_text.split()
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    return word_counts

def main():
    # Sample text
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed semper nisl. Sed euismod, nunc id aliquam lacinia, nunc nunc tincidunt sem, nec lacinia nisl nunc id nunc."
    
    # Count the words
    word_counts = count_words(text)
    
    # Print the word counts
    for word, count in word_counts.items():
        print(f'{word}: {count}')

if __name__ == "__main__":
    main()
