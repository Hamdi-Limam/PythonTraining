## Bubble Sort Algorithm 
For most people, Bubble Sort is likely the first sorting algorithm they heard of in their Computer Science course.

It's highly intuitive and easy to "translate" into code, which is important for new software developers so they can ease themselves into turning ideas into a form that can be executed on a computer. However, Bubble Sort is one of the worst-performing sorting algorithms in every case except checking whether the array is already sorted, where it often outperforms more efficient sorting algorithms like [Quick Sort](https://stackabuse.com/quicksort-in-python/).

The idea behind Bubble Sort is very simple, we look at pairs of adjacent elements in an array, one pair at a time, and swap their positions if the first element is larger than the second, or simply move on if it isn't. Let's look at an example and sort the array 8, 5, 3, 1, 4, 7, 9:
![bubble_sort](https://stackabuse.s3.amazonaws.com/media/bubble-sort-in-java-1.gif)

If you focus on the first number, the number 8, you can see it "bubbling up" the array into the correct place. Then, this process is repeated for the number 5 and so on.

When no swaps are made, that means that the list is sorted. Though, with the previously implemented algorithm, it'll keep evaluating the rest of the list even though it really doesn't need to. To fix this, we'll keep a boolean flag and check if any swaps were made in the previous iteration.

If no swaps are made, the algorithm should stop:
```
def bubble_sort(our_list):
    # We want to stop passing through the list
    # as soon as we pass through without swapping any elements
    has_swapped = True

    while(has_swapped):
        has_swapped = False
        for i in range(len(our_list) - 1):
            if our_list[i] > our_list[i+1]:
                # Swap
                our_list[i], our_list[i+1] = our_list[i+1], our_list[i]
                has_swapped = True
```
The other optimization we can make leverages the fact that Bubble Sort works in such a way that the largest elements in a particular iteration end up at the end of the array.

The first time we pass through the list the position n is guaranteed to be the largest element, the second time we pass through the position n-1 is guaranteed to be the second-largest element and so forth.

This means that with each consecutive iteration we can look at one less element than before. More precisely, in the k-th iteration, only need to look at the first n - k + 1 elements:
```
def bubble_sort(our_list):
    has_swapped = True

    num_of_iterations = 0

    while(has_swapped):
        has_swapped = False
        for i in range(len(our_list) - num_of_iterations - 1):
            if our_list[i] > our_list[i+1]:
                # Swap
                our_list[i], our_list[i+1] = our_list[i+1], our_list[i]
                has_swapped = True
        num_of_iterations += 1
```

### Conclusion
In the most inefficient approach, Bubble Sort goes through n-1 iterations, looking at n-1 pairs of adjacent elements. This gives it the time complexity of O(n2), in both best-case and average-case situations. O(n2) is considered pretty horrible for a sorting algorithm.

It does have an O(1) space complexity, but that isn't enough to compensate for its shortcomings in other fields.