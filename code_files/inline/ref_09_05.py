import string

def word_frequency_counter(text):
    # Step 1: Convert the text to lowercase
    text = text.lower()

    # Step 2: Remove punctuation marks
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Step 3: Split the text into words
    words = text.split()

    # Step 4: Create a dictionary to store word frequencies
    word_freq = {}

    # Step 5: Count the frequency of each word
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    # Step 6: Sort the word frequencies in descending order
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

    # Step 7: Return the word frequencies
    return sorted_word_freq

# Example usage
text = "This is a test. This is only a test."
result = word_frequency_counter(text)
for word, freq in result:
    print(f"{word}: {freq}")
