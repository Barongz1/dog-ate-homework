"""The Dog Ate My Homework: Funniest Excuse — entry for make.fun.

Writes one line to /output/entry.txt. The line is a dog's excuse after being caught eating the homework, under 200 characters.
"""
import os

LINE = "It wasn't homework, it was a snack with math on it, and honestly the fractions tasted better than the answers."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
