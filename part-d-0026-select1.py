import polars as pl

def main():

    employees = pl.read_csv("employees.csv")

    #print(employees.columns) # ['name', 'department', 'email', 'salary', 'years_at_company', 'start_date']

    s1 = employees.select(pl.col("salary"))

    print(s1.head(3))


if __name__ == "__main__":
    main()

# shape: (3, 1)
# ┌────────┐
# │ salary │
# │ ---    │
# │ i64    │
# ╞════════╡
# │ 250000 │
# │ 96540  │
# │ 126489 │
# └────────┘


# python main.py
