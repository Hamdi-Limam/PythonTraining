## Selection Sort Algorithm 
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

1. Set the first element as minimum.
![sort_image1](https://cdn.programiz.com/cdn/farfuture/w1ZKsO2Obaw1WV03_lamX22SVyapwhbiKoLkT5Raiiw/mtime:1582112622/sites/tutorial2program/files/Selection-sort-0-initial-array.png)

2. Compare minimum with the second element. If the second element is smaller than minimum, assign the second element as minimum.

Compare minimum with the third element. Again, if the third element is smaller, then assign minimum to the third element otherwise do nothing. The process goes on until the last element.
![sort_image2](https://cdn.programiz.com/cdn/farfuture/9jjqXX0fGtJE2ul2Mga20fvf_GkNlFAFsDMwrrwFzbQ/mtime:1582112622/sites/tutorial2program/files/Selection-sort-0-comparision.png)

3. After each iteration, minimum is placed in the front of the unsorted list.
![sort_image3](https://cdn.programiz.com/cdn/farfuture/6o-qergdHNq6D7eBxBi87yIuCLc7MJy2BHR4QHeNxxQ/mtime:1582112622/sites/tutorial2program/files/Selection-sort-0-swapping.png)

4. For each iteration, indexing starts from the first unsorted element. Step 1 to 3 are repeated until all the elements are placed at their correct positions.
![sort_image4](https://cdn.programiz.com/cdn/farfuture/VPGtdVYag2vfHBotOaFEiYLqvWAD_Jwfnwur_AtKQHo/mtime:1582112622/sites/tutorial2program/files/Selection-sort-0.png)

### Selection Sort Code in Python

# Selection sort in Python
```
def selectionSort(array, size):

    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)
```