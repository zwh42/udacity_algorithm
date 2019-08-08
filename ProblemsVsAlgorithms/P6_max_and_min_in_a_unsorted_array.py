def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None
    
    min_value = ints[0]
    max_value = ints[0]

    
    for num in ints[1:]:
        if num < min_value:
            min_value = num
        
        if num > max_value:
            max_value = num
    
    return (min_value, max_value)


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")