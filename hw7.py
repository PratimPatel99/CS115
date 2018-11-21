'''i pledge my honor that I have abided by the Stevens Honor System -ppate78'''

def numToBaseB(N,B):
    '''takes in a number and changes it to a number of base b'''
    if N==0:
        return ""
    return numToBaseB(N//B,B)+str(N%B)
print(numToBaseB(4,3))

def baseBToNum(S,B):
    '''takes in a number of base b and changes it to a number of base 10'''
    def baseBToNum_helper(S,B,count):
        if S=='':
            return 0
        return int(S[-1])*(B**(count))+baseBToNum_helper(S[:-1],B,count+1)
    return baseBToNum_helper(S,B,0)
print(baseBToNum('11',2))

def baseToBase(B1,B2,sinB1):  
    '''takes in B1,B2,sinB1, and returns the equivalent value in base B2'''
    return numToBaseB((baseBToNum(sinB1,B1)),B2)
print(baseToBase(10,2,'3'))

def add(S,T):
    '''takes in S and T and returns the binary version of those'''
    return numToBaseB((baseBToNum(S,2)+baseBToNum(T,2)),2)
print(add('011','100'))


FullAdder ={ ('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }

def addB(S1,S2):
    '''adds two binary numbers'''
    def addB_help(s,t,c):
        if s =='' and t == '':
            if c =='0':
                return ''
            return '1'
        if s =='':
                summ,car = FullAdder[('0',t[-1],c)]
        elif t == '':
                summ,car = FullAdder[(s[-1], '0', c)]
        else:
                summ, car = FullAdder[(s[-1], t[-1], c)]
        return addB_help(s[:-1], t[:-1], car) + summ
            
    return addB_help(S1,S2,'0')
print(addB('11','1'))


    