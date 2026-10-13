
print("=" * 50)
print("KERALA FRESH MART".center(50))
print("SMART BILLING".center(50))
print("=" * 50)

customer_name = input("Customer name: ")
item_name = input("Item name: ")
quantity = int(input("Quantity: "))
price_per_unit = float(input("Price per unit (Rs): "))
loyalty_member = input("Loyalty member? (y/n): ").lower()
payment_mode = input("Payment mode (cash/upi/card): ").lower()


amount = quantity * price_per_unit


if amount >= 2000:
    discount_rate = 10
elif amount >= 1000:
    discount_rate = 5
elif amount < 500:
    discount_rate = 2
else:
    discount_rate = 0

discount = amount * discount_rate / 100


if loyalty_member == "y" and amount >= 500:
    bonus = 25
else:
    bonus = 0


taxable_amount = amount - discount - bonus
gst = taxable_amount * 5 / 100
grand_total = taxable_amount + gst


print("-" * 50)
print("Customer:", customer_name)
print("-" * 50)
print(f"{'Item':<20}{'Qty':>5}{'Price':>12}{'Amount':>13}")
print("-" * 50)
print(f"{item_name:<20}{quantity:>5}{price_per_unit:>12,.2f}{amount:>13,.2f}")
print("-" * 50)

print(f"{'Amount:':<30}Rs. {amount:>10,.2f}")
print(f"{'Discount rate:':<30}{discount_rate:>10}%")
print(f"{'Discount:':<30}Rs. {discount:>10,.2f}")
print(f"{'Loyalty bonus:':<30}Rs. {bonus:>10,.2f}")
print(f"{'Taxable amount:':<30}Rs. {taxable_amount:>10,.2f}")
print(f"{'GST (5%):':<30}Rs. {gst:>10,.2f}")
print(f"{'Grand Total:':<30}Rs. {grand_total:>10,.2f}")
print("=" * 50)


if quantity % 12 == 0:
    print("Bonus: Free cloth bag with this order!")


if payment_mode == "cash" and grand_total > 10000:
    print("Cash limit of Rs 10,000 exceeded. Please pay by UPI or card")
elif payment_mode in ["cash", "upi", "card"]:
    print("Payment accepted via", payment_mode.upper())
else:
    print("Invalid payment mode. Bill not settled.")

print("=" * 50)