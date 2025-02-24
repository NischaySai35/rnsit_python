class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None
        print('An empty List is created')

    def create_node(self):
        data = input('Enter data of the new node: ')
        node = Node(data)
        return node

    def add_node(self):
        position = int(input('Enter position of the new node: '))
        if self.head is None:
            if position == 1:
                self.head = self.create_node()
                return
            else:
                print('Invalid Position')
        temp = self.head
        temp2 = None
        i = 1
        while temp.link is not None and i < position:
            temp2 = temp
            temp = temp.link
            i += 1
        if temp.link is None:
            if position == i+1:
                temp.link = self.create_node()
            else:
                print('Invalid Position')
            return
        new_node = self.create_node()
        new_node = temp2.link
        temp2.link = new_node

    def delete_node(self):
        if self.head is None:
            print('List is empty')
            return
        position = int(input('Enter position of the node to delete: '))
        if position == 1:
            print(f'Node with data {self.head.data} is deleted')
            self.head = self.head.link
            return
        if self.head.link is None and position != 1:
            print('Invalid Position')
            return
        temp = self.head
        i = 1
        while temp.link.link is not None and i < position:
            temp = temp.link
            i += 1
        # Check if last node to be deleted
        if temp.link.link is None:
            if i == position: # check once more
                print(f'Node with data {temp.link.data} is deleted')
                temp.link = None
            else: # Check if last node reached but not the position
                print('Invalid Position')
            return
        # Delete the in between node
        print(f'Node with data {temp.link.data} is deleted')
        temp.link = temp.link.link

    def display_list(self, head):
        if head is not None:
            self.display_list(head.link)
            print(head.data, end=' ')
