class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Insert method to create nodes
    def insert(self, data):
        if self.data is not None:
            if self.data < data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif self.data > data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data
    
    def search_item(self, item):
        if self is None or self.data == item:
            return True

        if self.data < item:
            return self.right.search_item(item)
    
        return self.left.search_item(item)

    # Print Method,  in-order traversal
    def print_tree(self):
        if self.left is not None:
            self.left.print_tree()
        print(self.data)
        if self.right is not None:
            self.right.print_tree()

if __name__ == "__main__":
    a = Node(8)

    a.insert(3)
    a.insert(10)
    a.insert(6)
    a.insert(1)
    a.insert(14)

    print("Search item 6 in the tree")
    print(a.search_item(6))
    a.print_tree()

    