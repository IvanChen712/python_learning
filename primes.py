def _odd_iter():
    odd = 1
    while True:
        odd = odd + 2
        yield odd


# 必须要定义一个辅助函数，不能直接在filter里用lambda函数
# 在 Python 中，lambda 表达式可以捕获外部变量，形成闭包。但是在这个特定的情况下，lambda 表达式捕获的是变量
# n，它在每次迭代中都会发生变化，导致 lambda 表达式中使用的始终是迭代器 it 的最后一个值，而不是在创建 lambda 表达式时的值。这就导致了筛选的结果不正确。
def _not_divisible(prime):
    return lambda x: x % prime > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


for n in primes():
    if n < 100:
        print(n, end=' ')
    else:
        break
