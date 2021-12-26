
BIT_MASK = 0xF
MASK_SIZE = len( format(BIT_MASK, "b") )


def closest(x):
    assert( 64 % MASK_SIZE == 0)
    for bit_set in range(64 // MASK_SIZE):
        

        return 0


def forced_closest(x):
    word = ""
    bit_word = format(x, '064b')
    word_len = len(bit_word)
    #Find the first one
    one = 0
    zero = 0
    for i in range(word_len):
        if bit_word[-1-i] == "1":
            one = word_len - 1 - i
            break
    if one < word_len -1 :
        #Take the zero on the right
        zero = one + 1
    else : #We started with one
        #Find the first zero
        for i in range(word_len):
            if bit_word[-1-i] == "0":
                zero = word_len - 1 - i
                break
        one = zero + 1 #Take the one in the right of the zero
    return x - 2**(word_len -1 - one) + 2**(word_len -1 - zero)



def lookup_cache():
    L = []
    for i in range(BIT_MASK + 1):
        L.append(forced_closest(i))
    return L

if __name__ == "__main__" :
    # cache_closet = lookup_cache()
    x = int(input("Enter a number an integer : "))
    print("Forced closest : ", forced_closest(x))