def str2float(s):
    float_part = 0
    val = 0
    for ch in s:
        if ch == '.':
            float_part = 1
        else:
            num = int(ch)
            if float_part >= 1:
                val = val + num / (10 ** float_part)
                float_part += 1
            else:
                val = val * 10 + num
    return val


# testing
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
