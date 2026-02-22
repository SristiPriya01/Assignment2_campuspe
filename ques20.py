# 1. Count number of words
def count_words(text):
    # Split text by spaces and return length
    return len(text.split())


# 2. Count number of vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


# 3. Count number of consonants
def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        # Check if alphabet and not vowel
        if char.isalpha() and char not in vowels:
            count += 1
    return count


# 4. Reverse the text
def reverse_text(text):
    return text[::-1]


# 5. Check if text is palindrome (ignore case and spaces)
def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


# 6. Remove vowels from text
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result


# 7. Word frequency (returns dictionary)
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        # Remove punctuation marks
        word = word.strip(".,!?")
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq


# 8. Find longest word
def longest_word(text):
    words = text.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


# 9. Main analysis function
def analyze_text(text):
    print("\nText Analysis Results")
    print("Word count:", count_words(text))
    print("Vowel count:", count_vowels(text))
    print("Consonant count:", count_consonants(text))
    print("Reversed text:", reverse_text(text))
    print("Is palindrome:", is_palindrome(text))
    print("Text without vowels:", remove_vowels(text))
    print("Word frequency:", word_frequency(text))
    print("Longest word:", longest_word(text))


# Run program
if __name__ == "__main__":
    user_text = input("Enter text: ")
    analyze_text(user_text)