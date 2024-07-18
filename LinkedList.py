from Element import Element


class LinkedList:
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
                index = current_element.index
                new_element.index = index + 1
                current_element.previous = current_element
                break
            current_element = current_element.next

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
            return
        else:
            new_element.next = self.start
            self.start = new_element

    def delete_first_element(self):
        if self.start is None:
            return
        self.start = self.start.next

    def delete_last_element(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
            return
        current_element = self.start
        while current_element.next.next is not None:
            current_element = current_element.next
        current_element.next = None

    def delete_index(self, index):
        if self.start is None:
            return
        current_element = self.start
        while index != current_element.index:
            current_element = current_element.next
        self.start = current_element
        self.delete_first_element

    def delete_value(self, value):
        current_element = self.start
        if current_element.value == value:
            self.delete_first_element()
            return
        while current_element is not None and current_element.next.value != value:
            current_element = current_element.next
        if current_element is None:
            return
        else:
            current_element.next = current_element.next.next

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
#
# 1,4,3,5
#
# 4.prev = 3
# 4.next = 4
# curr = 3
# 3.prev = 1
