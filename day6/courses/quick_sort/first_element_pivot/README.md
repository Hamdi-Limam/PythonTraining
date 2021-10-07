## Quick sort Algorithm: first/last element pivot

### Introduction
Quicksort is **a popular sorting algorithm and is often used**, right alongside Merge Sort. It's a good example of an efficient sorting algorithm, with an **average complexity of O(nlogn)**. Part of its popularity also derives from the ease of implementation.

Quicksort is a representative of three types of sorting algorithms: **divide and conquer, in-place, and unstable**.
* Divide and conquer: Quicksort splits the array into smaller arrays until it ends up with an empty array, or one that has only one element, before recursively sorting the larger arrays.
* In place: Quicksort doesn't create any copies of the array or any of its subarrays. It does however require stack memory for all the recursive calls it makes.
* Unstable: A stable sorting algorithm is one in which elements with the same value appear in the same relative order in the sorted array as they do before the array is sorted. An unstable sorting algorithm doesn't guarantee this, it can of course happen, but it isn't guaranteed.

This is something that becomes important when you sort objects instead of primitive types. For example, imagine you have several Person objects that have the same age, i.e. Dave aged 21 and Mike aged 21. If you were to use Quicksort on a collection that contains both Dave and Mike, sorted by age, there is no guarantee that Dave will come before Mike every time you run the algorithm, and vice versa.

### Quicksort
The basic version of the algorithm does the following:

Divide the collection in two (roughly) equal parts by taking a pseudo-random element and using it as a pivot.

Elements smaller than the pivot get moved to the left of the pivot, and elements larger than the pivot to the right of it.

This process is repeated for the collection to the left of the pivot, as well as for the array of elements to the right of the pivot until the whole array is sorted.

When we describe elements as "larger" or "smaller" than another element - it doesn't necessarily mean larger or smaller integers, we can sort by any property we choose.

If we have a custom class Person, and each person has a name and age, we can sort by name (lexicographically) or by age (ascending or descending).

### How Quicksort Works
Quicksort will, more often than not, fail to divide the array into equal parts. This is because the whole process depends on how we choose the pivot. We need to choose a pivot so that it's roughly larger than half of the elements, and therefore roughly smaller than the other half of the elements. As intuitive as this process may seem, it's very hard to do.

Think about it for a moment - how would you choose an adequate pivot for your array? A lot of ideas about how to choose a pivot have been presented in Quicksort's history - randomly choosing an element, which doesn't work because of **how "expensive" choosing a random element is while not guaranteeing a good pivot choice**; picking an element from the middle; picking a median of the first, middle and last element; and even more complicated recursive formulas.

The most straight-forward approach is to simply choose the first (or last) element. This leads to Quicksort, ironically, **performing very badly on already sorted (or almost sorted) arrays**.

This is how most people choose to implement Quicksort and, since it's simple and this way of choosing the pivot is a very efficient operation (and we'll need to do it repeatedly), this is exactly what we will do.

Now that we have chosen a pivot - what do we do with it? Again, there are several ways of going about the partitioning itself. We will have a "pointer" to our pivot, and a pointer to the "smaller" elements and a pointer to the "larger" elements.

The goal is to move the elements around so that all elements smaller than the pivot are to its left, and all larger elements are to its right. The smaller and larger elements don't necessarily end up sorted, we just want them on the proper side of the pivot. We then recursively go through the left and right side of the pivot.

A step by step look at what we're planning to do will help illustrate the process. Using the array shown below, we've chosen the first element as the pivot (29), and the pointer to the smaller elements (called "low") starts right after, and the pointer to the larger elements (called "high") starts at the end.

* 29 is the first pivot, low points to 99 and high points to 44
29 | 99 (low),27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44 (high)

* We move high to the left until we find a value that's lower than our pivot.
29 | 99 (low),27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21 (high),44

* Now that our high variable is pointing to 21, an element smaller than the pivot, we want to find a value near the beginning of the array that we can swap it with. It doesn't make any sense to swap with a value that's also smaller than the pivot, so if low is pointing to a smaller element we try and find one that's larger.
* We move our low variable to the right until we find an element larger than the pivot. Luckily, low was already positioned on 99.
* We swap places of low and high:
29 | 21 (low),27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,99 (high),44

* Right after we do this, we move high to the left and low to the right (since 21 and 99 are now in their correct places)
* Again, we move high to the left until we reach a value lower than the pivot, which we find right away - 12
* Now we search for a value larger than the pivot by moving low to the right, and we find the first such value at 41

This process is continued until the low and high pointers finally meet in a single element:
29 | 21,27,12,19,28 (low/high),44,78,87,66,31,76,58,88,83,97,41,99,44

* We've got no more use of this pivot so the only thing left to do is to swap pivot and high and we're done with this recursive step:
28,21,27,12,19,29,44,78,87,66,31,76,58,88,83,97,41,99,44

As you can see, we have achieved that all values smaller than 29 are now to the left of 29, and all values larger than 29 are to the right.

The algorithm then does the same thing for the 28,21,27,12,19 (left side) collection and the 44,78,87,66,31,76,58,88,83,97,41,99,44 (right side) collection.

### Implementation
Quicksort is a naturally recursive algorithm - divide the input array into smaller arrays, move the elements to the proper side of the pivot, and repeat.

Let's go through how a few recursive calls would look:
* When we first call the algorithm, we consider all of the elements - from indexes 0 to n-1 where n is the number of elements in our array.
* If our pivot ended up in position k, we'd then repeat the process for elements from 0 to k-1 and from k+1 to n-1.
* While sorting the elements from k+1 to n-1, the current pivot would end up in some position p. We'd then sort the elements from k+1 to p-1 and p+1 to n-1, and so on.

That being said, we'll utilize two functions - `partition() and quick_sort()`. The `quick_sort()` function will first `partition()` the collection and then recursively call itself on the divided parts.

Let's start off with the `partition()` function:
```
def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high
```
And finally, let's implement the `quick_sort()` function:
```
def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)
```
With both of them implemented, we can run quick_sort() on a simple array:
```
array = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]

quick_sort(array, 0, len(array) - 1)
print(array)
```
Since the algorithm is unstable, there's no guarantee that these two 44's were in this order to each other. Maybe there were originally switched - though this doesn't mean much in an integer array.

### Time Complexities
Worst Case Complexity `[Big-O]: O(n2)`
It occurs when the pivot element picked is either the greatest or the smallest element.

This condition leads to the case in which the pivot element lies in an extreme end of the sorted array. One sub-array is always empty and another sub-array contains n - 1 elements. Thus, quicksort is called only on this sub-array.

However, the quicksort algorithm has better performance for scattered pivots.
Best Case Complexity `[Big-omega]: O(n*log n)`
It occurs when the pivot element is always the middle element or near to the middle element.
Average Case Complexity `[Big-theta]: O(n*log n)`
It occurs when the above conditions do not occur.
