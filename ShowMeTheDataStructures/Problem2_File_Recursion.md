# File Recursion

---
+ Design Summary   
Recursive traverse is used for this problem. In each folder, a function is called to separated files/folders. For the files, the code will check if the file name match the suffix and put it into a list if match. For each folders, the traverse function will be called.

+ Time & space Complexity  
  Suppose there's n level of sub directory, in each level there's m sub directories, k files. In the base case (no more sub directory), the runtime is O(k) in search k files to match the suffix, then in the upper level, the base case will be called m times, plus the search of k files, thus the run time is O(k*m + k). After compute recursively, the time complexity is O(k * m^n).

  For the space complexity, each function call needs to create a stack to store function info, and inside function the space allocation is O(1). The total space complexity is O(m^n).     