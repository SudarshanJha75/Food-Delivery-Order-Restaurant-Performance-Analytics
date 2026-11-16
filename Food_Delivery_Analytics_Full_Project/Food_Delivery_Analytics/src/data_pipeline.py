from pathlib import Path
import pandas as pd

NUMERIC_COLUMNS = [
    "order_hour", "order_amount", "discount", "delivery_fee",
    "distance_km", "restaurant_rating", "delivery_rating", "delivery_time_min"
]

def load_and_clean_data(input_path, output_path):
    # Read the CSV file into a Pandas DataFrame.
    df = pd.read_csv(input_path)

    # Remove duplicate order IDs, keeping the first occurrence.
    df = df.drop_duplicates(subset=["order_id"])

    # Convert date strings to actual datetime values.
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    # Convert numeric fields; invalid values become missing values.
    for column in NUMERIC_COLUMNS:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    # Fill missing ratings with the median rating.
    for column in ["restaurant_rating", "delivery_rating"]:
        df[column] = df[column].fillna(df[column].median())

    # Remove records with essential missing values or impossible values.
    df = df.dropna(subset=["order_id", "order_date", "order_amount", "delivery_time_min"])
    df = df[(df["order_amount"] >= 0) & (df["delivery_time_min"] > 0)]

    # Create revenue after discount; do not subtract delivery fee.
    df["food_revenue"] = (df["order_amount"] - df["discount"]).clip(lower=0)

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    return df
