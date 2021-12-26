from time import time
import random as rd


def reverse(x, L):
    mask_size = 16
    bit_mask = 0xFFFF
    p_3 = ( x >> 3*mask_size ) & bit_mask
    p_2 = ( x >> 2*mask_size ) & bit_mask 
    p_1 = ( x >> 1*mask_size ) & bit_mask
    p_0 = ( x >> 0*mask_size ) & bit_mask
    return (L[p_0] << 3*mask_size) | (L[p_1] << 2*mask_size) | (L[p_2] << 1*mask_size) | (L[p_3] << 0*mask_size)

def forced_reverse(x):
    word = ""
    bit_word = format(x, 'b')
    for i in range(64) :
        if i < len(bit_word):
            word += bit_word[-i - 1]
        else :
            word += "0"
    return int(word, 2)

def forced_reverse_16bit(x):
    word = ""
    bit_word = format(x, 'b')
    for i in range(16) :
        if i < len(bit_word):
            word += bit_word[-i - 1]
        else :
            word += "0"
    return int(word, 2)

def lookup():
    l = [0]* 2**16
    for i in range(2**16):
        l[i] = forced_reverse_16bit(i)
    return l


if __name__ == '__main__' :
    try:
        L = lookup()
        tests = []
        for i in range(10000):
            tests.append(rd.randrange(2**64))

        start = time()
        for x in tests:
            forced_reverse(x)
        print("Forced Reverse : ", time()-start)

        start = time()
        for x in tests:
            reverse(x,L)
        print("Lookup table : ", time()-start)

        print("Validity testing ...")
        for x in tests: 
            assert reverse(x,L) == forced_reverse(x), "Lookup reverse doesn't match forced reverse for " + str(x) + " !, we had forced = " + str(forced_reverse(x)) + " and other = " + str(reverse(x,L))
        print("Okey")

        x= int(input("Reverse the number : "))
        print("Its reverse is : ",reverse(x, L))
    except (ValueError):
        raise ValueError("Please enter a valid integer value")