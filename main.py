# Pandas: How to Convert a Pivot Table to a DataFrame

import pandas as pd

df = pd.DataFrame({
    'id': [1, 1, 2, 2, 3, 3],
    'name': ['Alice', 'Alice', 'Bobby', 'Bobby', 'Carl', 'Dan'],
    'experience': [1, 2, 2, 3, 3, 8],
})


table = df.pivot_table(
    index='id',
    columns=['name'],
    values='experience',
    aggfunc='mean',
    fill_value=0
)

new_df = table

new_df.columns.name = None

new_df.reset_index()

print(new_df)