# Union and Intersection of Two Linked List

---

+ Union   
    create a singe element set using Python's set. Traverse both list and add each value to the element set, in this way there will be no duplication and missing.
    Then create a new linked list using all the element in the element set, which will be the union linked list.

    The traverse time complexity is O(n), and the build of the new list is also O(n).


+ Intersection
  create 2 element sets using Python's set, and traverse both list and add each node's value to the correspoinding element set, seprately. The create a new intersection set, add all elements in both two element set are add to the new intersection set. Then create a new linked list using the intersection set, which is the intersection list.

   The traverse time complexity is O(n), and the creation of intersection set's time complexity is O(n^2), as the code have to traverse one set with a for loop, and in each look it will check whether the element is in another set, which will take O(n) also.
    

