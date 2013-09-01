with open("enWord_list.txt") as word_file:
    english_words = set(word.strip().lower() for word in word_file)

def is_english_word(word):
    if word.lower() in english_words:
        return "true"
