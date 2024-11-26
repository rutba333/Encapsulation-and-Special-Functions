class class_reverse:
    def __init__(self, word_s):
        self.s = word_s

    def reverse_word(self):
        return self.s[::-1]

# Taking input from the user
word = input("Enter the word to be reversed: ")
rev_ob = class_reverse(word)
result = rev_ob.reverse_word()

# Printing the reversed string
print("Reversed String:", result)
    