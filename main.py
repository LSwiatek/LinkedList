from LinkedList import LinkedList

linked_list = LinkedList()
linked_list.add("5")
linked_list.add("1")
linked_list.add("3")
linked_list.add("6")
linked_list.add("8")
linked_list.add("9")
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









