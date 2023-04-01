import subprocess

tests = {
    "D8": "18\n",
    "A4": "15\n",
    "AA8": "20\n",
    "339A6": "22\n",
    "AA8A": "Blackjack!\n",
    "asdmk": None,
    "": None,
    "AAAAAAAAAAAAA": None, # Cheating
    "A44444A": None, # Cheating
    "12311231231231231231231231231231231232213": None, # Cheating
}

if __name__ == "__main__":
    subprocess.check_call(["gcc", "-o", "blackjack", "blackjack.c"])
    for test, expected in tests.items():
        print(f"Test: {test}")
        try:
            result = subprocess.check_output(["./blackjack", test]).decode()
            print(f"Result: {result}")
            print(f"Expected: {expected}")
            if result != expected:
                print("Test failed!")
                exit(1)
            else:
                print("Test passed!")
        except subprocess.CalledProcessError:
            if expected is not None:
                print("Test failed!")
                exit(1)
            else:
                print("Test passed! (expected failure)")
        print("=*" * 20)
    
