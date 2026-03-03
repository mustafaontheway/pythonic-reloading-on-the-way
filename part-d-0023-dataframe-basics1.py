import polars as pl

def main():

    emps = pl.read_csv("employees.csv")

    print(emps.describe())

    print("-----------------------")

    print(emps.columns)

    print("-----------------------")

    print(emps.dtypes)

    print("-----------------------")

    print(emps.schema)

    print("-----------------------")

    print(emps.shape)

    print("-----------------------")

    print(emps.height)

    print("-----------------------")

    print(emps.width)


if __name__ == "__main__":
    main()

"""
shape: (9, 7)
┌────────────┬───────────────┬────────────┬─────────────────────────┬──────────────┬──────────────────┬────────────┐
│ statistic  ┆ name          ┆ department ┆ email                   ┆ salary       ┆ years_at_company ┆ start_date │
│ ---        ┆ ---           ┆ ---        ┆ ---                     ┆ ---          ┆ ---              ┆ ---        │
│ str        ┆ str           ┆ str        ┆ str                     ┆ f64          ┆ f64              ┆ str        │
╞════════════╪═══════════════╪════════════╪═════════════════════════╪══════════════╪══════════════════╪════════════╡
│ count      ┆ 1000          ┆ 845        ┆ 1000                    ┆ 1000.0       ┆ 1000.0           ┆ 1000       │
│ null_count ┆ 0             ┆ 155        ┆ 0                       ┆ 0.0          ┆ 0.0              ┆ 0          │
│ mean       ┆ null          ┆ null       ┆ null                    ┆ 109790.73    ┆ 5.141            ┆ null       │
│ std        ┆ null          ┆ null       ┆ null                    ┆ 40031.948121 ┆ 3.241238         ┆ null       │
│ min        ┆ Aaron Castro  ┆ CEO        ┆ aaron.castro@polars.io  ┆ 55011.0      ┆ 0.0              ┆ 2014-07-24 │
│ 25%        ┆ null          ┆ null       ┆ null                    ┆ 77675.0      ┆ 2.0              ┆ null       │
│ 50%        ┆ null          ┆ null       ┆ null                    ┆ 96767.0      ┆ 5.0              ┆ null       │
│ 75%        ┆ null          ┆ null       ┆ null                    ┆ 135842.0     ┆ 8.0              ┆ null       │
│ max        ┆ Zachary Woods ┆ Sales      ┆ zachary.woods@polars.io ┆ 250000.0     ┆ 10.0             ┆ 2025-07-16 │
└────────────┴───────────────┴────────────┴─────────────────────────┴──────────────┴──────────────────┴────────────┘
-----------------------
['name', 'department', 'email', 'salary', 'years_at_company', 'start_date']
-----------------------
[String, String, String, Int64, Int64, String]
-----------------------
Schema({'name': String, 'department': String, 'email': String, 'salary': Int64, 'years_at_company': Int64, 'start_date': String})
-----------------------
(1000, 6)
-----------------------
1000
-----------------------
6

"""
