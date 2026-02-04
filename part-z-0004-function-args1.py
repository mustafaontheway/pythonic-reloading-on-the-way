def sum_nums(*args) -> int:

    print(args)

    print(type(args))

    sum: int = 0

    for i in args:

        sum += i 

    return sum

result1 = print(sum_nums(3, 12, 27))

print("-------------------------")

result2 = print(sum_nums(3, 12, 27, 45))

# (3, 12, 27)
# <class 'tuple'>
# 42
# -------------------------
# (3, 12, 27, 45)
# <class 'tuple'>
# 87

# python main.py
