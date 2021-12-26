from linkedLists import *


def list_reverse(M, s, f):
    if f <= s :
        return M
    f = f-1
    print("Before reverse : ", end ="")
    M.print()
    tail = M
    begin_before = Node(None, tail) #element before the start of the reverse
    begin_after = Node(None) #element after the start of the reverse
    end = Node(None) #last element of reversing
    i = 1
    X = tail
    Y = tail.next
    while X :
        if i >= s and i <= f:
            if i == s :
                begin_after = X
            if i <= f :
                end = X

                Y_next = Y.next
                Y.next = X
                X = Y
                Y = Y_next
        elif i>f:
            break
        else :
            begin_before = X
            X = Y
            Y = Y.next
        i += 1
    begin_before.next = X
    begin_after.next = Y
    print("After reverse : ", end = "")
    return M if s>1 else X


if __name__ == "__main__" :
    n = int(input("Input the length of the Main list : "))
    s = int(input("Input the start of the reverse : "))
    f = int(input("Input the end of the reverse : "))

    M = make_linked_list(list_generation(n))
    
    list_reverse(M, s, f).print()