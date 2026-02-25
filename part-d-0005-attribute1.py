member_ages = pl.Series("ages", [24, 17, 96, 47, 4, 44])

print(member_ages.name)

print(f"Number of member ages: {member_ages.shape[0]}")

print(member_ages.dtype) # here not UInt8

# ages
# Number of member ages: 6
# Int64
