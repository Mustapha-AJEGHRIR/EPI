import random as  rd


#Linked lists
class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next
    
    def print(self):
        node = self
        if type(self).__name__ == "Head":
            print("#", end= " --> ")
            node = self.next
        print(node.data, end = ' --> ')
        node = node.next
        while node.__class__ != Last :
            print(node.data, end = ' --> ')
            node = node.next
        print("X")

class Head(Node):
    def __init__(self, next=None) -> None:
        super().__init__(None, next=next)

class Last(Node):
    def __init__(self) -> None:
        super().__init__(None, next=None)
    
def list_search(node : Node, key) -> Node:
    while node.__class__ !="Last" and node!=key:
       node = node.next
    return node

def insert_after(node : Node, new_node: Node) -> None:
    new_node.next = node.next
    node.next = new_node

def delete_after(node : Node) -> None:
    if node.next.__class__ != "Last":
        node.next = node.next.next


def make_linked_list(L: list):
    if len(L) == 0:
        return Last()
    node = Last()
    L_r = reversed(L)
    for data in L_r :
        node = Node(data, node)
    final_node = Head(node)
    return final_node

def list_generation(n : int, min = 0, max = 100) -> list[int] :
    '''
    Generates a random list of integers of length n
    
    n : the length of the list
    min : minimum value possible (included)
    max : the maximum value possible (included)
    '''
    L = []
    for _ in range(n):
        L.append(rd.randint(min, max))
    L.sort()
    return L


if __name__ == '__main__' :
    L = input("Enter some words separated by speces : ").split()
    linked_list = make_linked_list(L).print()