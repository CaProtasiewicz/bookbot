def get_word_count(filepath):
    word_count = 0
    with open(filepath) as f:
        book_text = f.read()
        words_split = book_text.split()
        for word in words_split:
            word_count += 1
    return word_count

def character_count(filepath):
    character_dict = {}
    with open(filepath) as f:
        book_text = f.read()
        book_text = book_text.lower()
        words_list = book_text.split()
        words_split = "".join(words_list)
        for character in words_split:
           if character not in character_dict:
                character_dict[character] = 1
           else:
               character_dict[character] += 1
    return character_dict
    
    
    