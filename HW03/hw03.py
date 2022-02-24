HW_SOURCE_FILE = __file__

import sys

sys.setrecursionlimit(10000)

def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
    if pos == 0:
        return 0
    elif pos % 10 == 8:
        return num_eights(pos//10) + 1
    else:
        return num_eights(pos//10)

    #Iteration
    """
    def num_eight(pos):
        num = 0
        while pos > 0:
            pos, last = pos // 10, pos % 10
            if last == 8:
                num += 1
        return num
    """

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
    return calculate(n, 1, 1, 1)

def calculate(n, value, k, direction):
    if n == 1:
        return value
    else:
        if k % 8 == 0 or num_eights(k):
            return calculate(n, value - direction, k+1, -direction)
        else:
            return calculate(n, value + direction, k+1, direction)

    # Alternate solution
    # Considering how to call recursion function is the key to solving the problem.

    """
    def pingpong(n):
        if n < 8:
            return n
        def calculate(n):
            if n < 8:
                return 1 
            if (n-1) % 8 == 0 or num_eights(n-1):
                return (-1)*calculate(n-1)
            return calculate(n-1)
        return pingpong(n-1)+calculate(n-1)
    """

    #The problem is that we must consider about direction.
    #Iteration
    """
    def pingpong(n):
        value, k, direction = 1, 1, 1
        while k < n:
            if k % 8 == 0 or num_eights(k):
                direction = -direction
            value += direction
            k += 1
        return value
    """


def missing_digits(n):
    """Given a number a that is in sorted, non-decreasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return 0
    else:
        last1, last2 = n % 10, (n // 10) % 10
        if last2 < last1 - 1:
            return missing_digits(n//10) + last1 - last2 - 1
        else:
            return missing_digits(n//10)

    # Iteration
    """
    def missing_digit(n):
        if n < 10:
            return 0
        else:
            num = 0
            while n > 10:
                last1, last2 = n % 10, (n // 10) % 10
                if last2 < last1 - 1:
                    num += last1 - last2 - 1
                n //= 10
            return num
    """

def ascending_coin(coin):
    """Returns the next ascending coin in order.
    >>> ascending_coin(1)
    5
    >>> ascending_coin(5)
    10
    >>> ascending_coin(10)
    25
    >>> ascending_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def descending_coin(coin):
    """Returns the next descending coin in order.
    >>> descending_coin(25)
    10
    >>> descending_coin(10)
    5
    >>> descending_coin(5)
    1
    >>> descending_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    return helper(change, 1)

def helper(change, min_coin=1):
    if change == 0:
        return 1
    if change < 0:
        return 0
    if min_coin is None:
        return 0
    next_coin = helper(change, ascending_coin(min_coin))
    next_money = helper(change - min_coin, min_coin)
    return next_coin + next_money

    # Alternate solution
    # Using descending_coin function
    """
    def count_coins(change):
        return helper(change, 25)
    
    def helper(change, max_coin=25)
        if change == 0:
            return 1
        if change < 0:
            return 0
        if not max_coin:
            return 0
        next_coin = helper(change, descending_coin(max_coin))
        next_money = helper(change - max_coin, max_coin)
        return next_coin + next_money
    """

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    if n == 1:
        print_move(start, end)
        return None
    move_stack(n - 1, start, 6 - start - end)
    print_move(start, end)
    move_stack(n - 1, 6 - start - end, end)

    # Detailed analysis: https://blog.csdn.net/qq_41282102/article/details/85061198



from operator import sub, mul


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial',
    ...     ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'FunctionDef', 'Recursion'])
    True
    """
    # With reference to other people
    return (lambda f: lambda k: f(f, k))(lambda f, k: k if k == 1 else mul(k, f(f, sub(k, 1))))
    # Alternate solution:
    # return (lambda f: f(f))(lambda f: lambda x: 1 if x == 0 else x * f(f)(x - 1))
