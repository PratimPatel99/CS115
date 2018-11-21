''''I pledge my honor that I have abided by the Stevens Honor System. ppate78'''
from cs115 import range, reduce, map
'''the factorial function checks the base case of 0, and if it is 0 then it returns 1. If the value of n is not 0, it continuously calls
factorial until n gets to 0 (which it will use the value of 1 for) and then multiply all the values together to get the factorial'''
def factorial(n):
    if(n==0):
        return 1
    return n*factorial(n-1)
def add(m,l):
    """the add function simply takes in two values and then adds them together"""
    return(m+l)
def mean(L):
    """"the mean function first checks if the list is empty. Then, it takes the length of the list, adds all of the values of the list
using the sum function, and then divides it by the length. This gives the mean of the list"""
    if L==[]:
        return "The String is Empty"
    k=len(L)
    return (reduce(add,L))/k
def divides(n):
    def div(k):
        return n%k==0
    return div
'''checks to see if n is either 0 or 1, and if it is, it returns false. Otherwise, it will take the value of n, and then it will run all the values from 2
to 1 less than n in the divides function, and it will add all of the results of that. If the value is prime, then each value should be 0 and it will
return true meaning it is prime.'''
def prime(n):    
    if(n==1)or(n==0): return False
    return sum(map(divides(n),(range(2,n))))==0       
