import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were', 'will', 'with'
]

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as text:
        text = text.read().lower()
        text = text.replace("\n", " ")
        text = text.replace("’", "")
        # text = " ".join(text.split())
        # print(text)
        for character in string.punctuation:
            text = text.replace(character, "")
        word_list = text.split()
        clean_list = []
        for word in word_list:
            if word not in STOP_WORDS:
                clean_list.append(word)
                

        # for stop_word in STOP_WORDS:
        #     if stop_word in word_list:
        #         word_list.remove(stop_word)


        new_dict = {}
        for word in clean_list:
            new_dict[word] = clean_list.count(word)
            sorted_dict = sorted(new_dict.items())
        print(sorted_dict)

        # print(f"{key} | {value} {'*' * value}")

        
        # for stop_word in STOP_WORDS:
        #     text = text.replace(stop_word, "")

        # for word in word_list:
        #     if word in string.punctuation:
        #         #do something
        #     if word in STOP_WORDS:

        
        # for stop_word in STOP_WORDS:
        #     text = text.replace(stop_word, "")
        # print(text)



# make a loop that loops through the list and takes out anything that is equal to stop words

        # print (f"{len(lines)} lines in the file.")
        # for line in lines:
        #     line = line.replace(",", "")
        #     line = line.replace(".", "")
        #     line = line.replace("-", "")
        #     line = line.replace("?", "")
        #     line = line.replace(":", "")
        #     line = line.replace("’", "")
        #     line = line.lower()
        #     line = line.split()
        #     print(line)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
