import polars as pl

def main():

    employees = pl.read_csv("employees.csv")

    #print(employees.columns) # ['name', 'department', 'email', 'salary', 'years_at_company', 'start_date']

    #s1 = employees.select(pl.col("salary"))

    s2 = employees.select(pl.col("start_date"), pl.col("salary"))

    print(s2.head(3))

if __name__ == "__main__":
    main()

# shape: (3, 2)
# ┌────────────┬────────┐
# │ start_date ┆ salary │
# │ ---        ┆ ---    │
# │ str        ┆ i64    │
# ╞════════════╪════════╡
# │ 2016-07-14 ┆ 250000 │
# │ 2016-02-13 ┆ 96540  │
# │ 2015-03-01 ┆ 126489 │
# └────────────┴────────┘

# python main.py
