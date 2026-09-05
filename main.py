"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
    if x<=1:
        return x
    else:
        ra = foo(x-1)
        rb = foo(x-2)
        return ra + rb

def longest_run(mylist, key):
    current_sequence = 0
    max = 0
    for num in mylist:
        if num == key:
            current_sequence += 1
            if current_sequence>max:
                max = current_sequence
        else:
            current_sequence = 0
    return max


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size              # the length of the longest run on left side of input
                                                # eg, with a key of 12, [12 12 3] has left_size of 2 
        self.right_size = right_size            # length of longest run on right side of input
                                                # eg, key 12, [3 12 12] has right_size of 2
        self.longest_size = longest_size        # length of longest run in input
                                                # eg, [12 12 4 12 12 12]: longest_size is 3
        self.is_entire_range = is_entire_range  # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    ### TODO
    #base case if list is empty
    if len(mylist) == 0:
        return Result(0, 0, 0, False)

    #next case if the list is of lenght 1
    if len(mylist) == 1:
        is_match = (mylist[0] == key)
        if is_match:
            count =1
        else:
            count = 0
        return Result(left_size=count, right_size=count, longest_size=count, is_entire_range=is_match)
    
    #next case is if the length is >1 we divide it
    mid=len(mylist)//2
    left_result = longest_run_recursive(mylist[:mid], key)
    right_result = longest_run_recursive(mylist[mid:], key)

    #next is combining the results
    #add the left and right sizes if the key crosses both sides
    divided_size = left_result.right_size +right_result.left_size

    overall_longest = max(left_result.longest_size, right_result.longest_size, divided_size)

    #handle left side cases
    if left_result.is_entire_range:
        combined_left = left_result.left_size + right_result.left_size
    else:
        combined_left = left_result.left_size
    #handle right side cases
    if right_result.is_entire_range:
        combined_right = right_result.right_size + left_result.right_size
    else:
        combined_right = right_result.right_size

    #what if the entire range is the key
    combined_entire= left_result.is_entire_range and right_result.is_entire_range

    return Result(combined_left, combined_right, overall_longest, combined_entire)

#google gemini helped with this code
