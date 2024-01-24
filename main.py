from collections import Counter
import os

def main():
    book_path = "/home/libertus/workspace/github.com/lLibertusl/bookbot/books/frankenstein.txt"
    book_title = os.path.basename(os.path.normpath(book_path))
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    
    print(f"--- Begin report of {book_title} ---")
    print(f"{num_words} words found in the document\n")
    get_letter_report_descending_values(num_letters)
    print(f"--- End report ---")

def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)

def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()
    
def get_num_letters(text: str) -> dict:
    text = text.lower()
    letter_count_dict = dict(Counter(text))
    return letter_count_dict

def get_letter_report_descending_values(text_dict: dict) -> str:
     text_dict_sorted = sorted(text_dict.items(), key=lambda x:x[1], reverse=True)
     for i in text_dict_sorted:
          if i[0].isalpha():
               print(f"The '{i[0]}' character was found {i[1]} times")


main()