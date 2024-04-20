def word_frequency_counter(text):
    # Step 1: Convert the text to lowercase
    text = text.lower()

    # Step 2: Remove punctuation marks
    text = remove_punctuation_marks(text)

    # Step 3: Split the text into words
    words = text.split()

    # Step 4: Create a dictionary to store word frequencies
    word_freq = count_word_frequencies(words)

    # Step 6: Sort the word frequencies in descending order
    sorted_word_freq = sort_word_frequencies(word_freq)

    # Step 7: Print the word frequencies
    print_word_frequencies(sorted_word_freq)


def remove_punctuation_marks(text):
    punctuation_marks = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for mark in punctuation_marks:
        text = text.replace(mark, "")
    return text


def count_word_frequencies(words):
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq


def sort_word_frequencies(word_freq):
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_freq


def print_word_frequencies(sorted_word_freq):
    for word, freq in sorted_word_freq:
        print(f"{word}: {freq}")


# Example usage
text = "This is a test. This is only a test."
word_frequency_counter(text)