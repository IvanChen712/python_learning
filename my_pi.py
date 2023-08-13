import itertools


def pi(n):
    """ 计算pi的值 """
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odd_numbers = itertools.count(1, 2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*n-1.
    odd_numbers = itertools.islice(odd_numbers, n)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    series = (4 / n * (-1) ** (i % 2) for i, n in enumerate(odd_numbers))
    # step 4: 求和:
    return sum(series)


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
