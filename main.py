# open and read all of the contents of frankenstein.txt to the console
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
                #print(file_contents)

        # print the word count
        word_count = wordCount(file_contents)
                #print("The number of words in the book Frankenstein is: " + str(word_count))

        # print the count of each character used in the book
        character_count = characterCount(file_contents)
                #print(character_count)
        
        print("--- Begin report of books/frankenstein.txt ---")
        print(str(word_count) + " words were found in the document")

        for key in character_count:
                if key.isalpha(): 
                        print("The '" + key + "' character was found " + str(character_count[key]) + " times")

        print("--- End report ---")


# count and return the number of words in the book
def wordCount(file_contents):
        words = file_contents.split()
        return len(words)

# count and return the number of times each char is used in the book
def characterCount(file_contents):
        chars_hash = {}

        # combined_words = "".join(file_contents.split())                                    <--- use this to ignore whitespaces

        combined_words = file_contents

        for char in combined_words:
                # if the char is uppercase, make it lowercase
                if char.isupper():
                        char = char.lower()
                # if the char is already in the hash, increment the count by 1
                if char in chars_hash:
                        chars_hash[char] += 1
                # else, if the char is not in the hash, add it to the hash and set count to 1
                else:
                        chars_hash[char] = 1

        return chars_hash

main()