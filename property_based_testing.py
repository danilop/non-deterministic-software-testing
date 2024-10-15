import random
from hypothesis import given, strategies as st

def non_deterministic_sort(lst):
    """A non-deterministic sorting function that occasionally makes mistakes."""
    if random.random() < 0.1:  # 10% chance of making a mistake
        return lst  # Return unsorted list
    return sorted(lst)

@given(st.lists(st.integers()))
def test_non_deterministic_sort(lst):
    result = non_deterministic_sort(lst)

    # Property 1: The result should have the same length as the input
    assert len(result) == len(lst), "Length of the result should match the input"
    
    # Property 2: The result should contain all elements from the input
    assert set(result) == set(lst), "Result should contain all input elements"
    
    # Property 3: The result should be sorted in most cases
    attempts = [non_deterministic_sort(lst) for _ in range(100)]

    # We allow for some failures due to the non-deterministic nature
    # Replace 'any' with 'all' to make the test fail if any attempt is not sorted
    assert any(attempt == sorted(lst) for attempt in attempts), "Function should produce a correct sort in multiple attempts"

# Run the test
if __name__ == "__main__":
    test_non_deterministic_sort()
