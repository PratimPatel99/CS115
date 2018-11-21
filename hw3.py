'''
Created on 9/27/17 _______________________
@author:ppate78   _______________________
Pledge:  I pledge my honor that I have abided by the stevens honor system  _______________________

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here
def giveChange(amount, change):
    """takes in an amount and a list of coins, and returns the minimum amount of coins in order to get that amount, and what coins"""
    if amount == 0:
        return [0, []]
    if change == []:
        return [float("inf"), []]
    if change[0] > amount:
        return giveChange(amount, change[1:])
    [use_it_amount, use_it_list] = giveChange(amount-change[0], change)
    [lose_it_amount, lose_it_list] = giveChange(amount, change[1:])
    if use_it_amount + 1 < lose_it_amount:
        use_it_list.append(change[0])
        return [use_it_amount + 1, use_it_list]
    else:
        return [lose_it_amount, lose_it_list]
# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''' '''''''''''''''''''''''''''''' '''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''' '''''''''''''''''''''''''''''' '''''''''''''''''
def letterScore(letter, scorelist):
    """takes in a letter and the scorelist and returns the score of the letter"""
    if scorelist == []:
        return 0
    first = scorelist[0]
    if first[0] == letter:
        return first[1]
    return letterScore(letter, scorelist[1:])

def wordScore(S, scorelist):
    """takes in a word and a scorelist, and returns the score of the word"""
    if S == '':
        return 0
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)
    
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.
    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    if dct == []:
        return []
    if scores == []:
        return ['', 0]
    return [dct[0], wordScore(dct[0], scores)] + wordsWithScore(dct[1:], scores)

'''''''''''''''''''''''''''''' '''''''''''''''''''''''''''''' '''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''' '''''''''''''''''''''''''''''' '''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    def take_helper(n,L,accum):
        if n==1:
            return L[0]
        if L==[]:
            return []
        if n==accum:
            return L[0:accum]
        return take_helper(n,L,accum+1)
    return take_helper(n,L,0)
'''''''''''''''''''''''''''''' '''''''''''''''''''''''''''''' '''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''' '''''''''''''''''''''''''''''' '''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    def drop_helper(n,L,accum):
        if n==0:
            return []
        if L==[]:
            return[]
        if n==accum:
            return L[accum:]
        return drop_helper(n,L,accum+1)
    return drop_helper(n,L,0)
