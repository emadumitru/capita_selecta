### Type: Word Frequency Counter --- Style: Peaceful

def word_frequency_counter(text):
    # Step 1: Convert the text to lowercase
    text = text.lower()

    # Step 2: Remove punctuation marks
    punctuation_marks = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for mark in punctuation_marks:
        text = text.replace(mark, "")

    # Step 3: Split the text into words
    words = text.split()

    # Step 4: Create a dictionary to store word frequencies
    word_freq = {}

    # Step 5: Count the frequency of each word
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # Step 6: Sort the word frequencies in descending order
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

    # Step 7: Print the word frequencies
    for word, freq in sorted_word_freq:
        print(f"{word}: {freq}")

# Example usage
text = "This is a test. This is only a test."
word_frequency_counter(text)