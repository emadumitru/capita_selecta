# Word Frequency Counter

def calculate_word_frequencies(text):
    """
    Calculate the frequency of each word in the given text.
    
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

def print_word_freq(word_freq):
    """
    Print the word frequencies in a formatted manner.
    
    Args:
        word_freq (dict): A dictionary containing the word frequencies.
    """
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")

def main():
    # Sample text
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor."
    
    # Calculate word frequencies
    word_freq = calculate_word_frequencies(text)
    
    # Print word frequencies
    print_word_freq(word_freq)

if __name__ == "__main__":
    main()