#xndir1 (Write a function that checks if a sentence is a pangram.)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def check_pangram(n):
    x = "The sentence is pangram."
    for i in alphabet:
        if i not in n.upper():
            x = "The sentence is not pangram."
    return x
y = check_pangram("The five boxing wizards jump quickly")
print(y)