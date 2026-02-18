def find_dup(arr: list[int]) -> bool:

    return len(arr) != len(set(arr))
    
print(find_dup([3, 4, 5, 5]))

print(find_dup([3, 4, 6, 5, 12, 21]))

# True
# False
