'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.

Inside the recursive_count_th directory you'll find the count_th.py file. In this file, please add your recursive implementation to the count_th() method following these rules:

Your function should take in a single parameter (a string word)
Your function should return a count of how many occurrences of "th" occur within word. Case matters.
Your function must utilize recursion.
It cannot contain any loops.
Run python test_count_th.py to run the tests for your count_th() function to ensure that your implementation is correct.
'''
def count_th(word):
    # Find Base Case
    if len(word) < 2:
        return 0
    
    # starting at 0 and counting by 2 for a 'th' match - if it matches then add 1 recursive
    if(word[0:2] == 'th'): 
        return 1 + count_th(word[1:])

    return count_th(word[1:])
    

print(count_th("the only thing to test Tyrannossaurus Rex that is a long word for ht or th"))