import random as  rd

#Linked lists
class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next
    
    def print(self):
        print(self.data, end = ' --> ')
        node = self.next
        while node :
            print(node.data, end = ' --> ')
            node = node.next
        print("X")
    
def list_search(node : Node, key) -> Node:
    while node!=None and node!=key:
       node = node.next
    return node

def insert_after(node : Node, new_node: Node) -> None:
    new_node.next = node.next
    node.next = new_node

def delete_after(node : Node) -> None:
    if node.next != None:
        node.next = node.next.next


def make_linked_list(L: list):
    if len(L) == 0:
        return Node(None)
    node = Node(L.pop())
    L_r = reversed(L)
    for data in L_r :
        node = Node(data, node)
    return node

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