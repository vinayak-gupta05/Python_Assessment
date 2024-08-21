
''' Q19) Create a Python program that reads a text file named "paragraph.txt" and counts the occurrences of
each word in the paragraph, displaying the results in alphabetical order'''

from collections import Counter
import re

# Read and count words from "paragraph.txt"
word_count = Counter()

try:
    with open("paragraph.txt", "r") as file:
        text = file.read()
        # Normalize case and split into words using regex to handle punctuation
        words = re.findall(r'\b\w+\b', text.lower())
        word_count.update(words)
except FileNotFoundError:
    print("The file 'paragraph.txt' does not exist.")

# Display word count in alphabetical order
for word, count in sorted(word_count.items()):
    print(f"{word}: {count}")

