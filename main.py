from stats import get_word_count

def main():
    filepath = "books/frankenstein.txt"
    print(f"{get_word_count(filepath)} words found in the document")
    
main()