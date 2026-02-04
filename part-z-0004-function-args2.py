def mutl_nums(*args) -> int:

    mult = 1

    for i in args:

        mult *= i 

    return mult

print(mutl_nums(3, 10, 14))

print(mutl_nums(3, 10, -14, -21))

# 420
# 8820
