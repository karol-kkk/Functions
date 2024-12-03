# main.py
from letter_count import count_letter

text = "You never get a second chance to make a first impression"
letter = 'e'
letter_count = count_letter(text, letter)

print(f"The number of letter '{letter}': {letter_count}")