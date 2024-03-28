# Finds the smallest element in the array and returns its index
def find_smallest(arr): 
    # Stores the first element as the smallest value 
    smallest = arr[0]
    # Stores the index of the smallest value
    smallest_index = 0
    # Loop over the array and compare each element with the "smallest" value 
    # Starting from the second element as we took the first to be our intial "smallest" value
    for i in range(1, len(arr)):
        # If there is a smaller value update the "smallest" variable
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
        
    return smallest_index


# Sorts an array in ascending order and return the array sorted
def selection_sort(arr): 
    new_arr = []
    # Gets the smallest value, add it to the list,
    # then remove it and so on
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr
