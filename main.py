class Element:
    def __init__(self, value):
        self.value = value
        self.next = None


class List:
    def __init__(self):
        self.start = None

    def add(self, value):
        new_element = Element(value)
        if self.start is None:
            self.start = new_element
            return
        current_element = self.start
        while True:
            if current_element.next is None:
                current_element.next = new_element
                break
            current_element = current_element.next

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
linked_list.printLinkedList()

