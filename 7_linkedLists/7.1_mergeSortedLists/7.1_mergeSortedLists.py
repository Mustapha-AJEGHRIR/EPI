from linkedLists import *


def merge_lists(A : Node, B : Node) -> Node:
    c_head = Head()
    C = c_head
    A, B = A.next, B.next 
    while A.__class__ != Last or B.__class__ != Last :
        if A.__class__ == Last : 
            C.next = B
            C = C.next
            break
        if B.__class__ == Last : 
            C.next = A
            C = C.next
            break

        if A.data <= B.data :
            C.next = A
            A = A.next
            C = C.next
        else :
            C.next = B
            B = B.next
            C = C.next
    C.next = Last()
    return c_head



if __name__ == "__main__":
    n = int(input("Give a the length of the first list : "))
    m = int(input("Give a the length of the second list : "))

    A = make_linked_list(list_generation(n))
    B = make_linked_list(list_generation(m))

    merge_lists(A,B).print()