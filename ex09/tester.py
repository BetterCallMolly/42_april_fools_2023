import subprocess

tests = [
    ["Hello world how are you"],
    ["Hello", "world", "how", "are", "you"],
    ["Hello                world"],
    [""],
    ["😼"],
    ["Hello", "world", "how", "are", "you", "😼"],
]
if __name__ == "__main__":
    subprocess.check_call(["gcc", "-o", "frame", "frame.c"])
    for i, test in enumerate(tests):
        print(f"Test: ./frame {test}")
        if i >= len(tests) - 2:
            print("Multi-bytes characters are not properly handled")
        subprocess.check_call(["./frame"] + test)
        print("=========================================")

    # Same tests using valgrind to check for memory leaks
    for i, test in enumerate(tests):
        output = subprocess.check_output(["valgrind", "--leak-check=full", "./frame"] + test, stderr=subprocess.STDOUT)
        if b"ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)" not in output:
            print("Memory issues detected")
            exit(1)
        elif b"All heap blocks were freed -- no leaks are possible" not in output:
            print("Memory leaks")
            exit(1)
        else:
            print(f"Test #{i} : OK (no memory leaks detected)")