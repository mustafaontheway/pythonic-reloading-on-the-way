import polars as pl

df = pl.DataFrame({"Name": ["Aykan", "Ayhan", "Aybuke", "Aybilge", "Aygun", "Aysel", "Aysu", "Ayaz", "Ayazhan", "Aygeldi", "Ayses"], 
                   "Age": [96, 17, 24, 45, 65, 77, 4, 44, 66, 55, 77]})

print(df.tail(3))

print("---------------------------------")

print(df.tail(-3))

"""
shape: (3, 2)
┌─────────┬─────┐
│ Name    ┆ Age │
│ ---     ┆ --- │
│ str     ┆ i64 │
╞═════════╪═════╡
│ Ayazhan ┆ 66  │
│ Aygeldi ┆ 55  │
│ Ayses   ┆ 77  │
└─────────┴─────┘
---------------------------------
shape: (8, 2)
┌─────────┬─────┐
│ Name    ┆ Age │
│ ---     ┆ --- │
│ str     ┆ i64 │
╞═════════╪═════╡
│ Aybilge ┆ 45  │
│ Aygun   ┆ 65  │
│ Aysel   ┆ 77  │
│ Aysu    ┆ 4   │
│ Ayaz    ┆ 44  │
│ Ayazhan ┆ 66  │
│ Aygeldi ┆ 55  │
│ Ayses   ┆ 77  │
└─────────┴─────┘

"""
