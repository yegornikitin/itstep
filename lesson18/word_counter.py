import re
def words_count(file_name: str):
    with open(file_name, "r") as f:
        fileread = f.read()
        list_of_words = re.split(" |\n",  fileread)
        print("Words in File: ", list_of_words)
        print("Count of words in File: ", len(list_of_words))



words_count("for_word_counter.txt")






