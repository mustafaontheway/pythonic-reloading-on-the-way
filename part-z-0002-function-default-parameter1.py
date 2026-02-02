def age_calculator(birth_year: int, current_year: int = 2026) -> int:

    return current_year - birth_year

print(age_calculator(1947)) # 79

print(age_calculator(1996, 2027)) # 31
