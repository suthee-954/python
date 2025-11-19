class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

head = None

def insert():
  global head # Declare head as global
  data = int(input("enter value"))
  new_node = Node(data)
  if head is None:
    head = new_node
  else :
    temp = head
    while temp.next is not None:
      temp = temp.next
    temp.next = new_node

def traverse():
  global head # Declare head as global
  temp = head
  while(temp is not None): # Changed condition to temp is not None for correct traversal
    print(temp.data)
    temp = temp.next

if __name__ == '__main__':
  n = int(input())
  head = None # Re-initialize head before insertion loop
  for i in range(n):
    insert()
  traverse()
