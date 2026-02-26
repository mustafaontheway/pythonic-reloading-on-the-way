sales = pl.read_csv("salesdata.csv", schema_overrides = {"amount": pl.UInt16})

print(sales)

"""
shape: (9, 2)
┌──────────┬────────┐
│ name     ┆ amount │
│ ---      ┆ ---    │
│ str      ┆ u16    │
╞══════════╪════════╡
│ ayhan    ┆ 4000   │
│ hakan    ┆ 3000   │
│ bengu    ┆ 4100   │
│ bilge    ┆ 4400   │
│ kutluk   ┆ 4800   │
│ bumin    ┆ 2000   │
│ teoman   ┆ 4980   │
│ atilla   ┆ 4750   │
│ kultigin ┆ 4648   │

"""
