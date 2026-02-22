# Step 1: Define some characters
characters = ['a', 'b', 'c', 'd']

# Step 2: Create a dictionary that maps characters to numbers
char_to_index = {char: index for index, char in enumerate(characters)}

# Step 3: Create a dictionary that maps numbers back to characters
index_to_char = {index: char for char, index in char_to_index.items()}

# Step 4: Print the dictionaries
print("Character → Index:")
print(char_to_index)

print("\nIndex → Character:")
print(index_to_char)

# Step 5: Use the dictionaries
letter = 'c'
number = char_to_index[letter]

print(f"\nThe character '{letter}' becomes the number {number}")
print(f"The number {number} becomes the character '{index_to_char[number]}'")
