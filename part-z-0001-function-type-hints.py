def integer_divisors(num: int):

    divisors: list[int] = []

    for i in range(1, num + 1):

        if num % i == 0:

            divisors.append(i)

    return divisors

r1 = integer_divisors(20)

print(r1) # [1, 2, 4, 5, 10, 20]

r2 = integer_divisors(30)

print(r2) # [1, 2, 3, 5, 6, 10, 15, 30]

# python main.py
