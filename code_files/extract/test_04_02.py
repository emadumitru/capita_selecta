import unittest
from pre_04_02 import roll_dice as pre_roll_dice
from ref_04_02 import roll_dice as ref_roll_dice

class TestDiceRoll(unittest.TestCase):
    def test_pre_roll_dice(self):
        # Test the pre-refactored roll_dice function
        # by capturing the output and comparing it with the expected output
        
        # Redirect stdout to a StringIO object
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output
        
        pre_roll_dice()
        
        # Get the captured output
        output = captured_output.getvalue().strip()
        
        # Define the expected output
        expected_output = '''
         _________ 
        |         |
        |    *    |
        |         |
         ‾‾‾‾‾‾‾‾‾ 
        '''
        
        # Compare the output with the expected output
        self.assertEqual(output, expected_output)
    
    def test_ref_roll_dice(self):
        # Test the refactored roll_dice function
        # by capturing the output and comparing it with the expected output
        
        # Redirect stdout to a StringIO object
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output
        
        ref_roll_dice()
        
        # Get the captured output
        output = captured_output.getvalue().strip()
        
        # Define the expected output
        expected_output = '''
         _________ 
        |         |
        |    *    |
        |         |
         ‾‾‾‾‾‾‾‾‾ 
        '''
        
        # Compare the output with the expected output
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
