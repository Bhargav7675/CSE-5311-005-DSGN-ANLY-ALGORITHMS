# selection_sort.py

def selection_sort(arr):
    """
    Perform an in-place selection sort on the given array.

    Parameters:
    arr (list): The list of elements to be sorted.

    Returns:
    list: The sorted list of elements.
    """

    # Length of the array
    n = len(arr)

    # Iterate over each element in the array
    for i in range(n):
        # Find the index of the minimum element in the unsorted portion
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        # Invariant: After the ith iteration, the first i+1 elements are sorted
        # Explanation:
        # At the end of each iteration, the minimum element from the unsorted portion
        # is placed in its correct position in the sorted portion of the array.
        # This maintains the invariant that the first i+1 elements are sorted.

    return arr
