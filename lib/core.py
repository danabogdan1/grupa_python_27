
def even_numbers(list1):
    res = []
    for n in list1:
        if n % 2 == 0:
            res.append(n)
    return res

def odd_numbers(list1):
    res = []
    for n in list1:
        if n % 2 != 0:
            res.append(n)
    return res

def is_even(nr):
    if nr % 2 == 0:
        return True
    else:
        return False