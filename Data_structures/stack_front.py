import sys

class Stack:
    def __init__(self, sz=5):
        self.stk = []
        self.size = sz
        print("Stack created with size", sz)

    def push(self):
        if len(self.stk) == self.size:
            print("Stack is full")
            return
        else:
            ele = input("Enter element to push: ")
            self.stk.insert(0, ele)
            print("Element pushed successfully")

    def pop(self):
        if not self.stk:
            print("Stack is empty")
            return
        print("Element popped is", self.stk[0])
        del self.stk[0]
        
    def display(self):
        if not self.stk:
            print("Stack is empty")
            return
        print("Stack elements are", self.stk)

class Menu:
    def __init__(self):
        pass
    def get_menu(self, stack):
        menu = {
            1 : stack.push,
            2 : stack.pop,  
            3 : stack.display,
            4 : self.eop
        }
        return menu
    def eop(self):
        print("Exiting program")
        sys.exit()
    def invalid_choice(self):
        print("Invalid choice")
    def run_menu(self):
        stack = Stack()
        while True:
            print("\n----- MENU -----")
            print("1. Push Element")
            print("2. Pop Element")
            print("3. Display Stack")
            print("4. Exit")
            choice = int(input("\nEnter choice: "))
            menu = self.get_menu(stack)
            menu.get(choice, self.invalid_choice)()

m = Menu()
m.run_menu()
