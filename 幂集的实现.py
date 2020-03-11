from itertools import chain, combinations
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    result = chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    power_set = [list(x) for x in result]
    return power_set
a = [1,2,3,4]
power_set = powerset(a)
print(power_set)