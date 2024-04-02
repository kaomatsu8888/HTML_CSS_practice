def function(number, default_arg_list=[]):
    default_arg_list.append(number)
    return default_arg_list


print(function(1))  # [1]
print(function(2,[3,4]))  # [3, 4, 2]
print(function(3))  # [1, 3]
print(function(4,[5,6]))  # [5, 6, 4]
print(function(5))  # [1, 3, 5]
