from Element import Element
from GraphUtil import GraphUtil


class LinkedList:
    def __init__(self, graph=GraphUtil.NoRender):
        self.start = None
        self.graph = graph

    def add(self, value):
        new_element = Element(value)
        if self.start is None:
            self.start = new_element
            self.graph.reset_and_render_all(self)
            return
        current = self.start
        while True:
            if current.next is None:
                current.next = new_element
                index = current.index
                new_element.index = index + 1
                current.previous = current
                break
            current = current.next
        self.graph.reset_and_render_all(self)

    def add_at_beginning(self, value):
        new_element = Element(value)
        if self.start is None:
            self.start = new_element
            self.graph.reset_and_render_all(self)
            return
        else:
            new_element.next = self.start
            self.start = new_element
            self.graph.reset_and_render_all(self)

    def delete_first_element(self):
        if self.start is None:
            return
        self.graph.mark_node_for_deletion(self.start)
        self.start = self.start.next
        self.graph.reset_and_render_all(self)

    def delete_last_element(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.graph.mark_node_for_deletion(self.start)
            self.start = None
            self.graph.reset_and_render_all(self)
            return
        current = self.start
        while current.next.next is not None:
            current = current.next
        self.graph.mark_node_for_deletion(current.next)
        current.next = None
        self.graph.reset_and_render_all(self)

    def delete_index(self, index):
        if self.start is None:
            return
        current = self.start
        self.graph.mark_node_for_deletion(self.start)
        if index > self.length():
            raise Exception("Index out of range")
        elif index == 0:
            self.delete_first_element()
        elif index == self.length():
            self.delete_last_element()
        else:
            while index != current.index:
                current = current.next
            current.previous.next = current.next
            current.next.previous = current.previous
        self.graph.reset_and_render_all(self)

    def delete_value(self, value):
        current = self.start
        if current.value == value:
            self.delete_first_element()
            self.graph.reset_and_render_all(self)
            return
        while current is not None and current.next.value != value:
            current = current.next
        if current is None:
            return
        else:
            current.next = current.next.next
            self.graph.reset_and_render_all(self)

    def get_value_at_index(self, index):
        if self.start.index == index:
            print(self.start.value)
        else:
            current = self.start
            while index != current.index:
                current = current.next
            print(current.value)

    def print_linkedlist(self):
        current = self.start
        while current:
            print(current.value)
            current = current.next
        print("None")

    def length(self):
        current = self.start
        length = 1
        while current.next is not None:
            current = current.next
            length += 1
        return length

    def swap(self, left, right):
        left.previous.next = right
        right.previous = left.previous
        left.previous = right
        left.next = right.next
        right.next.previous = left
        right.next = left
        return left, right

    def sort_asc(self):
        if self.start.next is None:
            return
        current_element = self.start
        n = self.length()
        for i in range(n):
            while current_element.next is not None:
                if current_element.value > current_element.next.value:
                    self.swap(current_element, current_element.next)
                else:
                    current_element = current_element.next
        self.print_linkedlist()
        self.graph.reset_and_render_all(self)

    # to string
    def __str__(self):
        current_element = self.start
        result = ""
        while current_element:
            result += str(current_element.value) + " "
            current_element = current_element.next
        return result

# dodac set_value (update), insert_at_index
