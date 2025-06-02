import pandas as pd


def summarize_sales(sales: pd.DataFrame):
    sales = sales.copy()
    mask = ((sales['Quantity'] >= 5) & (sales['Item'] != 'Banana'))
    filtered = sales[mask]
    filtered['Revenue'] = filtered['Quantity'] * filtered['Price']
    store = filtered.groupby('Store')
    item = filtered.groupby('Item')
    rev = store.sum('Revenue')['Revenue']
    price = store.mean('Price')['Price']
    count = store.count('Item')['Item']
    

data = {
    'Store': ['A', 'A', 'B', 'B', 'B', 'C', 'C'],
    'Item': ['Apple', 'Banana', 'Apple', 'Banana', 'Carrot', 'Apple', 'Apple'],
    'Quantity': [10, 3, 8, 2, 6, 5, 5],
    'Price': [1.5, 2.0, 1.0, 1.8, 2.5, 1.2, 1.3]
}
sales = pd.DataFrame(data)

result = summarize_sales(sales)
print(result)