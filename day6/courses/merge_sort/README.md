## Merge Sort Algorithm
Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one. 

### The theory

This is the recursive approach for implementing merge sort. The steps needed to obtain the sorted array through this method can be found below:

* The list is divided into left and right in each recursive call until two adjacent elements are obtained.

* Now begins the sorting process. The i and j iterators traverse the two halves in each call. The k iterator traverses the whole lists and makes changes along the way.

* If the value at i is smaller than the value at j, left[i] is assigned to the myList[k] slot and i is incremented. If not, then right[j] is chosen.

* This way, the values being assigned through k are all sorted.

* At the end of this loop, one of the halves may not have been traversed completely. Its values are simply assigned to the remaining slots in the list.

And with that, the merge sort has been implemented!

### Time complexity
The algorithm works in O(n.logn). This is because the list is being split in log(n) calls and the merging process takes linear time in each call.