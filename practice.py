# set = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
# print("\nSet with the use of mixed values")
# print(set)
# Tuple = ('Geeks', 'for')
# print("\nTuple with the use of strings")
# print(Tuple)

# List1 = [1, 2, 3, 4, 5, 6]
# print("\nTuple using List")
# Tuple = tuple(List1)
# print(Tuple)
# print(Tuple[0])
# print(Tuple[-1])
# print(Tuple[-3])

# print("\nElements of a set")
# for i in set:
    # print(i, end=" ")
# print()
# print("Geeks" in set)


# normal_set = set(["a","b", "c"])

# print("Normal set")
# print(normal_set)

# frozen_set = frozenset(["e", "f", "g"])

# print("\nfrozen set")
# print(frozen_set)

# string = " Welcome to GeeksForGeeks"
# print("Creating string:")
# print(string)

# Dict = {'Name': 'Geeks', 1:[1, 2, 3, 4]}
# print("creating Dictionary: ")
# print(Dict)
# print(Dict['Name'])
# print(Dict.get(1))
# myDict = {x: x**2 for x in [1,2,3,4,5]}
# print(myDict)

# import numpy as np

# a = np.array([[1,2,3,4],[4,55,1,2],
            #    [8,3,20,19],[11,2,22,21]])
# m = np.reshape(a,(4, 4))
# print(m)

"""bYTEARRAY"""
# a = bytearray((12, 8, 25, 2))
# print("creating Bytearray:")
# print(a)

# print("\nAccessing elements:", a[1])
# a[1] = 3
# print("\nAfter Modifying:")
# print(a)

# a.append(30)
# print("\nAfter Adding Element:")
# print(a)
# print(a[4])

""" Linked list """
# Defining the linked list
# Node class
class Node:
    # function to initialize the  node object
    def __init__(self, data):
        self.data = data  #assign data
        self.next = None  # initialiize next as null

# Linked list class
# class LinkedList:

    # Function to initialize head
    # def __init__(self):
        # self.head = None

    """ Let us traverse the created list and print the data of 
    each node. For traversal, let us write a general-purpose
      function printList() that prints any given list."""
    # This function prints contents of linked list
    # starting from head
    # def printList(self):  # this is linked list Traversal
        # temp = self.head
        # while (temp):
            # print(temp.data)
            # temp = temp.next

# Code execution starts here
# if __name__ == '__main__':

    #start with the empty list
    # llist = LinkedList()

    # llist.head = Node(1)
    # second = Node(2)
    # third = Node(3)

    # llist.head.next = second; # Link first node with second
    # second.next = third ;   # Link second node with the third node

# llist.printList()

""" STACK"""

# stack = []

# stack.append('g')
# stack.append('f')
# stack.append('g')

# print('Initial stack')
# print(stack)

# print("\nElements popped from stack:")
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# print("\nStack after Elements are popped:")
# print(stack)

""" QUEUE"""

# queue = []

# queue.append('g')
# queue.append('f')
# queue.append('g')

# print('Initial queue')
# print(queue)

# print("\nElements dequeued from queue")
# print(queue.pop(0))
# print(queue.pop(0))
# print(queue.pop(0))

# print("\nqueue after removing elements")
# print(queue)

""" PRIORTY QUEUE """

# class PriorityQueue(object):
    # def __init__(self):
        # self.queue = []

    # def __str__(self): 
        # return ' '.join([str(i)for i in self.queue])
    
    # for checking if the queue is empty
    # def isEmpty(self):
        # return len(self.queue) == 0
    
    # for inserting an element in the queue
    # def insert(self, data):
        # self.queue.append(data)

    # for popping an element based on priorty
    # def delete(self):
        # try:
            # max = 0
            # for i in range(len(self.queue)):
                # if self.queue[i] > self.queue[max]:
                    # max = 1
            # item = self.queue[max]
            # del self.queue[max]
            # return item
        # except IndexError:
            # print()
            # exit()

# if __name__ == '__main__':
    # myQueue = PriorityQueue()
    # myQueue.insert(12) 
    # myQueue.insert(1)
    # myQueue.insert(14)
    # myQueue.insert(7)
    # print(myQueue)
    # while not myQueue.isEmpty():
        # print(myQueue.delete())

""" HEAP """
# import heapq

# li = [5, 7, 9, 1, 3]
# heapq.heapify(li)

# print("The createdheap is : " , end="")
# print(list(li))

# heapq.heappush(li,4)

# print("The modified heap after push is : ",end="")
# print(list(li))

# print("The popped and smallest element is : ",end="")
# print(heapq.heappop(li))

""" Binary tree"""
# A Python class that represents an individual node
# in a Binary Tree
# class Node:
    # def __init__(self, key):
        # self.left = None
        # self.right = None
        # self.val = key

# create root
# root = Node(1)
# root.left = Node(2);
# root.right = Node(3);
# root.left.left = Node(4);

""" Tree traversal"""

# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

# Afunction to do inorder tree traversal
def printInorder(root):


    if root:

        # first recur on left child
        printInorder(root.left)

        # the print data of the node
        print(root.val),

        # now recur on right child
        printInorder(root.right)

# function to do postorder tree traversal
def printPostorder(root):

    if root:

        # first recur on the left child
        printPostorder(root.left)

        # then recur on the right child
        printPostorder(root.right)

        # now print the data of the node
        print(root.val),

def printpreorder(root):

    if root:

        # first print the data of the node
        print(root.val),

        # then recur on the left child
        printpreorder(root.left)

        # finally recur on the right child
        printpreorder(root.right)

# driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Preorder traversal of binary tree is")
printpreorder(root)

print("\nInorder traversal of binary tree is ")
printInorder(root)

print("\nPostordertraversal of binary tree is")
printPostorder(root)










    
    
    
        
        




    
        
   