def get_word_count(filepath):
    word_count = 0
    with open(filepath) as f:
        book_text = f.read()
        words_split = book_text.split()
        for word in words_split:
            word_count += 1
    return word_count