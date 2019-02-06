#flag = ""
#flag = input('put some input in will ya? ')

import itertools

def compress(flag):
    b = ""
    for i in range(len(flag)):
        b += bin(ord(flag[i]))[2:].zfill(8)

    #print(b)

    def drop(b,m):
        return(b[:m]+b[(m+1):])

    def shift(b, i):
        return(b[i:] + b[:i])

    l = len(b)
    i = 1
    while(i<l):
        m = l%i
        b = drop(b,m)
        b = shift(b,i)
        l = len(b)
        i+=1

    #print("Compressed data: ",b)
    return b

def crack(rainbow_table):
    combinations = list(itertools.combinations(rainbow_table, 6))
    print('Running through combinations...')
    for combo in combinations:
        c = compress(''.join(combo))
        if c == '100001000100110000000100':
            print(combo)

if __name__ == '__main__':
    crack('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_#$@')


"""
INPUT: test
BINARY: 01110100 01100101 01110011 01110100
OUTPUT: 0010     0100     1110     0111

CONDENSED: 01110100011001010111001101110100
CONDENSED: 0010010011100111

OUTPUT:
Compressed data:
1000 0100 0100 1100 0000 0100


#SHA-256 of the complete
#flag is:
#e67753ef818688790288702b0592a46c390b695a732e1b9fec47a14e2f6f25ae
"""
