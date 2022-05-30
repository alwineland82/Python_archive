import operator as op
from functools import reduce
import re

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

def milk_it(exp):
    assert type(exp) == str 
    lst_of_values = list(filter(lambda x: x != '', re.split('\(|\)|\^|\+|\-|[a-z]', exp)))
    x = [i for i in exp if i.isalpha()]
    if len(lst_of_values) == 2:
        lst_of_values.insert(0, '1')
    if exp[1] == '-':
        lst_of_values[0] = '-' + lst_of_values[0]
    if '+' not in exp:
        lst_of_values[1] = '-' + lst_of_values[1]
    return lst_of_values + x
    
def expand(expr):
    numX, num, pwr, letter = milk_it(expr)
    r = 0
    pwr_t = int(pwr)
    result = ''
    while r < int(pwr) + 1:
        temp = ncr(int(pwr), r) * int(numX) ** pwr_t * int(num) ** r
        if temp > 0:
            result += '+' + str(temp) + letter
            if pwr_t >= 2:
                result += '^' + str(pwr_t)
        else:
            result += str(temp) + letter
            if pwr_t >= 2:
                result += '^' + str(pwr_t)
        r += 1
        pwr_t -= 1
    if result[0] == '+':
        return result[1:-1]
    return result[:-1]

# "8x^3-36x^2+54x-27"
print(expand("(x-1)^2"))
