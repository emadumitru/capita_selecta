### Type: Word Frequency Counter --- Style: Simple

def word_frequency_counter(text):
    word_count = {}
    words = text.split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

def print_word_frequency(word_count):
    for word, count in word_count.items():
        print(f"{word}: {count}")

# Sample text
text = "This is a sample text. It contains some words that will be counted."

# Count word frequency
word_count = word_frequency_counter(text)

# Print word frequency
print_word_frequency(word_count)