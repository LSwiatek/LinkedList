from LinkedList import LinkedList
import networkx as nx

from GraphUtil import GraphUtil
linked_list = LinkedList(GraphUtil(nx.MultiDiGraph(), render_delay=0.5))
# linked_list = LinkedList(GraphUtil.NoRender())
linked_list.add("5")
linked_list.add("1")
linked_list.add("3")
linked_list.add("6")
linked_list.add("8")
linked_list.add("9")

print(f"Linked list: {linked_list}")
linked_list.add_at_beginning("0")
linked_list.delete_last_element()
linked_list.delete_first_element()
linked_list.delete_index(2)

# linked_list.print_linkedlist()
# linked_list.sort_asc()


list = [1,5,4,6]


def sort_asc(list):
    n = len(list)
    for i in range(n):
        for j in range(n-i-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    print(list)

sort_asc(list)









