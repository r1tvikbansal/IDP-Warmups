import pandas as pd

def summarize_sales(sales: pd.DataFrame) -> pd.DataFrame:
    sales = sales.copy()
    
    filtered = sales[sales['Quantity'] >= 5]
    
    filtered = filtered[filtered['Item'].str.lower() != 'banana']
    
    filtered['Revenue'] = filtered['Quantity'] * filtered['Price']
    
    grouped = filtered.groupby(['Store', 'Item'])

    total_revenue = grouped['Revenue'].sum()
    avg_price = grouped['Price'].mean()
    item_count = grouped['Item'].count()
    
    result = pd.DataFrame({
        'Total Revenue': total_revenue,
        'Average Price': avg_price,
        'Item Count': item_count
    }).reset_index()
    
    result = result.sort_values(['Store', 'Total Revenue'], ascending=[True, False])
    return result

data = {
    'Store': ['A', 'A', 'B', 'B', 'B', 'C', 'C'],
    'Item': ['Apple', 'Banana', 'Apple', 'Banana', 'Carrot', 'Apple', 'Apple'],
    'Quantity': [10, 3, 8, 2, 6, 5, 5],
    'Price': [1.5, 2.0, 1.0, 1.8, 2.5, 1.2, 1.3]
}
sales = pd.DataFrame(data)

result = summarize_sales(sales)
print(result)