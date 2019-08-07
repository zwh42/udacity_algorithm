def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    def merge_sort(input_list, left, right):
        if left >= right:
            return
        
        mid = (left + right) // 2
        merge_sort(input_list, left, mid)
        merge_sort(input_list, mid + 1, right)
        merge(input_list, left, mid, right)
    
    def merge(input_list, left, mid, right):
        temp_list = [0 for i in range(right - left + 1)]

        i = 0
        p = left
        q = mid + 1
        while p <= mid and q <= right:
            if input_list[p] >= input_list[q]:
                temp_list[i] = input_list[p]
                p += 1
            else:
                temp_list[i] = input_list[q]
                q += 1
            i += 1
        
        if p > mid:
            while q <= right:
                temp_list[i] = input_list[q]
                q += 1
                i += 1
        
        if q > right:
            while p <= mid:
                temp_list[i] = input_list[p]
                p += 1
                i += 1

        input_list[left:right+1] = temp_list

    
    if len(input_list) == 0:
        return 0

    if len(input_list) ==1:
        return input_list[0]

    merge_sort(input_list, 0, len(input_list) - 1)

    p = 0 
    q = 1
    x, y = 0, 0
    while p < len(input_list) or q < len(input_list):
        if p < len(input_list):
            x = 10 * x + input_list[p]
            p += 2
        
        if q < len(input_list):
            y = 10 * y + input_list[q]
            q += 2

    return [x, y] 
        


              


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[1, 2], [2, 1]])
test_function([[1, 3, 5, 2, 4, 6], [642, 531]])
