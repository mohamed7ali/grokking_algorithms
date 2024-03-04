def binary_search(lst, item):
    # Get the boundaries of our list
    low = 0
    high = len(lst) - 1
    
    while low <= high:
        # Calculate the index of the middle element
        mid = (low + high) // 2
        # Retrieve the element at the middle index
        guess = lst[mid]
        # Return the index if there is a match
        if guess == item:
            return mid
        # Truncate to the lower part of the list
        if guess > item:
            high = mid - 1
        # Truncate to the upper part of the list
        else:
            low = mid + 1
    # Return None if the item is not found in the list
    return None 
