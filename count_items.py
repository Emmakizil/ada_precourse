"""Write a function count_item_in_list that takes two arguments, an item and a list called list_of_items. The function has the following behavior:
The function returns the number of times the item appears in the list
If the list does not contain the item, the function returns 0 ."""

def count_item_in_list(item, list_of_items):
    frequency = 0
    for i in range(len(list_of_items)):
        if list_of_items[i] == item:
            frequency += 1
    
    if frequency >= 1:
        return frequency
    return 0