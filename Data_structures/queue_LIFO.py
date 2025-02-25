import sys

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self):
        item = input("Enter item: ")
        self.queue.append(item)
        print(f"{item} enqueued to queue")

    def dequeue(self):
        if self.is_empty():
            print("dequeue from empty queue")
            return
        print("Element dequed is :", self.queue.pop(0))

    def peek(self):
        if self.is_empty():
            print("Empty queue")
            return
        print("peeked element :", self.queue[0])

    def size(self):
        print("Size = ", len(self.queue))
    
    def display(self):
        if self.is_empty():
            print("Empty queue")
            return
        print(self.queue)
    
class Menu:
    def __init__(self):
        pass
    def get_menu(self, queue):
        menu = {
            1 : queue.enqueue,
            2 : queue.dequeue,  
            3 : queue.peek,
            4 : queue.size,
            5 : queue.display,
            6 : self.eop
        }
        return menu
    def eop(self):
        print("Exiting program")
        sys.exit()
    def invalid_choice(self):
        print("Invalid choice")
    def run_menu(self):
        queue = Queue()
        while True:
            print("\n----- MENU -----")
            print("1. Enqueue Element")
            print("2. Dequeue Element")
            print("3. Peek Element")
            print("4. Size of Queue")
            print("5. Display Queue")
            print("6. Exit")
            choice = int(input("\nEnter choice: "))
            menu = self.get_menu(queue)
            menu.get(choice, self.invalid_choice)()

m = Menu()
m.run_menu()
