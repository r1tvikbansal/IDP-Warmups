# Data Aggregation Challenge with Pandas

**Difficulty:** Medium  
**Estimated Time:** 15 minutes  

## Problem Description

You are given a pandas DataFrame named `sales` with the following columns:

- `'Store'`: The name of the store (string)
- `'Item'`: The name of the item sold (string)
- `'Quantity'`: The number of items sold (integer)
- `'Price'`: The price per item in USD (float)

Write a function `summarize_sales(sales: pd.DataFrame) -> pd.DataFrame` that performs the following tasks:

1. Filters out any rows where:
   - `'Quantity'` is less than 5 **or**
   - `'Item'` is `'Banana'` (case-insensitive).
2. Adds a new column `'Revenue'` that calculates the revenue per row as `Quantity * Price`.
3. Groups the data by `'Store'` and `'Item'`.
4. For each group, computes:
   - `'Total Revenue'` as the sum of the `'Revenue'`.
   - `'Average Price'` as the mean of the `'Price'`.
   - `'Item Count'` as the total number of rows in that group.
5. Returns a DataFrame with columns: `'Store'`, `'Item'`, `'Total Revenue'`, `'Average Price'`, and `'Item Count'`.
6. The result should be sorted by `'Store'` in ascending order and then by `'Total Revenue'` in descending order.

## Function Signature

```python
def summarize_sales(sales: pd.DataFrame) -> pd.DataFrame:
```

## Example

```python
import pandas as pd

data = {
    'Store': ['A', 'A', 'B', 'B', 'B', 'C', 'C'],
    'Item': ['Apple', 'Banana', 'Apple', 'Banana', 'Carrot', 'Apple', 'Apple'],
    'Quantity': [10, 3, 8, 2, 6, 5, 5],
    'Price': [1.5, 2.0, 1.0, 1.8, 2.5, 1.2, 1.3]
}
sales = pd.DataFrame(data)

result = summarize_sales(sales)
print(result)
```

## Expected output

```
  Store    Item  Total Revenue  Average Price  Item Count
0     A   Apple           15.0           1.50           1
2     B  Carrot           15.0           2.50           1
1     B   Apple            8.0           1.00           1
3     C   Apple           12.5           1.25           2
```

**Notes:**

Filter 'Banana' rows case-insensitively (e.g., 'Banana', 'banana', 'BANANA' should all be removed).

'Item Count' represents the count of individual rows within each group after filtering.

**Hint:**
Use groupby, agg, and reset_index to structure your solution effectively.