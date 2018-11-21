"""I pledge my honor that I have abided by the Stevens Honor System - ppate78"""


FullAdder = { ('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }

def numToBaseB(N, B):
    """Takes in a non-negative integer and a base between 2 and 10 and returns the number in that base."""
    if N == 0:
        return '0'
    if N // B == 0:
        return str(N % B)
    return numToBaseB(N // B, B) + str(N % B)

def baseBToNum(S, B):
    """Takes in a string and a base where the string represents a number in the base. Returns the number as an integer in base 10."""
    if S == '':
        return 0
    return int(S[0]) * B ** (len(S)-1) + baseBToNum(S[1:], B)

def addB(S1, S2):
    """Takes in 2 binary strings and adds them."""
    def addB_help(s, t, carry):
        if s == '' and t == '':
            if carry == '0':
                return ''
            return '1'
        if s == '':
            summ, car = FullAdder[('0', t[-1], carry)]
        elif t == '':
            summ, car = FullAdder[(s[-1], '0', carry)]
        else:
            summ, car = FullAdder[(s[-1], t[-1], carry)]
        return addB_help(s[:-1], t[:-1], car) + summ
    
    return addB_help(S1, S2, '0')

def pad(i, k):
    if len(i) < k:
        return (k-len(i)) * '0' + i
    if len(i) == k:
        return i
    if len(i) > k:
        return i[-k-1:-1]
def Toggle(s):
    if s == '':
        return ''
    if s[0] == '1':
        return '0' + Toggle(s[1:])
    if s[0] == '0':
        return '1' + Toggle(s[1:])
    
def TcToNum(S):
    """takes in a string of binary in twos complement and returns an integer"""
    if S[0] == '0':
        return baseBToNum(S, 2)
    S = Toggle(S)
    return 0 - baseBToNum(addB(S, '00000001'), 2)
    
    
def NumToTc(N):
    """takes in a number, and returns the twos complement binary representation of that string"""
    if N < -128 or N > 127:
        return "Error"
    if N >= 0:
        return pad(numToBaseB(N, 2), 8)
    N = abs(N)
    return addB(Toggle(pad(numToBaseB(N, 2), 8)), '1')