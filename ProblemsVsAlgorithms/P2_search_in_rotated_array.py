def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
        return -1
    if len(input_list) == 1:
        if input_list[0] == number:
            return 0
        else:
            return -1

    def find_pivot_index(input_list, start, end):
        
        if start > end:
            return -1
        
        mid = (start + end) // 2

        if mid - 1 >= 0:            
            if input_list[mid - 1] > input_list[mid]:
                return mid
            else:
                pivot_index = 0
                
                temp = find_pivot_index(input_list, start, mid - 1)
                if temp > 0:
                    pivot_index = temp
                
                temp = find_pivot_index(input_list, mid + 1, end)
                if temp > 0:
                    pivot_index = temp
            
                
                return pivot_index
        else:
            return -1
        
        
        

    def binary_search(input_list,  start, end, number):
       
        if start > end:
            return -1

        mid = (start + end) // 2
        if number == input_list[mid]:
            return mid
        elif number < input_list[mid]:
            return binary_search(input_list, start, mid - 1, number)
        else:
            return binary_search(input_list, mid + 1, end, number)


    start = 0
    end = len(input_list) - 1
    pivot_index = find_pivot_index(input_list, start, end)

    #print("input list: ", input_list, "pivot index: ", pivot_index)

    if pivot_index < 0:
        pivot_index = 0

    left = binary_search(input_list[:pivot_index], 0, len(input_list[:pivot_index]) - 1, number)
    right = pivot_index + binary_search(input_list[pivot_index:], 0, len(input_list[pivot_index:]) -1, number)    

    match_index = -1
    if left >= 0:
        match_index = left
    elif right >= pivot_index:
        match_index = right

    return match_index




def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")





test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], 10])
test_function([[1], 10])
test_function([[10], 10])
test_function([[1, 2], 10])
test_function([[1, 2], 1])
test_function([[1, 2], 2])
