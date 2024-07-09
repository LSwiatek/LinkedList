class Element:
    def __init__(self, value):
        self.value = value
        self.next = None


class List:
    def __init__(self):
        self.start = None
        self.elements_list = []

    def add(self, value):
        new_element = Element(value)
        if self.start is None:
            self.start = new_element
            self.elements_list.append(new_element)
        else:
            current_element = self.elements_list[-1]
            self.elements_list.append(new_element)
            current_element.next = new_element

    def printLinkedList(self):
        current_element = self.start
        while current_element:
            print(current_element.value)
            current_element = current_element.next
        print("None")

linked_list = List()
linked_list.add("1")
linked_list.add("5")
linked_list.add("3")
linked_list.add("6")
linked_list.printLinkedList()




