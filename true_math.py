from math import inf
'''При делении на 0 выдает бесконечность'''

def divide(first, second):
    if second == 0:
        result = inf
    else:
        result = first / second
    return result