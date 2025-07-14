from string_search import find_substring_positions

# importing function from string_search.py
# searches for all places a small word appears in a big sentence.
def run_primary_test_cases():
    print("Running primary test cases...")
    text = "Peter told me that peter the pickle piper piped a pitted pickle before he petered out. Phew!"

    test_cases = [
        ("Peter", [0, 19, 74]),
        ("peter", [0, 19, 74]),
        ("pick", [29, 57]),
        ("pi", [29, 36, 42, 50, 57]),
        ("z", []),
        ("Peterz", [])
    ]

    passed = 0
    for query, expected in test_cases:
        result = find_substring_positions(text, query)
        if result == expected:
            print(f"[PASS] '{query}' => {result}")
            passed += 1
        else:
            print(f"[FAIL] '{query}' => Got: {result}, Expected: {expected}")
    print(f"{passed}/{len(test_cases)} primary tests passed.\n")

if __name__ == "__main__":
    run_primary_test_cases()
