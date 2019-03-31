def is_palindrome(word):
    # YOUR CODE GOES HERE
    if (word.lower() == word.lower()[::-1]):
        # .lower makes away with case differences
        return True
    else:
        return False

print(is_palindrome('Deleveled'))
# This should print True
