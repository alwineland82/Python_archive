import re
def calc(expression):
    res = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?|[*+-/()]', expression)
    dic = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}
    while '/' in res or '*' in res:
        res = [str(i) for i in res]
        for i in res:
            if i in '/*':
                temp = dic[i](float(res[res.index(i) - 1]), float(res[res.index(i) + 1]))
                ind = res.index(i) - 1
                del res[ind : ind + 3]
                res.insert(ind, temp)
                break
    while len(res) != 1:
        res = [str(i) for i in res]
        for i in res:
            if i in '+-':
                temp = dic[i](float(res[res.index(i) - 1]), float(res[res.index(i) + 1]))
                ind = res.index(i) - 1
                del res[ind : ind + 3]
                res.insert(ind, temp)
                break
    return res
print(calc("10- 2- -5"))
