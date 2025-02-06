# main.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

from utilities_package.english_utilities import *
# ToDo: Add your import statement here


if __name__ == "__main__":
    words = read_words()
    print(len(words), "words read from file")
    
    print("Total words that start with S:", count_total_words(words, "S"))

    mfl = most_frequent_letter(words)
    print("Most frequent letter(s):")
    for l in mfl:
        print(l)

    count = word_count_by_length(words, 10)
    print(count, "words are 10 characters in length")

    # ToDo: Contrive a test case for the most_frequent_letter function so there is a tie
    #  between at least 3 different letters.
