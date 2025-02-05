# english_utilities.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu



def read_words():
    """
        Read from a text file of English words into a list
        @return list: The words in a list. One word per element in the list or an emptuy list on exception
    """
    try:
        with open("data/english-2.txt", "r") as f:
            lines = f.readlines()  # Read all lines into a list
            # Optionally strip newline characters from each line:
            lines = [line.strip() for line in lines]
            return lines
    except FileNotFoundError:
        print(f"Error: File not found")
        return []
    except Exception as e:  # Catch other potential errors (e.g., permission issues)
        print(f"An error occurred: {e}")
        return []


if __name__ == "__main__":
    words = read_words()
    print(len(words), "words read from file")
