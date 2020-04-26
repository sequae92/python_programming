# Linked List Traversal

class Node:
  def __init__(self,value):
    self.data = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = Node(None)
  
  def print_list(self):
    temp = self.head
    while(temp):
      print("The value is {}".format(temp.data))
      temp = temp.next

if __name__ == "__main__":
  llist = LinkedList()

  llist.head = Node(1)
  second = Node(2)
  third = Node(3)
  fourth = Node(4)

  llist.head.next = second
  second.next = third
  third.next = fourth

  #Print all the elements of teh linekd list
  llist.print_list()
