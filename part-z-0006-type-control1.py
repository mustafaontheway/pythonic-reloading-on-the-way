def plus_five(arr):

    for i in range(len(arr)):

        if type(arr[i]) == int:

            arr[i] += 5

l1 = ["john", 10, True, 3.12]
l2 = ["bill", "gibson", True, 47]


plus_five(l1)

plus_five(l2) 

print(l1)

print(l2)

# ['john', 15, True, 3.12]
# ['bill', 'gibson', True, 52]
