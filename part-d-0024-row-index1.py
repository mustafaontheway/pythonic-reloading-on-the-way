import polars as pl

def main():

    emps = pl.read_csv("employees.csv").with_row_index()

    print(emps.head(5))

if __name__ == "__main__":
    main()

"""
shape: (5, 7)
┌───────┬────────────────────┬────────────┬──────────────────────────────┬────────┬──────────────────┬────────────┐
│ index ┆ name               ┆ department ┆ email                        ┆ salary ┆ years_at_company ┆ start_date │
│ ---   ┆ ---                ┆ ---        ┆ ---                          ┆ ---    ┆ ---              ┆ ---        │
│ u32   ┆ str                ┆ str        ┆ str                          ┆ i64    ┆ i64              ┆ str        │
╞═══════╪════════════════════╪════════════╪══════════════════════════════╪════════╪══════════════════╪════════════╡
│ 0     ┆ Nicholas Maldonado ┆ CEO        ┆ nicholas.maldonado@polars.io ┆ 250000 ┆ 9                ┆ 2016-07-14 │
│ 1     ┆ Michael Fletcher   ┆ Operations ┆ michael.fletcher@polars.io   ┆ 96540  ┆ 9                ┆ 2016-02-13 │
│ 2     ┆ Jeffrey Tanner     ┆ null       ┆ jeffrey.tanner@polars.io     ┆ 126489 ┆ 10               ┆ 2015-03-01 │
│ 3     ┆ Diana Weaver       ┆ HR         ┆ diana.weaver@polars.io       ┆ 84672  ┆ 5                ┆ 2019-11-25 │
│ 4     ┆ Sierra Ross        ┆ null       ┆ sierra.ross@polars.io        ┆ 148601 ┆ 7                ┆ 2018-02-14 │
└───────┴────────────────────┴────────────┴──────────────────────────────┴────────┴──────────────────┴────────────┘

"""
