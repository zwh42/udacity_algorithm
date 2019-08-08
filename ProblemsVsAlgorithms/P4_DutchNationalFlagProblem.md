# Dutch National Flag Problem

---
if we can put all 0s in the front part of the array and all 2s in the end part of the array, the problem will be solved. Thus we keep to pointer p, q to indicate where the next 0, 2 should be, p start from the beginning and q from the end. Then we traverse the array using index i. and do differnt swap with different input_list[i]. The time complexity is O(n) as there is one traverse. The space complexity is O(1) as no extra space corresponding input array size n is needed.     