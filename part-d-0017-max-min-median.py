import polars as pl

def main():

    profit_or_loss = pl.read_csv("proorlo.csv", schema_overrides={"profit_or_loss": pl.Int8}).to_series()

    print(profit_or_loss.max()) # 7

    print(profit_or_loss.min())

    print(profit_or_loss.median())

# 99
# -100
# -3.5

if __name__ == "__main__":
    main()
