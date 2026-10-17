# Text Wrap
# problem link - https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap
def wrap(string, max_width):
    wraped_str=textwrap.fill(string,max_width)   
    return wraped_str
    '''
    How the textwrap will works:
    ---------------------------
    import textwrap
    s = "ABCDEFGHIJKL"
    print(textwrap.fill(s, width=4))
    
    output:
    ABCD
    EFGH
    IJKL
    '''
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
