# Easy Functions
def find_max(list):
    return max(list)

def list_sum(list):
    return sum(list)

def append_element(list, element):
    list.append(element)
    return list

# Moderate Functions
def average(list):
    return sum(list) / len(list) if list else 0  # Handles empty lists

def remove_element(list, element):
    list.remove(element)
    return list

def reverse_list(list):
    return list[::-1]

# Tough Functions
def sort_list(list):
    return sorted(list)

def count_occurrences(list, element):
    return list.count(element)

def find_index(list, element):
    return list.index(element)

