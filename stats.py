def get_word_count(contents):
    word_count = 0
    words_split = contents.split()
    for word in words_split:
        word_count += 1
    return word_count

def character_count(contents):
    character_dict = {}
    book_text = contents.lower()
    for character in book_text:
        if character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1
    return character_dict

def sort_dict(dictionary):
    char_list = []
    
    # Loopa por cada caractere e sua contagem no dicionário
    for character, count in dictionary.items():
        # Cria um novo dicionário para esse caractere
        char_dict = {
            "character": character,
            "count": count
        }
        # Adiciona esse dicionário para nossa lista
        char_list.append(char_dict)
        
    # Organizar a lista baseado na contagem
    # Função que define o valor para ser organizado com base    
    def sort_on(char_dict):
        return char_dict["count"]
    
    # Organizar a lista em ordem decrescente (reverse = True)
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list