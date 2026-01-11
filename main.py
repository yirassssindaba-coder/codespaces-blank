from mean_var_std import calculate

# Example 1: Valid input (should work)
list_input_valid = [0, 1, 2, 3, 4, 5, 6, 7, 8]
try:
    result = calculate(list_input_valid)
    print("--- Valid Input Result ---")
    for key, value in result.items():
        print(f"'{key}': {value}")
except ValueError as e:
    print(f"Error with valid input: {e}")

print("\n" + "="*40 + "\n")

# Example 2: Invalid input (should raise ValueError)
list_input_invalid = [1, 2, 3]
try:
    calculate(list_input_invalid)
except ValueError as e:
    print(f"--- Invalid Input Test Passed ---")
    print(f"Caught expected error: '{e}'")

# Note: The actual freeCodeCamp tests are in test_module.py which main.py typically imports. 
# This simple main.py helps you test your function manually.
