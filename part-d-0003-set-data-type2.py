member_ages = pl.Series(name= "ages", values = [24, 17, 96, 47, 4, 44], dtype = pl.UInt8)

base_years = pl.Series(name = "important_years", values = [2014, 2000, 2017, 1996], dtype = pl.UInt16)

profit_or_loss = pl.Series(name = "P/L last 3 year", values = [550_000, -104_000, 655_000], dtype = pl.Int32)
