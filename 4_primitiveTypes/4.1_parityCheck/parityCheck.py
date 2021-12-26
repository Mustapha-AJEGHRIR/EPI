import random as rd
from time import time
def parity(n: int) -> bool:
    return sum(map(int,format(n, 'b')))%2

def parity2(n: int) -> bool:
    p = 0
    while n :
        p = (n) ^ p
        n >>=1
    return p % 2

def parity3(n : int) -> bool :
    n ^= n >> 32
    n ^= n >> 16
    n ^= n >> 8
    n ^= n >> 4
    n ^= n >> 2
    n ^= n >> 1
    return n & 0x1


if __name__== '__main__':

    L = []
    for _ in range(100000):
        L.append(rd.randrange(2**64 -1))
    
    start = time()
    for x in L:
        parity(x)
    print("For 1 : ", time() - start)

    start = time()
    for x in L:
        parity2(x)
    print("For 2 : ", time() - start)
    
    start = time()
    for x in L:
        parity3(x)
    print("For 3 : ", time() - start)


    try :
        n = int(input("Parity check for : "))
        p = parity(n)
        print( "First : "  + ("not pair !" if p else "pair !") )
        p2 = parity2(n)
        print( "Second : " + ("not pair !" if p2 else "pair !") )
        p3 = parity3(n)
        print( "Third : " + ("not pair !" if p3 else "pair !") )
    except (ValueError):
        print("Please enter a valid number !")
        raise ValueError("You should enter a valid integer value")
    