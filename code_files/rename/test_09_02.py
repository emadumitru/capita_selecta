import unittest
from pre_09_02 import word_frequency_counter as pre_word_frequency_counter, print_word_frequency as pre_print_word_frequency
from ref_09_02 import calculate_word_frequency, print_word_frequency

class TestWordFrequencyCounter(unittest.TestCase):
    def test_pre_refactored_code(self):
        # Sample text
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor."

        # Calculate word frequency using pre-refactored code
        pre_word_counts = pre_word_frequency_counter(text)

        # Calculate word frequency using refactored code
        ref_word_counts = calculate_word_frequency(text)

        # Compare the word counts
        self.assertEqual(pre_word_counts, ref_word_counts)

    def test_pre_refactored_code_print(self):
        # Sample text
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor."

        # Calculate word frequency using pre-refactored code
        pre_word_counts = pre_word_frequency_counter(text)

        # Print word frequency using pre-refactored code
        pre_print_word_frequency(pre_word_counts)

    def test_refactored_code_print(self):
        # Sample text
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor."

        # Calculate word frequency using refactored code
        ref_word_counts = calculate_word_frequency(text)

        # Print word frequency using refactored code
        print_word_frequency(ref_word_counts)

if __name__ == '__main__':
    unittest.main()
