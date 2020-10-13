#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime complexity for this code is linear time: O(n). In this code code the `a` increases in proportion to the input 
   value `n`


b) The runtime complexity for this code is quasilinear time: O(n log n). The inner while loop runs at O(log n) and then
   the outside for loop runs at O(n) so the combined time is O(n log n).

c) The runtime complexity for this code is linear time: O(n). Since the recursion decrements `n` then the statements executed 
   are proportional to the input.

## Exercise II

The use of a algorithm that starts by dividing the floors in half so that you have a set of lower levels and higher levels. 
If an egg breaks at that floor then we start checking the floors below until a dropped egg does not break. If not then 
we start searching the top floors until a dropped egg breaks. Using this binary search algorithm is best here because the
floors are pre sorted. Everytime we pass through a search iteration we cut the searched list in half.

The runtime complexity of this solution is logarithmic time: (O log n)
