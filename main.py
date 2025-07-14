# asking user input the text to search
from string_search import find_substring_positions, format_position

def main():
    text = input("Enter the main text: ")
    subtext = input("Enter the subtext to search for: ")

    matches = find_substring_positions(text, subtext)
    output = format_position(matches)
    print("\nResult:")
    print(output)

if __name__ == "__main__":
    main()
