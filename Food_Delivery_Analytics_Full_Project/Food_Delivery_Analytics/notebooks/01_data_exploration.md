# Notebook 01 – Data Exploration

Create a Jupyter notebook in this folder and try:

```python
import pandas as pd
df = pd.read_csv("../dataset/raw/bengaluru_food_delivery_sample.csv")
df.head()
df.shape
df.info()
df.describe()
df.isnull().sum()
df["area"].value_counts()
```

Answer in your own words:
1. How many rows and columns are present?
2. Which columns are numeric?
3. Which column contains missing values?
4. Which area has the most sample orders?
5. What does one row represent?
