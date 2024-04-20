import unittest
import sys
from io import StringIO
from pre_09_04 import count_words as pre_count_words, print_word_counts as pre_print_word_counts
from ref_09_04 import calculate_word_counts as ref_calculate_word_counts, print_word_counts as ref_print_word_counts

class TestWordCount(unittest.TestCase):
    def test_pre_refactored_code(self):
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed semper nisl. Sed euismod, nunc id aliquam lacinia, nunc nunc tincidunt sem, nec lacinia nisl nunc id nunc."
        
        # Test count_words function
        pre_word_counts = pre_count_words(text)
        self.assertEqual(pre_word_counts['lorem'], 1)
        self.assertEqual(pre_word_counts['ipsum'], 1)
        self.assertEqual(pre_word_counts['dolor'], 1)
        self.assertEqual(pre_word_counts['sit'], 1)
        self.assertEqual(pre_word_counts['amet'], 1)
        self.assertEqual(pre_word_counts['consectetur'], 1)
        self.assertEqual(pre_word_counts['adipiscing'], 1)
        self.assertEqual(pre_word_counts['elit'], 1)
        self.assertEqual(pre_word_counts['sed'], 4)
        self.assertEqual(pre_word_counts['semper'], 1)
        self.assertEqual(pre_word_counts['nisl'], 2)
        self.assertEqual(pre_word_counts['euismod'], 1)
        self.assertEqual(pre_word_counts['nunc'], 4)
        self.assertEqual(pre_word_counts['id'], 3)
        self.assertEqual(pre_word_counts['aliquam'], 1)
        self.assertEqual(pre_word_counts['lacinia'], 2)
        self.assertEqual(pre_word_counts['tincidunt'], 1)
        self.assertEqual(pre_word_counts['sem'], 1)
        self.assertEqual(pre_word_counts['nec'], 1)
        
        # Test print_word_counts function
        captured_output = StringIO()
        sys.stdout = captured_output
        pre_print_word_counts(pre_word_counts)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "lorem: 1\nipsum: 1\ndolor: 1\nsit: 1\namet: 1\nconsectetur: 1\nadipiscing: 1\nelit: 1\nsed: 4\nsemper: 1\nnisl: 2\neuismod: 1\nnunc: 4\nid: 3\naliquam: 1\nlacinia: 2\ntincidunt: 1\nsem: 1\nnec: 1")
    
    def test_refactored_code(self):
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed semper nisl. Sed euismod, nunc id aliquam lacinia, nunc nunc tincidunt sem, nec lacinia nisl nunc id nunc."
        
        # Test calculate_word_counts function
        ref_word_counts = ref_calculate_word_counts(text)
        self.assertEqual(ref_word_counts['lorem'], 1)
        self.assertEqual(ref_word_counts['ipsum'], 1)
        self.assertEqual(ref_word_counts['dolor'], 1)
        self.assertEqual(ref_word_counts['sit'], 1)
        self.assertEqual(ref_word_counts['amet'], 1)
        self.assertEqual(ref_word_counts['consectetur'], 1)
        self.assertEqual(ref_word_counts['adipiscing'], 1)
        self.assertEqual(ref_word_counts['elit'], 1)
        self.assertEqual(ref_word_counts['sed'], 4)
        self.assertEqual(ref_word_counts['semper'], 1)
        self.assertEqual(ref_word_counts['nisl'], 2)
        self.assertEqual(ref_word_counts['euismod'], 1)
        self.assertEqual(ref_word_counts['nunc'], 4)
        self.assertEqual(ref_word_counts['id'], 3)
        self.assertEqual(ref_word_counts['aliquam'], 1)
        self.assertEqual(ref_word_counts['lacinia'], 2)
        self.assertEqual(ref_word_counts['tincidunt'], 1)
        self.assertEqual(ref_word_counts['sem'], 1)
        self.assertEqual(ref_word_counts['nec'], 1)
        
        # Test print_word_counts function
        captured_output = StringIO()
        sys.stdout = captured_output
        ref_print_word_counts(ref_word_counts)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "lorem: 1\nipsum: 1\ndolor: 1\nsit: 1\namet: 1\nconsectetur: 1\nadipiscing: 1\nelit: 1\nsed: 4\nsemper: 1\nnisl: 2\neuismod: 1\nnunc: 4\nid: 3\naliquam: 1\nlacinia: 2\ntincidunt: 1\nsem: 1\nnec: 1")

if __name__ == '__main__':
    unittest.main()
