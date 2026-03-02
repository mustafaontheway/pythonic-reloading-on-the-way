import polars as pl

def main():

    profit_or_loss = pl.read_csv("proorlo.csv", schema_overrides={"profit_or_loss": pl.Int8}).to_series()

    print(profit_or_loss.head())

#     shape: (10,)
# Series: 'profit_or_loss' [i8]
# [
#         75
#         81
#         66
#         -32
#         75
#         -38
#         -55
#         17
#         -58
#         -42
# ]


if __name__ == "__main__":
    main()
