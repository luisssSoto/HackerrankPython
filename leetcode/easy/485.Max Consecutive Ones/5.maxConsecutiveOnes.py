"""Max Consecutive Ones"""
def find_max_consecutive_ones(nums):
    count = 0
    max_consecutive_ones = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count = 0
        if count > max_consecutive_ones:
            max_consecutive_ones = count
    return max_consecutive_ones

test1 = [1]
print(find_max_consecutive_ones(test1))
print(len(test1))
print(test1.count(0))

#1. input: array
#   output: integer

#2. create a count
#   iterate
#   conditional

#3. count variable
#   greater count
#   iterate the array
#   conditional if the element is 1 count += 1
#   else: conditional if the count is greater thant greaterCount replace the value count = 0
#   else count = 0
#   return greaterCount

#4. a little doubt at the end carefully