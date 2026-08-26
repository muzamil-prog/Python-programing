total_sales = 0

for employee in range(1, 6):
    sales = float(input(f"Enter sales amount for Employee {employee}: Rs. "))

    # Calculate tax
    if sales < 50000:
        tax_rate = 0.05
    elif sales <= 100000:
        tax_rate = 0.10
    else:
        tax_rate = 0.15

    tax_amount = sales * tax_rate

    print(f"Sales Amount: Rs. {sales:.2f}")
    print(f"Tax Amount: Rs. {tax_amount:.2f}")
    print("-------------------------")

    total_sales += sales

average_sales = total_sales / 5

print("===== Final Result =====")
print(f"Total Sales: Rs. {total_sales:.2f}")
print(f"Average Sales: Rs. {average_sales:.2f}")