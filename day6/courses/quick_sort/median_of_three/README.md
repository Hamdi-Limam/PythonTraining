## Quick sort algorithm: Median of three
For More explanation: [Check this video](https://www.youtube.com/watch?v=1Vl2TB7DoAM)

### The issues with basic quicksort
1. O(n²) on sorted or reverse data
2. Process is not efficient on very small partition

### Simple improvement: Cutoffs
1. If partition length <= the cutoff, insertion sort it
2. More efficient for very small partitions

### Improved solution of median of 3
1. Sort the first, middle and last elements of the partition:
2. Swap the middle element with the next-to-last element (now the pivot)
3. Set up the i and j counters, ignoring the first and last elements
4. Partition as usual

### Code
```
import statistics

def partition(num, first, last):

    # Sort the first, middle and last elements of the partition:
    mid = (first+last) // 2
    num[first] = min([num[first], num[last], num[mid]])
    num[last] = max([num[first], num[last], num[mid]])
    num[mid] = statistics.median([num[first], num[last], num[mid]])
    

    # Swap the middle element with the next-to-last element (now the pivot)
    num[mid], num[last-1] = num[last-1], num[mid]
    pivot = num[last-1]

    # Set up the i and j counters, ignoring the first and last elements
    i = first+1
    j = last-1

    # Partition as usual
    while True:
        while i <= j and num[i]<=pivot:
            i += 1
        while i <= j and num[j]>=pivot:
            j -= 1
        if i <= j:
            num[i], num[j] = num[j], num[i]
        else:
            break
    num[last-1], num[i] = num[i], num[last-1]
    return j

def quicksort(num, first, last):
    if first<last:
        pivot = partition(num, first, last)
        quicksort(num, first, pivot-1)
        quicksort(num, pivot+1, last)


num = [5,15,3,0,12,17,0]
quicksort(num, 0, len(num)-1)
print(num)
```
### Performance
* Guaranteed O(n log n) for sorted or reverse data
* Pivot is the middle element
* Slight constant increase in time to select the pivot
* We always have at least one item to each side of the pivot
* Cutoffs also result in a slight performance increase
