class Node:
    def __init__(self, data=0):
        self.val = data
        self.link = None

class List:
    def __init__(self):
        self.head = None
        
    def add_front(self, data):
        nd = Node(data)
        nd.link = self.head
        self.head = nd
        
    def is_merged(self, l1, l2):
        i = l1.head
        j = l2.head
        while i is not None and j is not None:
            if i == j:
                return "YES"
            i = i.link
            j = j.link
        return "NO"
    
    def disp(self):
        i = self.head
        while i is not None:
            print(i.val, end=" -> " if i.link else "\n")
            i = i.link

l1 = List()
l2 = List()

l1.add_front(6)
l1.add_front(5)
l1.add_front(4)
l1.add_front(3)
l1.add_front(2)
l1.add_front(1)

l2.add_front(9)
l2.add_front(8)
l2.add_front(7)

l2.head.link.link.link = l1.head.link.link.link

print("List 1 : ", end="")
l1.disp()
print("List 2 : ", end="")
l2.disp()

print("\nAre the lists merged?")
print(l1.is_merged(l1, l2))
