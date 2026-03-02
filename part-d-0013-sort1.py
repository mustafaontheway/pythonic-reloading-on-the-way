import polars as pl

def main():

    profit_or_loss = pl.read_csv("proorlo.csv", schema_overrides={"profit_or_loss": pl.Int8}).to_series()

    profit_or_loss.sort()

    profit_or_loss.sort(descending=False)

    profit_or_loss.sort(descending=True)

if __name__ == "__main__":
    main()
