# Node: contains data and a point to next Node (singly linked),
#      and optionally a pointer to the previos Node (doubly linked)
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def contains(self, val):
        if (self.val == val):
            return True
        else:
            return False


class NodeDouble(Node):
    def __init__(self, val):
        super().__init__(val)
        self.prev = None

    def get_prev(self):
        return self.prev

    def set_prev(self, prev):
        self.prev = prev


node1 = Node(1)
print(node1.get_data())
node2 = NodeDouble(2)
print(node2.get_data())


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, val):
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, val):
        curr = self.head
        index = 0
        while (curr != None):
            if (curr.contains(val)):
                return index
            else:
                curr = curr.get_next()
                index += 1
        return -1

    def delete_at(self, index):
        if (index > self.count-1):
            return
        if (index == 0):
            self.head = self.head.get_next()
        prev = self.head
        while (index > 1):
            prev = prev.get_next()
            index -= 1
        curr = prev.get_next()
        prev.next = curr.get_next()
        curr.set_next(None)
        self.count -= 1
        return curr

    def print_list(self):
        curr = self.head
        if (curr == None):
            print("list is empty")
        while (curr.next != None):
            print(curr.get_data(), "->", end=" ")
            curr = curr.next
        print(curr.get_data())


test_list = LinkedList()
test_list.insert(3)
test_list.insert(5)
test_list.insert(7)
test_list.insert(9)
test_list.print_list()
print("item count = ", test_list.get_count())
print("finding item 11: ", test_list.find(11))
print("finding item 7: ", test_list.find(7))
deleted = test_list.delete_at(1)
test_list.print_list()
print("deleted val: ", deleted.get_data())
print("next of deleted: ", deleted.get_next())
print("current count: ", test_list.get_count())
print("finding item 7: ", test_list.find(7))
