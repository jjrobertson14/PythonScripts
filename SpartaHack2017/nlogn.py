import math

def nlogn(c,l,u):
    lower = l
    upper = u
    while True:
        middle = (lower+upper)/2
        if lower == middle or middle == upper:
            return middle
        if middle*math.log(middle, 2) > c:
            upper = middle
        else:
            lower = middle
