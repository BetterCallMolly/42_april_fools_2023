import os
import sys
import shutil

shutil.copy("game_linux", "game_linux_patched")

OFFSETS = [
    (0x00001232, 0x00001237, "Disable call to scanf (no name)"),
    (0x00001319, 0x0000131E, "Disable call to srand"),
    (0x0000136E, 0x00001373, "Disable call to scanf (first input)"),
    (0x0000128A, 0x0000128F, "Disable call to strcat (corrupts name)"),
]


# Set all bytes to NOP (0x90)
with open("game_linux_patched", "r+b") as f:
    for i, (offset, end_offset, description) in enumerate(OFFSETS):
        print(f"Patch {i + 1}/{len(OFFSETS)}: {description}...", end="")
        f.seek(offset)
        f.write(b"\x90" * (end_offset - offset))
        print("Done!")


# Run the game (execve)
os.execv("game_linux_patched", ["game_linux_patched"])