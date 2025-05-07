def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if the discount is 20% or higher.

    Parameters:
    - price (float): Original price of the item.
    - discount_percent (float): Discount percentage to apply.

    Returns:
    - float: Final price after applying discount or the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price


# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount)

    if final_price < original_price:
        print(f"Discount applied. Final price: ${final_price:.2f}")
    else:
        print(f"No discount applied. Final price remains: ${original_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for price and discount.")
