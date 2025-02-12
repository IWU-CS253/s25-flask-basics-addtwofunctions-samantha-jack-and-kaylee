def average_length(user_string):
    words = user_string.split()
    if words:  # Ensure the string is not empty
        avg = sum(len(word) for word in words) / len(words)
    else:
        avg = 0
    return avg

def count_words(user_string):
    words = user_string.split()
    if words:  # Ensure the string is not empty
        word_count = len(words)
    else:
        word_count = 0
    return word_count

def count_char(user_string):
    words = user_string.split()
    if words:  # Ensure the string is not empty
        char_count = 0
        for word in words:
            char_count += (len(word))
    else:
        char_count = 0
    return char_count