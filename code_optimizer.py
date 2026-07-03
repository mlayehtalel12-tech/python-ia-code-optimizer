from typing import List

def calculate_total_with_tax(item_prices: List[float], tax_rate: float = 0.15) -> float:
    """Calculates the total cost of items including a specified sales tax.

    Args:
        item_prices (List[float]): A list of prices for the individual items.
        tax_rate (float, optional): The sales tax rate to apply. Defaults to 0.15 (15%).

    Returns:
        float: The final total price including tax, rounded to two decimal places.

    Raises:
        ValueError: If any price in the list is negative.
    """
    if any(price < 0 for price in item_prices):
        raise ValueError("Item prices cannot be negative.")
        
    total_base_price = sum(item_prices)
    final_total = total_base_price * (1 + tax_rate)
    
    return round(final_total, 2)
