Max and Min in a Unsorted Array

---
Then answer is quite straighforward. Firstly we take the first element in the array as both the min/max value. Then we traverse the rest of the array. If the element in the array < min, we update the min, similarly, if the element in the array > max, we update the max. Then with only one traversal, we can get both min/max. The time complexity is O(n), and space complexity is O(1) as there is no extra space needed.