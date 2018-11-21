"""I pledge my honor that I have abided by the Stevens Honor System -ppate78"""

def pascal_row(n):
    """takes in a number and returns the pascal row of that number"""
    if n==0:
        return [1]
    def pascal_helper(lst):
        if lst==[]:
            return []
        if len(lst)==1:
            return []
        return [lst[0]+lst[1]]+pascal_helper(lst[1:])
    return [1]+ pascal_helper(pascal_row(n-1)) + [1]

def pascal_triangle(n):
    """takes in a number and returns all pascal rows up to that number"""
    if n == 0:
        return [[1]]
    if n == 1:
        return [[1] , [1, 1]]
    return pascal_triangle(n - 1) + [pascal_row(n)]

    
        
        