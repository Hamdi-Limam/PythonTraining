##  Binary Search Tree (BST) and its functionality in python
We are going to see how we can code Binary Search Tree and its functionality in python. Binary search tree are binary tree where the left child is less than root and right child is greater than root. We will be performing insertion, searching, traversal, min and other functions. [Read more about them here](https://en.wikipedia.org/wiki/Binary_search_tree).
```
left_subtree (keys)  ≤  node (key)  ≤  right_subtree (keys)
```
Check full code in `day6_tasks/day6_task3/binary_search_tree.py`

### Creating the Node Class
Node class to make the nodes of binary search tree.
```
class Node():
   def __init__(self,data):
      self.left = None
      self.right = None
      self.data = data
```
### Inserting Nodes to the tree
The insert method, what this method is doing is checking if the data is lesser than node then moves to left child else moves to right child and place it at the end.
```
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
```
A new key is always inserted at the leaf. We start searching a key from the root until we hit a leaf node. Once a leaf node is found, the new node is added as a child of the leaf node. 
1. Start from the root. 
2. Compare the inserting element with root, if less than root, then recurse for left, else recurse for right. 
3. After reaching the end, just insert that node at left(if less than current) else right. 

### In Order Traversal algo
In this traversal method, the left subtree is visited first, then the root and later the right sub-tree. We should always remember that every node may represent a subtree itself. If a binary tree is traversed in-order, the output will produce sorted key values in an ascending order. **Inorder traversal of BST always produces sorted output**.

We can construct a BST with only Preorder or Postorder or Level Order traversal. Note that we can always get inorder traversal by sorting the only given traversal.
```
    # Print Method,  in-order traversal
    def print_tree(self):
        if self.left is not None:
            self.left.print_tree()
        print(self.data)
        if self.right is not None:
            self.right.print_tree()
```
Algorithm Inorder(tree):
1. Traverse the left subtree, i.e., call Inorder(left-subtree)
2. Visit the root.
3. Traverse the right subtree, i.e., call Inorder(right-subtree)

# Search item in the tree
```
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

```
Search algo:
1. Check if root value is equal to the item
2. Traverse the left subtree, if item is smaller than the root value
3. Traverse the right subtree, if item is bigger than the root value

## Delete node from a tree
There are three cases when deleting a node from a tree:
1. Node to be deleted is the leaf (0 child): simply remove from the tree
2. Node to be deleted has only one child: Copy the child to the node and delete the child
3. Node to be deleted has two children: find inorder successor of the node. Copy contents of the inorder successor to the node and delete the inorder successor. Note that inorder predecessor can also be used. 

The important thing to note is, inorder successor is needed only when the right child is not empty. In this particular case, inorder successor can be obtained by **finding the minimum value in the right child of the node**.

Check code of the file `binary_search_tree.py`

