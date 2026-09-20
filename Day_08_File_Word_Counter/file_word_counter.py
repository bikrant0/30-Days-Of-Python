# File Word Counter

def count_words(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            print(f"\nFile: '{filename}'")
            print(f"Total words: {word_count}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


with open("sample.txt", "w") as file:
    file.write("Hello world. This is a sample text file for Day 8 of my Python challenge.")

if __name__ == "__main__":
    print("Welcome to the File Word Counter!")
    filename = input("Enter the filename (or press Enter for sample.txt): ").strip()
    if filename == "":
        filename = "sample.txt"
    count_words(filename)