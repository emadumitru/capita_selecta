import unittest
from pre_09_05 import word_frequency_counter
from ref_09_05 import calculate_word_frequency
class TestWordFrequencyCounter(unittest.TestCase):
    def test_word_frequency_counter(self):
        text = "This is a test. This is only a test."

        # Test pre-refactored code
        expected_output_pre = [
            ("this", 2),
            ("is", 2),
            ("a", 2),
            ("test", 2),
            ("only", 1)
        ]
        result_pre = []
        def print_mock_pre(word, freq):
            result_pre.append((word, freq))
        word_frequency_counter(text)
        self.assertEqual(result_pre, expected_output_pre)

        # Test refactored code
        expected_output_ref = [
            ("this", 2),
            ("is", 2),
            ("a", 2),
            ("test", 2),
            ("only", 1)
        ]
        result_ref = []
        def print_mock_ref(word, freq):
            result_ref.append((word, freq))
        calculate_word_frequency(text)
        self.assertEqual(result_ref, expected_output_ref)

if __name__ == '__main__':
    unittest.main()
# Example usage
text = "This is a test. This is only a test."
calculate_word_frequency(text)