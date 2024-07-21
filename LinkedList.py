from Element import Element
from GraphUtil import GraphUtil

class LinkedList:
    def __init__(self, graph = GraphUtil.NoRender):
        self.start = None
        self.graph = graph

    def add(self, value):
        new_element = Element(value)
        if self.start is None:
            self.start = new_element
            self.graph.reset_and_render_all(self)
            return
        current_element = self.start
        while True:
            if current_element.next is None:
                current_element.next = new_element
                index = current_element.index
                new_element.index = index + 1
                current_element.previous = current_element
                break
            current_element = current_element.next

        self.graph.reset_and_render_all(self)

    # pierwsza wersja funkcji add jaką zrobiłam, po zweryfikowaniu w internecie zmienilam na powyzszą wersje
    # def add(self, value):
    #     new_element = Element(value)
    #     if self.start is None:
    #         self.start = new_element
    #         self.elements_list.append(new_element)
    #     else:
    #         current_element = self.elements_list[-1]
    #         self.elements_list.append(new_element)
    #         current_element.next = new_element

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
        current_element = self.start
        while current_element.next.next is not None:
            current_element = current_element.next
        self.graph.mark_node_for_deletion(current_element.next)
        current_element.next = None
        self.graph.reset_and_render_all(self)

    def delete_index(self, index):
        if self.start is None:
            return
        current_element = self.start
        while index != current_element.index:
            current_element = current_element.next
        self.start = current_element
        self.graph.mark_node_for_deletion(self.start)
        self.delete_first_element
        self.graph.reset_and_render_all(self)

    def delete_value(self, value):
        current_element = self.start
        if current_element.value == value:
            self.delete_first_element()
            self.graph.reset_and_render_all(self)
            return
        while current_element is not None and current_element.next.value != value:
            current_element = current_element.next
        if current_element is None:
            return
        else:
            current_element.next = current_element.next.next
            self.graph.reset_and_render_all(self)

    def get_value_at_index(self, index):
        if self.start.index == index:
            print(self.start.value)
        else:
            current_element = self.start
            while index != current_element.index:
                current_element = current_element.next
            print(current_element.value)

    def print_linkedlist(self):
        current_element = self.start
        while current_element:
            print(current_element.value)
            current_element = current_element.next
        print("None")

    def sort_asc(self):
        if self.start.next is None:
            return
        current_element = self.start
        # while current_element.next is not None:
        if current_element.value > current_element.next.value:
            current_element.previous = current_element.next
            current_element.next = current_element.next
            current_element = current_element.previous
            current_element.previous = current_element.previous.previous
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
#
# 1,4,3,5
#
# 4.prev = 3
# 4.next = 4
# curr = 3
# 3.prev = 1
