'''
Created on _______________________
@author:   _______________________
Pledge:    _______________________

CS115 - Hw 5
I pledge my honor that I have abided by the Stevens Honor System
-ppate78
'''

import turtle  # Needed for graphics
from math import inf
# Ignore 'Undefined variable from import' errors in Eclipse.
def sv_tree(trunkLength,levels):
    """prints out a tree with a certain amount of levels and with a certain trunklength"""
    def sv_tree_helper(trunkLength,levels):
        if levels==0:
            return
        turtle.forward(trunkLength)
        turtle.left(45)
        sv_tree_helper(trunkLength/2,levels-1)
        turtle.right(90)
        sv_tree_helper(trunkLength/2,levels-1)
        turtle.left(45)          
        turtle.backward(trunkLength)
    
    sv_tree_helper(trunkLength, levels)
    turtle.done()
#sv_tree(100, 4)

def fast_lucas(n):
    """returns the lucas number"""
    def fast_lucas_memo(n,memo):
        if n in memo:
            return memo[(n)]
        if n==0:
            return 2
        if n==1:
            return 1
        result= fast_lucas_memo(n-1,memo)+fast_lucas_memo(n-2,memo)
        memo[(n)]=result
        return result
    return fast_lucas_memo(n,{})



def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, coins, memo):
        if (amount,coins) in memo:
            return memo[(amount,coins)]
        if coins == ():
            return float(inf)
        if amount == 0:
            result= 0
        elif coins == []:
            result= float(inf)
        elif coins[0]>amount:
            result= fast_change_helper(amount,coins[1:],memo)
        else:
            loseit=fast_change_helper(amount,coins[1:], memo)
            useit= 1+ fast_change_helper(amount - coins[0], coins, memo)
            result = min(useit,loseit)
        memo[(amount,coins)] = result
        return result
    return fast_change_helper(amount, tuple(coins), {})

    # Call the helper. Note we converted the list to a tuple.
    

# If you did this correctly, the results should be nearly instantaneous.

print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a tree.
sv_tree(128, 4)
"""
Created on Oct 8, 2017

@author: NehiPrat
"""