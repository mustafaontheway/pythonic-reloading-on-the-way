import polars as pl

def main():

    interest_rates = pl.read_csv("interests.csv").to_series()

    print(interest_rates.head(5))

    print("-------------------------------------------------")

    floored = interest_rates.floor().cast(pl.Int8)

    print(floored.head(5))

if __name__ == "__main__":
    main()

"""
shape: (5,)
Series: 'rates' [i8]
[
        5
        5
        null
        4
        null
]

"""
