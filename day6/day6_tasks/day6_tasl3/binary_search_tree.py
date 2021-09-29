class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data

    # Insert method to create nodes
    def insert(self, data):
        if self.val is not None:
            if self.val < data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            elif self.val > data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                self.val = data
    
    # Search item in a tree
    def search_item(self, item):
        if self.val == item:
            print("Item is found!")
            return
        if self.val < item:
            if self.right:
                self.right.search_item(item)
            else:
                print("Item is not present in tree!")
        else:
            if self.left:
                self.left.search_item(item)
            else:
                print("Item is not present in tree!")

    # Search and return the min
    def get_min(self):
        while self.left:
            self = self.left
        return self.val

        # Search and return the min
    def get_max(self):
        while self.right:
            self = self.right
        return self.val
            
    # Print Method,  in-order traversal
    def print_tree(self):
        if self.left is not None:
            self.left.print_tree()
        print(self.val, end=" ")
        if self.right is not None:
            self.right.print_tree()

if __name__ == "__main__":
    a = Node(8)

    a.insert(3)
    a.insert(10)
    a.insert(6)
    a.insert(1)
    a.insert(4)
    a.insert(7)
    a.insert(14)
    a.insert(13)

    print("Search item 6 in the tree:", end=" ")
    a.search_item(1)

    print("Printing the tree:")
    a.print_tree()
    print()

    print("Printing the min node in the tree:", end=" ")
    print(a.get_min())

    print("Printing the min node in the tree:", end=" ")
    print(a.get_max())