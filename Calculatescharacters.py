import string

def count_characters(phrase):
    spaces = 0
    special_characters = 0
    numbers = 0
    alphabets = 0
    
    for char in phrase:
        if char == ' ':
            spaces += 1
        elif char.isnumeric:
            numbers += 1
        elif char.isalpha():
            alphabets += 1
        elif char in string.punctuation:
            special_characters += 1
            
    return spaces, special_characters, numbers, alphabets

# Input phrase
phrase = input("Enter a phrase with spaces, alphabets, numbers and special characters.: ")

# Call the function to count characters
spaces, special_characters, integers, alphabets = count_characters(phrase)

# Print the results
print(f"Spaces: {spaces}")
print(f"Special characters: {special_characters}")
print(f"Numbers: {numbers}")
print(f"Alphabets: {alphabets}")
