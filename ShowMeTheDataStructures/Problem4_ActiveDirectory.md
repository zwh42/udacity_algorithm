# Active Directory

---
## Design
In function is_user_in_group(), firstly we will check if user is in current group's users, then for each sub group, we will call function is_user_in_group() recursively.

## Time Complexity
Say there's n level of sub-group, each sub-group have m sub-groups under it, and k users. In the base case (no more sub group), the code take O(k) to search for the user. In the upper level, the base case will be called by m times, plus one search of user at its level, thus the time complexity is O(m * k + k). With the same calculation, we can get the worst time complexity is O(k * m^n).

## Space Complexity
Say there's n level of sub-group, each sub-group have m sub-groups under it, and k users. Since both the user and subgroup are stored in the list, the space complexity is O(m + k). This holds true for each level, thus the space complexity is O((m + k) * n).




