import sys

class Node:
    def __init__(self, data = 0):
        self.left = None
        self.data = data
        self.right = None
        #print(f'Node with data {data} created')

class Bst:
    def __init__(self):
        self.root = None
        print('BST Created !!')

    def create_bst(self):
        data_list = list(map(int, input('Enter data values :').split()))
        
        for data in data_list:
            node = Node(data)
            
            if self.root is None:
                self.root = node
                continue
            
            temp1 = self.root
            temp2 = None
            
            while temp1 != None:
                temp2 = temp1
                if data < temp1.data:
                    temp1 = temp1.left
                else:
                    temp1 = temp1.right
                    
            if data < temp2.data:
                temp2.left = node
            else:
                temp2.right = node

    def del_node(self, root):
        if self.root is None:
            print('Tree is empty')
            return  
        
        data = int(input('Enter data to be deleted: '))
        
        tmp1 = self.root
        tmp2 = None
        while tmp1 != None:
            if tmp1.data == data:
                break
            tmp2 = tmp1
            if data < tmp1.data:
                tmp1 = tmp1.left
            else:
                tmp1 = tmp1.right
            
        if tmp1.left is None and tmp1.right is None:
            if tmp1 == self.root:
                self.root = None
            elif tmp2.left == tmp1:
                tmp2.left = None
            else:
                tmp2.right = None
            return
        
        if tmp1.left is None or tmp1.right is None:
            child = tmp1.left if tmp1.left is not None else tmp1.right
            if tmp1 == self.root:
                self.root = child
            elif tmp2.left == tmp1:
                tmp2.left = child
            else:
                tmp2.right = child
            return
        
        if tmp1.left and tmp1.right:
            tmp3 = tmp1
            tmp2 = tmp1.right
            while tmp2.left is not None:
                tmp1 = tmp2
                tmp2 = tmp2.left
            tmp3.data = tmp2.data
            if tmp1.left == tmp2:
                tmp1.left = tmp2.right
            else:
                tmp3.right = tmp2.right
            return

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=' ')            

    def search_node(self):
        if self.root is None:
            print('Tree is empty')
            return
        data = int(input('Enter data to be searched: '))
        temp = self.root
        level = 1
        while temp != None:
            if temp.data == data:
                print(f'Node with data {data} found at level {level}')
                return
            if data < temp.data:
                temp = temp.left
            else:
                temp = temp.right
            level += 1
        print(f'Node with data {data} not found')

class Menu:
    def invalid_choice(self):
        print('Invalid choice entered')
    
    def end_of_program(self):
        sys.exit('End of Program')

    def match_user_choice(self, choice, bst):
        match choice:
            case 1 : 
                bst.create_bst()
            case 2 : 
                if bst.root is None:
                    print('Tree is empty')
                else:
                    bst.del_node(bst.root)
            case 3 :
                if bst.root is None:
                    print('Tree is empty')
                else:
                    bst.inorder(bst.root)
            case 4 :
                if bst.root is None:
                    print('Tree is empty')
                else:
                    bst.preorder(bst.root)
            case 5 :
                if bst.root is None:
                    print('Tree is empty')
                else:
                    bst.postorder(bst.root)
            case 6 :
                if bst.root is None:
                    print('Tree is empty')
                else:
                    bst.search_node()
            case 7 :
                self.end_of_program()
            case _ :
                self.invalid_choice()

    def run_menu(self):
        bst = Bst()
        while True:
            print("\n----- MENU -----")
            print("1. Create BST")
            print("2. Delete Node")
            print("3. Inorder")
            print("4. Preorder")
            print("5. Postorder")
            print("6. Search Node")
            print("7. Exit")
            
            choice = int(input("\nEnter choice: "))
            self.match_user_choice(choice, bst)

def start_app():
    menu = Menu()
    menu.run_menu()

start_app()