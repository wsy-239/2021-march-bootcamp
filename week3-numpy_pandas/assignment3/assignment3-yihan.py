# Q1.
"""
请实现 2个python list 的 ‘cross product’ function.
要求按照Numpy 中cross product的效果: https://numpy.org/doc/stable/reference/generated/numpy.cross.html
只实现 1-d list 的情况即可.
x = [1, 2, 0]
y = [4, 5, 6]
cross(x, y)
> [12, -6, -3]
"""


def cross(x, y):
    if len(x) == 2:
        return [x[0] * y[1] - x[1] * y[0]]
    if len(x) == 3:
        return [x[1] * y[2] - x[2] * y[1], x[2] * y[0] - x[0] * y[2], x[0] * y[1] - x[1] * y[0]]


# Q2.
"""
交易传输指令经常需要验证完整性，比如以下的例子
{
    request :
    {
        order# : 1,
        Execution_details: ['a', 'b', 'c'],
        request_time: "2020-10-10T10:00EDT"
    },
    checksum:1440,
    ...
}
可以通过很多种方式验证完整性，假设我们通过判断整个文本中的括号 比如 '{}', '[]', '()' 来判断下单是否为有效的。
比如 {{[],[]}}是有效的，然而 []{[}](是无效的。
写一个python 程序来进行验证。
 def checkOrders(orders: [str]) -> [bool]:
 return a list of True or False.
checkOrders(["()", "(", "{}[]", "[][][]", "[{]{]"] return [True, False, True, True, False]
"""


def checkOrders(orders: [str]) -> [bool]:
    result = []
    match = {'(': ')', '{': '}', '[': ']'}
    for od in orders:
        tmp = []
        for i in range(len(od)):
            if od[i] in "({[":
                tmp.append(od[i])
            else:
                if not len(match) or match[tmp[-1]] != od[i]:
                    break
                tmp.pop()
        if not len(tmp):
            result.append(True)
        else:
            result.append(False)

    return result


# Q3
"""
我们在进行交易的时候通常会选择一家broker公司而不是直接与交易所交易。
假设我们有20家broker公司可以选择 (broker id is 0...19)，通过一段时间的下单表现(完成交易的时间)，我们希望找到最慢的broker公司并且考虑与其解除合约。
我们用简单的数据结构表达broker公司和下单时间: [[broker id, 此时秒数]]
[[0, 2], [1, 5], [2, 7], [0, 16], [3, 19], [4, 25], [2, 35]]
解读: 
Broker 0 使用了0s - 2s = 2s
Broker 1 使用了5 - 2 = 3s
Broker 2 使用了7 - 5 = 2s
Broker 0 使用了16-7 = 9s
Broker 3 使用了19-16=3s
Broker 4 使用了25-19=6s
Broker 2 使用了35-25=10s
综合表现，是broker2出现了最慢的交易表现。
Def slowest(orders: [[int]]) -> int:
slowest([[0, 2], [1, 5], [2, 7], [0, 16], [3, 19], [4, 25], [2, 35]]) return 2
"""


def slowest(orders: [[int]]) -> int:
    idx = -1
    tmp = {}
    for i in range(len(orders)):
        bid = orders[i][0]
        if i == 0:
            idx = bid
            btime = orders[i][1]
        else:
            p = orders[i - 1][1]
            c = orders[i][1]
            btime = c - p
        if bid in tmp:
            tmp[bid] += btime
        else:
            tmp[bid] = btime

    for k in tmp.keys():
        if tmp[k] > tmp[idx]:
            idx = k

    return idx


# Q4
"""
判断机器人是否能返回原点
一个机器人从平面(0,0)的位置出发，他可以U(向上), L(向左), R(向右), 或者D(向下)移动一个格子。
给定一个行走顺序，问是否可以回到原点。
例子
1. moves = "UD", return True.
2. moves = "LL", return False.
3. moves = "RRDD", return False.
4. moves = "LDRRLRUULR", return False.
def judgeRobotMove(moves: str) -> bool:
"""


def judgeRobotMove(moves: str) -> bool:
    pos = [0, 0]
    for s in moves:
        if s == 'U':
            pos[1] += 1
        if s == 'D':
            pos[1] -= 1
        if s == 'L':
            pos[0] -= 1
        if s == 'R':
            pos[0] += 1

    return pos[0] == 0 and pos[1] == 0


# Q5
"""
写一个验证email格式的程序， 对于给定的string监查是不是一个email地址:
1. 必须只包含小写字母，"-", "/" , "." , "_" 和数字
2. 有且仅有一个"@"
3. @之前之后不能为空
4. 以 ".edu" 或 ".com" 结尾
可以使用regex或者python标准包的方法。
"""


def isValidEmail(email):
    import re
    pattern = r"[-/.0-9_a-z]+@[-/.0-9_a-z]*\.(com|edu)"
    m = re.match(pattern, email)
    return m is not None
