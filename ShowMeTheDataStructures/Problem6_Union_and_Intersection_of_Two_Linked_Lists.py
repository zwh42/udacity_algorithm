class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    if llist_1.size()  == 0 and llist_2.size() == 0:
        return None
    if llist_1.size()  == 0:
        return llist_2
    if llist_2.size() == 0:
        return llist_1

    result = LinkedList()
    p1 = llist_1.head
    p2 = llist_2.head

    element_set = set()

    for p in [p1, p2]:
        while p is not None:
            element_set.add(p.value)
            p = p.next
    
    #print("union set: {}".format(element_set))
    for element in element_set:
        result.append(element)
    
    return result





def intersection(llist_1, llist_2):
    # Your Solution Here
    if llist_1.size()  == 0:
        return None
    if llist_2.size() == 0:
        return None 

    p_list = [llist_1.head, llist_2.head]
    element_set = [set(), set()]
    result = LinkedList()

    for i in range(len(p_list)):
        while p_list[i] is not None:
            element_set[i].add(p_list[i].value)
            p_list[i] = p_list[i].next
    
    #print("set1: {}, set2: {}\n".format(element_set[0], element_set[1]))
    intersection_set = set()
    for element in element_set[0]:
        if element in element_set[1]:
            intersection_set.add(element)
    
    #print("intersection: {}\n".format(intersection))

    for element in intersection_set:
        result.append(element)
    
    return result

    






if __name__ == "__main__":
    # Test case 1
    print("test case 1:\n")
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print ("union: ", union(linked_list_1,linked_list_2))
    print ("intersection:", intersection(linked_list_1,linked_list_2))

    # Test case 2
    print("test case 2:\n")
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print ("union: ", union(linked_list_3,linked_list_4))
    print ("intersection:",intersection(linked_list_3,linked_list_4))


    # Test case 3
    print("test case 3:\n")
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = []
    element_2 = []

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print ("union: ", union(linked_list_3,linked_list_4))
    print ("intersection:", intersection(linked_list_3,linked_list_4))
