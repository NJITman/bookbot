def get_word_count(text):
  return len(text.split())

def get_letter_counts(text):
  letter_counts = {}
  for char in text:
    find_char = char.lower()
    if find_char in letter_counts:
      letter_counts[find_char] += 1
    else:
      letter_counts[find_char] = 1

  return letter_counts


with open("./books/frankenstein.txt") as f:
  file_contents = f.read()

print("--- Begin report of books/frankenstein.txt ---")
print(f"{get_word_count(file_contents)} words found in the document")
letter_counts = get_letter_counts(file_contents)
letter_sorted = sorted(list(letter_counts.keys()))
for letter in letter_sorted:
  if letter.isalpha():
    print(f"The '{letter}' character was found {letter_counts[letter]} times")
print("--- End report ---")
