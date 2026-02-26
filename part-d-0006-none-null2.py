sales_by_employee = pl.Series("sales (USD)", [55_000, 42_000, None, 44_000])

premiums = sales_by_employee * 0.08

print(premiums)

"""
shape: (4,)
Series: 'sales (USD)' [f64]
[
	4400.0
	3360.0
	null
	3520.0
]

"""
