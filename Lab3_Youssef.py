'''
Jack Youssef
2/7/23
CS 242
Lab 3 (option 1)

Includes a makeTwoWay function that takes a singly linked structure as its argument
and returns a doubly linked list that contains the same items and structure.

Also includes the Node and TwoWayNode classes.
''' 


# Define a function makeTwoWay that expects a singly linked structure as its argument. The
# function builds and returns a doubly linked structure that contains the items in the singly linked
# structure. (Note: The function should not alter the argument's structure.)
 
class Node(object):
    """ Represents a one-way Node. """
    def __init__(self, data, next = None):
        """ Instantiates a Node with default next of None. """
        self.data = data
        self.next = next
        
class TwoWayNode(Node):
    """ Represents a two-way Node. """
    def __init__(self, data, previous = None, next = None):
        """ Instantiates a Node with default next and previous of None. """
        Node.__init__(self, data, next)
        self.previous = previous

def makeTwoWay(single_head):
    """ Takes a singly linked list and returns a doubly linked list with the same items. """
    print('\n* making doubly......\n')

    new_list = None
    probe = single_head
    previous = single_head
    while probe != None:
        previous = previous.next
        new_list = TwoWayNode(probe.data, previous, new_list)
        probe = probe.next
    
    return new_list
    

def main():
    """ Driver: Tests makeTwoWay function. """
    
    # creating nodes
    node = None
    print('* creating nodes:\n')
    for count in range(1, 11):
        node = Node(count, node)
        print(node.data)
        
    # convert to doubly
    doubly_probe = makeTwoWay(node)
    
    # test doubly iteration
    print('* doubly iteration test:\n')
    print('data:', doubly_probe.data, ', previous: ', doubly_probe.previous, ', next:', doubly_probe.next.data)
    doubly_probe = doubly_probe.next
    while doubly_probe.next != None:
        print('data:', doubly_probe.data, ', previous: ', doubly_probe.previous.data, ', next:', doubly_probe.next.data)
        doubly_probe = doubly_probe.next
    print('data:', doubly_probe.data, ', previous: ', doubly_probe.previous.data, ', next:', doubly_probe.next)
  
    
if __name__ == '__main__':
    main()
    
    