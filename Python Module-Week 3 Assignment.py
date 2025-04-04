def calculate_discount(price, discount_percent):
      
  if discount_percent >= 20:
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price
  else:
    return price

try:
  price_str = input("Enter the original price of the item: ")
  price = float(price_str)
  discount_str = input("Enter the discount percentage: ")
  discount_percent = float(discount_str)

  final_price = calculate_discount(price, discount_percent)

  if final_price == price:
    print(f"No discount applied. The final price is: {final_price:.2f}")
  else:
    print(f"The final price after discount is: {final_price:.2f}")

except ValueError:
  print("Invalid input. Please enter numeric values for price and discount percentage.")