# Easy Functions
def union_sets(set1, set2):
    return set1.union(set2)

def add_element(s, element):
    s.add(element)
    return s

def is_subset(subset, superset):
    return subset.issubset(superset)

# Moderate Functions
def intersection_sets(set1, set2):
    return set1.intersection(set2)

def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

def remove_element(s, element):
    s.discard(element)  # Use discard to avoid KeyError if the element is not present
    return s

# Tough Functions
def difference_sets(set1, set2):
    return set1.difference(set2)

def is_disjoint(set1, set2):
    return set1.isdisjoint(set2)

def clear_set(s):
    s.clear()
    return s
