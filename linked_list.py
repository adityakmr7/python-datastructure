class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previoud node is not in the linked list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node


    def delete_node(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return 

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        
        if cur_node is None:
            return 
        prev.next = cur_node.next
        cur_node = None
    

    def delete_node_at_post(self, pos):
        if self.head:
            cur_node = self.head
            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return

            prev = None
            count = 0
            while cur_node and count != pos:
                prev = cur_node
                cur_node = cur_node.next
                count += 1

            if cur_node is None:
                return 

            prev.next = cur_node.next
            cur_node = None





llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.delete_node_at_pos(0)

llist.print_list()










        