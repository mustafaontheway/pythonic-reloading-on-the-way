import polars as pl

def main():

    dummy_data = pl.DataFrame({
        
        "names": ["ayhan", "bilge", "kaan", "kutluk", "bumin"],
        "birth_years": [1910, None, 1965, 1997, 1964],
        "isMarried": [True, False, True, None, False]
        }, 
        schema_overrides={"birth_years": pl.UInt16})
    
    print(dummy_data)

if __name__ == "__main__":
    main()

"""
shape: (5, 3)
┌────────┬─────────────┬───────────┐
│ names  ┆ birth_years ┆ isMarried │
│ ---    ┆ ---         ┆ ---       │
│ str    ┆ u16         ┆ bool      │
╞════════╪═════════════╪═══════════╡
│ ayhan  ┆ 1910        ┆ true      │
│ bilge  ┆ null        ┆ false     │
│ kaan   ┆ 1965        ┆ true      │
│ kutluk ┆ 1997        ┆ null      │
│ bumin  ┆ 1964        ┆ false     │
└────────┴─────────────┴───────────┘

"""
