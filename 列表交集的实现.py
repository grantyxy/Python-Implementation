from typing import List


def true_intersection(*true_set: List) -> List:
    """
    :type true_set: Zero, One, or more lists
    """
    # 检测参数个数，如果为2个以下，抛出异常
    if len(true_set) < 2:
        raise TypeError("交集必须只有在两个或以上才可能存在！")
    else:
        # 确定头两个集合的交集，然后用求出的交集与第3个，第4个...迭代求交
        intersection_list = [x for x in true_set[0] if x in true_set[1]]
        for x in range(2, len(true_set)):
            intersection_list = [x for x in true_set[x] if x in intersection_list]
        return intersection_list


l1 = ['GenStat', 'JMP', 'MATLAB+Statistics Toolbox', 'NCSS', 'R', 'SAS', 'SPSS', 'Stata', 'Statgraphics',
      'WPS Analytics']
l2 = ['GenStat', 'LIMDEP', 'MATLAB+Statistics Toolbox', 'NCSS', 'NLOGIT', 'R', 'SAS', 'SHAZAM', 'SPSS', 'Stata',
      'The Unscrambler']
l3 = ["EViews", 'gretl', 'Mathematica', 'R', 'RATS', 'SageMath', 'SAS', 'Stata']

print(true_intersection(l2, l3))
