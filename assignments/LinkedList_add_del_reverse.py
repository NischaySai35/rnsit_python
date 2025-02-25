class Node:
    def __init__(self, data=0):
        self.val = data
        self.link = None

class List:
    def __init__(self):
        self.head = None
    
    # front addition
    def add_front(self, data):
        nd = Node(data)
        nd.link = self.head
        self.head = nd

    # insert at position
    def insert_at_pos(self, data, pos):
        nd = Node(data)
        if pos == 0:
            nd.link = self.head
            self.head = nd
            return

        prv = self.head
        for i in range(pos-1):
            if prv == None:
                print("Position unavailable")
                return
            prv = prv.link

        nd.link = prv.link
        prv.link = nd
        print("Element inserted")

    # delete at position
    def delete_at_pos(self, pos):
        if self.head is None:
            print("Empty")

        if pos == 0:
            self.head = self.head.link

        tmp = self.head
        for i in range(pos):
            prv = tmp
            if tmp == None:
                print("Position unavailable")
                return
            tmp = tmp.link

        prv.link = tmp.link
        print("Element deleted")
    # diplay the list
    def disp(self):
        i = self.head
        while i is not None:
            if i.link is None:
                print(i.val)
                break
            print(i.val, end=" -> ")
            i = i.link

    # reverse the list
    def rev_list(self):
        i = self.head.link
        tmp = self.head
        while i is not None:
            self.add_front(i.val)
            i = i.link
        tmp.link = None
        print("List reversed")
            
ll = List()
ll.add_front(6)
ll.add_front(5)
ll.add_front(3)
ll.add_front(2)
ll.add_front(1)

ll.insert_at_pos(4,3)

ll.disp()

ll.insert_at_pos(145,2)

ll.disp()

ll.delete_at_pos(2)

ll.disp()

ll.rev_list()

ll.disp()

