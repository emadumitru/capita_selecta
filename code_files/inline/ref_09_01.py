# Word Frequency Counter

def word_frequency_counter(text):
    """
    Count the frequency of each word in the given text.
    
    Args:
        text (str): The input text.
    
    Returns:
        dict: A dictionary containing the word frequencies.
    """
    word_freq = {}
    words = text.split()
    
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    return word_freq

def main():
    # Sample text
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor."
    
    # Count word frequencies
    word_freq = word_frequency_counter(text)
    
    # Print word frequencies
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")

if __name__ == "__main__":
    main()
