sales_by_employee = pl.Series("sales (USD)", [55_000, 42_000, 64_000, 44_000], dtype = pl.UInt16)

copy_sales_by_employee = sales_by_employee.alias("sales_amounts")

print(copy_sales_by_employee)

print("-------------------------")

copy_sales_by_employee -= 1500

print("-------------------------")

print(copy_sales_by_employee)

print("-------------------------")

print(sales_by_employee)

"""
shape: (4,)
Series: 'sales_amounts' [u16]
[
	55000
	42000
	64000
	44000
]
-------------------------
shape: (4,)
Series: 'sales_amounts' [u16]
[
	53500
	40500
	62500
	42500
]
-------------------------
shape: (4,)
Series: 'sales (USD)' [u16]
[
	55000
	42000
	64000
	44000
]

"""
