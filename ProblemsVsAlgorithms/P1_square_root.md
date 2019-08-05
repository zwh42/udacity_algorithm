# Square Root

---


Since the expected time complexity is O(log(n)), a natural choice is a binary search like algorithm. It is started by set "start = 0" and "end = number", from which median can be calculate as "mid = (start + end) // 2". The if mid * mid equals number, we know the answer should be mid. When mid^2 > number, it means the square root should e in the first half, thus reset end = mid - 1, redo binary search in the first half. Similarly, if mid^2 < number, it means the square root is in the second half, we have to reset the start to mid + 1 and do binary search in the second half, besides, we need to record the mid value as an approximation of the floored square root, in case we cannot find the integer square root. When the binary search ended, we can return the mid value as the answer.

Time complexity is O(log(n)) with binary search.
No extra space needed, the space complexity is O(1).




   