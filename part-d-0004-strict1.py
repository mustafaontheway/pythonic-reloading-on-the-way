quarterly_profit_rates = pl.Series(name = "profit rates", values = [12.34, 11.33, 14.24, "17.87"], dtype = pl.Float32, strict = False)

print(quarterly_profit_rates)

"""
shape: (4,)
Series: 'profit rates' [f32]
[
	12.34
	11.33
	14.24
	17.870001
]

"""
