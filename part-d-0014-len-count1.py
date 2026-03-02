import polars as pl

def main():

    profit_or_loss = pl.read_csv("proorlo.csv", schema_overrides={"profit_or_loss": pl.Int8}).to_series()

    print(profit_or_loss.len()) # Null values count towards the total

    print(profit_or_loss.count()) # Return the number of non-null elements in the column

    # 507
    # 500


if __name__ == "__main__":
    main()

# python main.py
