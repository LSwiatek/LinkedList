from LinkedList import LinkedList
import networkx as nx

from GraphUtil import GraphUtil
linked_list = LinkedList(GraphUtil(nx.MultiDiGraph(), render_delay=0.5))
# linked_list = LinkedList(GraphUtil.NoRender())
linked_list.add("5")
linked_list.add("1")
linked_list.add("3")
# linked_list.add("6")
# linked_list.add("8")
# linked_list.add("9")
linked_list.insert_at_index1(2, "22")

print(f"Linked list: {linked_list}")

# linked_list.update_value(2, "10")
# linked_list.add_at_beginning("0")
# linked_list.delete_last_element()
# linked_list.delete_first_element()
# linked_list.delete_index(2)
# print(f"Linked list: {linked_list}")
