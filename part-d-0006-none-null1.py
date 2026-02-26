sales_by_employee = pl.Series("sales (USD)", [55_000, 42_000, None, 44_000])

print(sales_by_employee)

"""
shape: (4,)
Series: 'sales (USD)' [i64]
[
	55000
	42000
	null
	44000
]

"""
