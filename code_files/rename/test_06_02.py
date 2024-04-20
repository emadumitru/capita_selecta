from ref_06_02 import tower_of_hanoi as ref_tower_of_hanoi, complex_tower_of_hanoi as ref_complex_tower_of_hanoi
from pre_06_02 import tower_of_hanoi as pre_tower_of_hanoi, complex_tower_of_hanoi as pre_complex_tower_of_hanoi
def test_tower_of_hanoi():
    # Test case 1
    n = 3
    source = "A"
    auxiliary = "B"
    destination = "C"

    print("Testing pre-refactored tower_of_hanoi...")
    pre_tower_of_hanoi(n, source, auxiliary, destination)

    print("Testing refactored tower_of_hanoi...")
    ref_tower_of_hanoi(n, source, auxiliary, destination)

def test_complex_tower_of_hanoi():
    # Test case 1
    n = 3

    print("Testing pre-refactored complex_tower_of_hanoi...")
    pre_complex_tower_of_hanoi(n)

    print("Testing refactored complex_tower_of_hanoi...")
    ref_complex_tower_of_hanoi(n)

# Run the tests
test_tower_of_hanoi()
test_complex_tower_of_hanoi()
