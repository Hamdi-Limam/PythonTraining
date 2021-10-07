## Python code for shell sort algorithm

def shellsort(list1):

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    gap = len(list1) // 2
    while gap > 0:
        for i in range(gap,len(list1)):
            current_val = list1[i]
            j = i

            while j>=gap and current_val<list1[j-gap]:
                list1[j] = list1[j-gap]
                j = j - gap

            list1[j] = current_val
        
        gap = gap // 2 
        
if __name__ == "__main__":
    arr = [20, 1, 5, 4, 3, 7, 0]
    print("Unsorted list:", arr)

    shellsort(arr)
    print("Sorted list:", arr)