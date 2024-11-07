'''Complete the following data from ice cream sales

Show your work to your teacher for how you did each question

2 points (working on it)

3 points (solved all the parts)

'''

 

import pandas as pd

import numpy as np



# Create a DataFrame with ice cream sales data

np.random.seed(42)

data = {

    'Flavor': ['Vanilla', 'Chocolate', 'Strawberry', 'Mint Chip', 'Cookie Dough'] * 20,

    'Size': np.random.choice(['Small', 'Medium', 'Large'], 100),

    'Price': np.random.uniform(2, 6, 100).round(2),

    'Sales': np.random.randint(10, 100, 100),

    'Date': pd.date_range(start='2023-06-01', periods=100)

}

df = pd.DataFrame(data)

# Display the first few rows of the DataFrame

print(df.head())

# 1. Which flavor has the highest total sales? Use idxmax()
# Hint: Group by flavor and sum the sales
highest = (df.groupby('Flavor')['Sales'].sum()).idxmax()
print(highest)


# 2. What's the average price for each size? Use groupby() and mean()
# Hint: Group by size and calculate the mean price
price = df.groupby('Size')['Price'].mean()
print('price:', price)


# 3. Find the top 3 days with the highest total sales
# Hint: Use groupby(), sum(), sort_values(), and nlargest()
days = ((df.groupby('Date')['Sales'].sum()).sort_values()).nlargest(3)
print('days:', days)


# 4. How many unique flavors are there? Use .unique() and len()
uniqueFlavor = len(df['Flavor'].unique())
print('unique:', uniqueFlavor)

# 5. Create a new DataFrame with only Large size ice creams, sorted by price in descending order
# Hint: Use boolean indexing and sort_values()
mask = df['Size'] == 'Large'
sorts = df[mask].sort_values(by=['Price'], ascending=False)
print('sorted:', sorts)


# 6. (Challenge question - not needed for full points)

#What's the most popular flavor for each size? Use groupby(), sum(), and idxmax()
popular = (df.groupby(['Size', 'Flavor'])['Sales'].sum()).groupby('Size').idxmax()
print('popular:', popular)


# Your code here