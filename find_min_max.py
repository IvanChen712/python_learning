def find_min_max(num_list):
    if not num_list:
        return None, None
    minimum = num_list[0]
    maximum = num_list[0]
    for x in num_list:
        if x > maximum:
            maximum = x
        if x < minimum:
            minimum = x
    return minimum, maximum


# 测试
if find_min_max([]) != (None, None):
    print('测试失败!')
elif find_min_max([7]) != (7, 7):
    print('测试失败!')
elif find_min_max([7, 1]) != (1, 7):
    print('测试失败!')
elif find_min_max([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
