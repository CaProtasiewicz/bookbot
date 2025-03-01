from stats import get_word_count
from stats import character_count

def main():
    filepath = "books/frankenstein.txt"
    print(f"{get_word_count(filepath)} words found in the document")
    print(character_count(filepath))
    
main()