def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        raise Exception("please input a positive integer!")

    if number <= 1:
        return number

    start = 0
    end = number

    while start <= end:
        mid = (start + end) // 2
        product = mid ** 2
       
        if product == number:
            return mid
        elif product < number:
            start = mid + 1
            root = mid
        else:
            end = mid - 1
    
    return root
        

        

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (296 == sqrt(87654)) else "Fail")
print ("Pass" if  (1024 == sqrt(1049600)) else "Fail")