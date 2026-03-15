num = int(input("Enter a number: "))

print("\nMultiplication Table of", num)

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

#song

import time
import sys

def typing(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.07)
    print()

print("Initializing music terminal...\n")
time.sleep(1)

typing("♪ Aarambh hai prachand")
typing("♪ Bole mastakon ke jhund")

time.sleep(1)
print("\nProcess completed ✓")

