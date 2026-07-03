# python-ia-code-optimizer
# AI-Powered Python Code Optimizer & Docstring Generator

An advanced prompt-engineering framework designed to automate code review, enforce PEP 8 standards, generate Google-style docstrings, and write comprehensive unit tests using sequential prompt chaining.

## 🚀 Overview
This repository showcases how specialized generative AI prompts can transform raw, unoptimized Python scripts into production-ready code in seconds, cutting documentation and review time by over 70%.

## ⛓️ The Prompt Chain
The workflow utilizes three distinct, specialized system prompts executed in sequence:

1. *Refactoring Prompt*: Reviews code structure, fixes variable naming, and optimizes performance according to PEP 8.
2. *Documentation Prompt*: Appends strict type hinting and injects Google Style docstrings.
3. *Testing Prompt*: Generates isolated unit tests using pytest covering both edge cases and happy paths.

## 📊 Example Transformation

### Before Optimization
def calc(items):
    t = 0
    for i in items:
        t = t + i
    res = t * 1.15
    return res

### After Optimization
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

---
Developed as part of practical applications inspired by the One Million Prompters Initiative.
