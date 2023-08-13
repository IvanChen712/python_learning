def generate_permutation_list(num_list):
    """find permuted lists of n given numbers"""
    # 建立base case
    if len(num_list) == 0:
        return []  # 当n为0时不返回任何数字
    if len(num_list) == 1:
        return [num_list]  # 当n为1时返回所有式子，作为之后首数字的基础
    list_of_comb = []  # 新建列表来存更新的排列
    for i in range(len(num_list)):
        first_num = num_list[i]  # 生成首字母
        for j in generate_permutation_list(num_list[:i] + num_list[i + 1:]):  # 去除首字母，继续递归
            list_of_comb.append([first_num] + j)  # 加入新的list

    return set(list_of_comb)  # 最后返回最终结果


if __name__ == "__main__":
    print(generate_permutation_list([1, 5, 5, 5]))
