## Binary search
Binary search is an efficient algorithm for finding an item from a **sorted list of items**. It works by repeatedly **dividing in half the portion of the list** that could contain the item, until you've narrowed down the possible locations to just one.

One of the most common ways to use binary search is to find an item in an array. For example, the Tycho-2 star catalog contains information about the brightest 2,539,913 stars in our galaxy. 

Suppose that you want to search the catalog for a particular star, based on the star's name. If the program examined every star in the star catalog in order starting with the first, an algorithm called linear search, the computer might have to examine all 2,539,913 stars to find the star you were looking for, in the worst case. If the catalog were sorted alphabetically by star names, **binary search** would not have to examine more than 22 stars, even in the worst case.

Example: 
![binary_search_image](https://www.geeksforgeeks.org/wp-content/uploads/Binary-Search.png)

The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(Log n). 
We basically ignore half of the elements just after one comparison.
1. Compare x with the middle element.
2. If x matches with the middle element, we return the mid index.
3. Else If x is greater than the mid element, then x can only lie in the right half subarray after the mid element. So we recur for the right half.
4. Else (x is smaller) recur for the left half.