# nicholdw.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

from collections import Counter

def count_total_words(words, prefix):
    """
    Count the total words that start with a particular string
    @param words list: The words to process
    @param prefix string: The prefix to use
    @return the number of words in words that begin with 
    """
    # Use list comprehension
    sub_list = [word for word in words if word.startswith(prefix)]
    return len(sub_list)


def most_frequent_letter(words):
    """
    Find the most frequent letter in a list of words, using case-inseneitive logic. 
    @param words list: The words to process
    @return list: A 1-element list if there's only one, else a multi-element list if there's a tie. 
    """

    letter_counts = Counter()  # Use Counter for efficient counting

    for word in words:
        for letter in word:
            letter = letter.lower() #count lowercase and uppercase the same.
            if letter.isalpha(): #only count letters
                letter_counts[letter] += 1

    if not letter_counts: #no letters in the words
        return []

    max_frequency = max(letter_counts.values())  # Find the highest frequency

    most_frequent = [letter for letter, count in letter_counts.items() if count == max_frequency]

    return most_frequent

def word_count_by_length(words, length):
    """
    Count the number of words that are a specific length
    @param words list: The words to process
    @param length int: The length to test for
    @return int: The number of words that are length characters 
    """
    count = 0
    for word in words:
        if len(word) == length:
            count += 1
    return count
    