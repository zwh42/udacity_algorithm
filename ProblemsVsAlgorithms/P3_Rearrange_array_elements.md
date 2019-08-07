# Rearrange Array Elements

---
If the input array is an sorted array, the solution is quite straightforward, we just need 2 pointers to point the first two elements in the array at first. And traverse the array with step 2 to form the two numbers.

Thus the question is to sort the array, which can be achieved by merge sort. The time complexity is O(nlog(n)). and The space complexity is O(n).   