from collections import deque

class Node:
    def __init__(self,key):
        self.key = key
        self.right = None
        self.left = None

    

    def insert(self,value):
        if not self.key:
            self.key = Node(value)
        
        if value < self.key:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)


    def level_order(self,root):
        res = []
        q = deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node =  q.popleft()
                if node :
                    level.append(node.key)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res




if __name__ == "__main__":
    x = None

    while True:
        print("""
        1. Insert value to the root node
        2. Insert more values
        3. To find the level order of the tree
        4. Quit
        """)

        try:
            print("Enter the option:")
            option = int(input())

            if option == 1:
                value = int(input("Enter the value: "))
                x = Node(value)
                print("Root node created with value:", value)

            elif option == 2:
                if x is None:
                    print("Please create a root node first (Option 1).")
                else:
                    value = int(input("Enter the value: "))
                    x.insert(value)
                    print("Value inserted.")

            elif option == 3:
                if x is None:
                    print("Please create a root node first (Option 1).")
                else:
                    result = x.level_order(x)
                    print("Level order of the tree:", result)

            elif option == 4:
                print("Exiting the program.")
                break

            else:
                print("Invalid option. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a valid option or value.")