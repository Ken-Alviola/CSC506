from random_word import RandomWords
import random

def wordlist_25k():
    count = 0
    random_wordlist = []
    while count < 500:
        random_wordlist += r.get_random_words()
        count += 1
        if count % 10 == 0:
            print(count)
    return random_wordlist

stack = []
#prepends the list to form a stack
while len(stack) < 25000:
    stack.insert(0,random.sample(random_wordlist,1)[0])
    
#pops top item
while len(stack) > 0:
    stack.pop()

count = 0
while count < 25000:
    stack.insert(0,random.sample(random_wordlist,1)[0])
    stack.pop()
    count += 1
    
queue = []
#appends the list to form a queue
while len(queue) < 25000:
    queue.append(random.sample(random_wordlist,1)[0])
    
#dequeues item from front of queue
while len(queue) > 0:
    queue.pop()
#appends list then pops for 200 iterations
count = 0
while count < 25000:
    queue.append(random.sample(random_wordlist,1)[0])
    queue.pop()
    count += 1
    
'''Python supports automatic garbage collection so deallocation of memory
is done implicitly. However to force it to deallocate each node after use,
add the following code:

	import gc		 #added at the start of program
	gc.collect()	 #to be added wherever memory is to be deallocated
'''


class Node:

    # Class to create nodes of linked list
    # constructor initializes node automatically
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    # head is default NULL
    def __init__(self):
        self.head = None

    # Checks if stack is empty
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    # Method to add data to the stack
    # adds to the start of the stack
    def push(self, data):

        if self.head == None:
            self.head = Node(data)

        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    # Remove element that is the current head (start of the stack)
    def pop(self):

        if self.isempty():
            return None

        else:
            # Removes the head node and makes
            # the preceding one the new head
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    # Returns the head node data
    def peek(self):

        if self.isempty():
            return None

        else:
            return self.head.data

    # Prints out the stack
    def display(self):

        iternode = self.head
        if self.isempty():
            print("Stack Underflow")

        else:

            while(iternode != None):

                print(iternode.data, "->", end=" ")
                iternode = iternode.next
            return
        
LL_stack = Stack()        
count = 0
while count < 25000:
    LL_stack.push(random.sample(random_wordlist,1)[0])
    count += 1

while LL_stack.isempty() != True:
    LL_stack.pop()
    
count = 0
while count < 25000:
    LL_stack.push(random.sample(random_wordlist,1)[0])
    LL_stack.pop()
    count += 1
    
# Python3 program to demonstrate linked list
# based implementation of queue

# A linked list (LL) node
# to store a queue entry
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

# A class to represent a queue

# The queue, front stores the front node
# of LL and rear stores the last node of LL


class Queue:

    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    # Method to add an item to the queue
    def EnQueue(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    # Method to remove an item from queue
    def DeQueue(self):

        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next

        if(self.front == None):
            self.rear = None

LL_queue = Queue()
count = 0
while count < 25000:
    LL_queue.EnQueue(random.sample(random_wordlist,1)[0])
    count += 1

while LL_stack.isempty() != True:
    LL_queue.DeQueue()
    
count = 0
while count < 25000:
    LL_queue.EnQueue(random.sample(random_wordlist,1)[0])
    LL_queue.DeQueue()
    count += 1