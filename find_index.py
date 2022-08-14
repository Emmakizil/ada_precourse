"""Write a function find_index_of_item that takes two arguments, an item and a list called list_of_items. The function has the following behavior:

If the list contains the item, the function returns the index of the item in the list.
If the list contains the item multiple times, the function returns the index of the first time the item appears in the list.
If the list does not contain the item, the function returns -1.
Example inputs and outputs:"""

def find_index_of_item(item, list_of_items):
    frequency = 0
    for i in range(len(list_of_items)):
        if list_of_items[i] == item:
            frequency += 1
    
    if frequency == 1:
        return list_of_items.index(item)
    elif frequency > 1:
        return frequency
    else: return -1