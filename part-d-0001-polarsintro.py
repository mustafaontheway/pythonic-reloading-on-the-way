import polars as pl

print("Polars version:", pl.__version__)

print("--------------------------------------")

df = pl.DataFrame({"Name": ["Python", "Rust", "Kotlin", "Vyper"], "Age": [96, 17, 24, 45]})

display(df)
