# Given a list arr sorted in ascending order of size N and an integer K.
# Check if K is present in the list or not using binary search algo.
# returns 1 if K is present in the array, else it returns -1.

# Non recursive solution
def searchInSorted(N, K, arr):
    start = 0
    end = N - 1
    
    while start <= end:
        middle = (end + start) // 2
        
        # Check if K is present at mid
        if arr[middle] == K:
            return 1

        # If x is smaller, ignore right half
        elif arr[middle] > K:
            end = middle - 1
            middle = (end + start) // 2
        
        # If x is greater, ignore left half
        else:
            start = middle + 1
            middle = (end + start) // 2

    # If we reach here, then the element
    # was not present
    return -1

if __name__ == "__main__":
    N = 10
    K = 23
    arr = [2,5,8,12,16,23,38,56,72,91]
    print(searchInSorted(N, K, arr))