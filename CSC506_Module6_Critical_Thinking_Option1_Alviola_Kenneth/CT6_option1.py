def balanced_tree(array_nums):
    '''creates a balanced tree from a sorted array and returns the tree'''
    if not array_nums:
        return None
    root = len(array_nums)//2
    node = Node(array_nums[root])
    node.left = balanced_tree(array_nums[:root])
    node.right = balanced_tree(array_nums[root+1:])
    return node

def create_list(tree, templist=[]):
    '''creates a list from a binary tree'''
    
    items = []
    queue = [tree]

    while queue:
        copy = queue[:]
        queue = []

        for item in copy:
            if item is None:
                items.append(None)
                queue.append(None)
                queue.append(None)
            else:
                items.append(item.key)
                queue.append(item.left)
                queue.append(item.right)

        if all((x is None for x in queue)):
            break

    return items

def initialize_tree(num_list):
    '''creates balanced tree object and list to insert nodes'''
    num_list = sorted(num_list)
    tree = BinarySearchTree()
    btree = balanced_tree(num_list)
    ordered_list = create_list(btree)
    return tree, ordered_list

class Node:
    def __init__(self,x):
        self.key = x
        self.left = None
        self.right = None
        self.parent = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, key):
        x = self.root
        while x != None and x.key != key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def insert(self, z):
        x = self.root
        y = None
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self.root = z
        else:
            if z.key < y.key:
                y.left = z
            else:
                y.right = z

    def delete(self, z):
        if z.left == None and z.right == None:
            if z == self.root:
                self.root = None
            else:
                if z == z.parent.left:
                    z.parent.left = None
                else:
                    z.parent.right = None
        elif z.left != None and z.right != None:
            y = self.bstMinimum(z.right)
            z.key = y.key
            self.delete(y)
        else:
            if z.left != None:
                z.left.parent = z.parent
                if z == self.root:
                    self.root = z.left
                else:
                    if z == z.parent.left:
                        z.parent.left = z.left
                    else:
                        z.parent.right = z.left
            else:
                z.right.parent = z.parent
                if z == self.root:
                    self.root = z.right
                else:
                    if z == z.parent.left:
                        z.parent.left = z.left
                    else:
                        z.parent.right = z.left

    def bstMinimum(self, x):
        while x.left != None:
            x = x.left
        return x
    
    def build_tree(self,ordered_list):
        for num in ordered_list:
            self.insert(Node(num))

    def bstGetRoot(self):
        return self.root
    
    
    def print_tree(self, root, val="key", left="left", right="right"):
        def display(root, val=val, left=left, right=right):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if getattr(root, right) is None and getattr(root, left) is None:
                line = '%s' % getattr(root, val)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if getattr(root, right) is None:
                lines, n, p, x = display(getattr(root, left))
                s = '%s' % getattr(root, val)
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if getattr(root, left) is None:
                lines, n, p, x = display(getattr(root, right))
                s = '%s' % getattr(root, val)
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display(getattr(root, left))
            right, m, q, y = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * \
                '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + \
                (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + \
                [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        lines, *_ = display(root, val, left, right)
        for line in lines:
            print(line)