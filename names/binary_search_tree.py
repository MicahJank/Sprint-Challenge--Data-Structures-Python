"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
# import sys
# # sys.path.append('../queue')
# from queue import Queue

# sys.path.append('../stack')
# from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # node_to_add = BSTNode(value)
        # current_node = self

        # go right
        if value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                node_to_add = BSTNode(value)
                self.right = node_to_add

        # go left
        else:
            if self.left is not None:
                self.left.insert(value)
            else:
                node_to_add = BSTNode(value)
                self.left = node_to_add

        # Traverse Right
        # if value >= self.value:
        #     while current_node.right is not None or value < current_node.value:
        #         if value >= current_node.value:
        #             current_node = current_node.right
        #         else:
        #             while current_node.left is not None or value >= current_node.value:
        #                 if value < current_node.value:    
        #                     current_node = current_node.left
        #                 else:
        #                     break
        #             else:
        #                 current_node.left = node_to_add
        #                 break
        #     else:
        #         current_node.right = node_to_add

            
        # # Traverse left
        # else:
        #     while current_node.left is not None or value >= current_node.value:
        #         if value < current_node.value:
        #             current_node = current_node.left
        #         else:
        #             while current_node.right is not None or value < current_node.value:
        #                 if value >= current_node.value:    
        #                     current_node = current_node.right
        #                 else:
        #                     break
        #             else:
        #                 current_node.right = node_to_add
        #                 break
        #     else:
        #         current_node.left = node_to_add

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False
        else:
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False

        # current_node = self

        # while current_node.value != target:
        #     if target > current_node.value and current_node.right is not None:
        #         current_node = current_node.right
        #     elif target < current_node.value and current_node.left is not None:
        #         current_node = current_node.left
        #     else:
        #         return False
        # else:
        #     return True


    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self

        while current_node.right is not None:
            current_node = current_node.right
        
        return current_node.value



    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value) # - pre order if the function runs first
        if self.left is not None:
            self.left.for_each(fn)
            # fn(self.value) # - in order if the function runs left first and then goes right
        
        if self.right:
            self.right.for_each(fn)
            # fn(self.value) # - post order if the function runs right first and then goes left


    # Stack Traversal - DFT - Depth First Traversal
    # As long as stack is not empty keep popping off the node and checking children and adding
    # them to the stack until you have traversed all nodes

    # Queue Traversal - BFT - Breadth First Traversal
    # As long as the queue is not empty keep dequeuing the node and check the children and add
    # them to the queue until you have traversed all nodes

    # Part 2 -----------------------


    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left is not None:
            node.left.in_order_print(node.left)
            print(node.value)
        else:
            print(node.value)
        
        if node.right is not None:
            node.right.in_order_print(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     # make a queue
    #     queue = Queue()
    #     # enqueue the node
    #     queue.enqueue(node)
    #     # as long as the queue is not empty
    #     while len(queue) > 0:
    #         # dequeue from the front of the queue, this is the current node
    #         current_node = queue.dequeue()
    #         # check that the kids are not None
    #         if current_node.left is not None:
    #             # enqueue the kids of the current node on the queue
    #             queue.enqueue(current_node.left)

    #         if current_node.right is not None:
    #             queue.enqueue(current_node.right)

    #         print(current_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # def dft_print(self, node):
    #     # make a stack
    #     stack = Stack()
    #     # push the node on the stack
    #     stack.push(node)
    #     # as long as the stack is not empty
    #     while len(stack) > 0:
    #         # pop off the stack, this is our current node
    #         current_node = stack.pop()

    #         # check that the kids are not None
    #         if current_node.right is not None:
    #             stack.push(current_node.right)

    #         if current_node.left is not None:
    #             # put the kids of the current node on the stack
    #             stack.push(current_node.left)
            
    #         print(current_node.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left is not None:
            node.pre_order_dft(node.left)

        if node.right is not None:
            node.pre_order_dft(node.right)
        

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left is not None:
            node.left.post_order_dft(node.left)
        
        if node.right is not None:
            node.right.post_order_dft(node.right)
            print(node.value)
        else:
            print(node.value)
