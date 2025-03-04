from stats import get_word_count, character_count, sort_dict
import sys

def main():
    
    arguments = sys.argv
    filepath = sys.argv[1]
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    with open(filepath) as f:
       contents = f.read()

    word_count = get_word_count(contents)
    char_count = character_count(contents)
    sorted_chars = sort_dict(char_count)
      
           
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_data in sorted_chars:
        if char_data["character"].isalpha():
            print(f"{char_data["character"]}: {char_data["count"]}")
    print("============= END ===============")
    

main()