# Python program for implementation of MergeSort

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]

def mergesort(list1):
    if len(list1) > 1:
        mid = len(list1) // 2

        # create temp arrays
        left_list1 = list1[:mid]
        right_list1 = list1[mid:]
        
        # Recursive call on each half
        mergesort(left_list1)
        mergesort(right_list1)

        # Merge the temp arrays back into arr[l..r]
        i = 0 # Initial index of left subarray
        j = 0 # Initial index of right subarray
        k = 0 # Initial index of merged subarray
        
        while i<len(left_list1) and j<len(right_list1):
            if left_list1[i] < right_list1[j]:
                list1[k] = left_list1[i]
                i = i+1
                k = k+1
            else:
                list1[k] = right_list1[j]
                j = j+1
                k = k+1
        
        # Copy the remaining elements of left list, if there are any
        while i<len(left_list1):   
            list1[k] = left_list1[i]
            i = i+1
            k = k+1
        
        # Copy the remaining elements of right list, if there are any
        while j<len(right_list1):
            list1[k] = right_list1[j]
            j = j+1
            k = k+1    

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Unsorted list: ", arr)

    mergesort(arr)
    print("Sorted list: ", arr)