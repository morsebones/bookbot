from stats import word_count
from stats import char_count
from stats import sorted_dict
import sys
def main():
    # Check if the correct number of command line arguments is provided
    # If not, print usage message and exit
    # If the correct number of arguments is provided, proceed with the program
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_text = get_book_text(sys.argv[1])
        num_words = word_count(book_text)
        char_counts = char_count(book_text)
        letter_counts = sorted_dict(char_counts)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for entry in letter_counts:
            print(f"{entry['char']}: {entry['num']}")
        print("============= END ===============")

# Function to read the book text from a file
# Takes the file path as an argument and returns the text
def get_book_text(book):
    with open(book) as f:
        text = f.read()
    return text

main()