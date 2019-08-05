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
        
       
        #print("sublist", input_list[start:end + 1])
        
        if start >= end:
            return -1
        
        mid = (start + end) // 2
        
        #print("start:", start, "end:", end, "mid: ", mid, "length:", len(input_list))
        #print(input_list[mid - 1] > input_list[mid])

        if mid - 1 >= 0 and input_list[mid - 1] > input_list[mid]:
            return mid
        else:
            pivot_index = find_pivot_index(input_list, start, mid - 1)
            if pivot_index >= 0:
                return pivot_index
            
            pivot_index = find_pivot_index(input_list, mid, end + 1)
            if pivot_index >= 0:
                return pivot_index
        

    def binary_search(input_list, number, start, end):
        if start >= end:
            return -1

        mid = (start + end) // 2

        print(input_list)
        print("start = {}, end = {}, mid = {}".format(start, end, mid))

        if number == input_list[mid]:
            return mid
        elif number < input_list[mid]:
            binary_search(input_list, start, mid - 1, number)
        else:
            binary_search(input_list, mid + 1, end, number)


    start = 0
    end = len(input_list) - 1
    pivot_index = find_pivot_index(input_list, start, end)
    print("{}, pivot index: {}".format(input_list, pivot_index))

    left = binary_search(input_list[:pivot_index], start, pivot_index - 2, number)
    right = binary_search(input_list[pivot_index:], pivot_index, end, number)    

    if left >= 0:
        return left
    elif right >= 0:
        return right
    else:
        return -1




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