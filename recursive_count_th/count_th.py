"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""
def count_th(word):
    # base case: if the given word is less than 2 then `th` cannot occur so return 0
    if len(word) < 2:
        return 0
    # check if the next two characters are `th`
    elif word[:2] == 'th':
        # The recursive call moves to the next character in the word and increments the number of times `th` appears
        return count_th(word[1:]) + 1
    # if the next two letters are not `th` then we move to the next letter in the word
    else:
        return count_th(word[1:])
