# Q3: String Manipulator
# Performs various string operations
def string_manipulator():
    text = input("Enter sentence: ")

    words = text.split()   # Splitting sentence into words

    print("Original:", text)
    print("Characters (with spaces):", len(text))
    print("Characters (without spaces):", len(text.replace(" ", "")))
    print("Words:", len(words))
    print("UPPERCASE:", text.upper())
    print("lowercase:", text.lower())
    print("Title Case:", text.title())

    # Checking if sentence is not empty
    if words:
        print("First word:", words[0])
        print("Last word:", words[-1])

    print("Reversed:", text[::-1])  # String slicing to reverse

if __name__=="__main__":
    string_manipulator()