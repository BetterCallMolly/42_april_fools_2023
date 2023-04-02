import subprocess
import os
from time import time

if __name__ == "__main__":
    if not os.path.exists("./sastantua"):
        print("You need to compile sastantua.c first")
        exit(1)
    if not os.path.exists("./sastantua_linux"):
        print("Please download the binary from the intranet")
        exit(1)
    for i in range(-1, 41):
        org_time = time()
        expected_output = subprocess.check_output(["./sastantua_linux", str(i)])
        org_time = time() - org_time

        my_time = time()
        output = subprocess.check_output(["./sastantua", str(i)])
        my_time = time() - my_time

        percentage = (org_time - my_time) / org_time * 100
        rapport = "slower" if percentage > 0 else "faster"
        if output != expected_output:
            print("Error with size", i)
        else:
            print("OK with size {} ({}% {} than the original)".format(i, abs(percentage), rapport))

