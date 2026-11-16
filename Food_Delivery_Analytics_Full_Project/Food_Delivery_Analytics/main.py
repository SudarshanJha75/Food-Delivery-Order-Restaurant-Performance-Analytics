from pathlib import Path
from src.data_pipeline import load_and_clean_data
from src.analysis import create_analysis_outputs

ROOT = Path(__file__).resolve().parent

def main():
    input_file = ROOT / "dataset" / "raw" / "bengaluru_food_delivery_sample.csv"
    output_file = ROOT / "dataset" / "processed" / "cleaned_orders.csv"
    print("FOOD DELIVERY ORDER & RESTAURANT PERFORMANCE ANALYTICS")
    print("Study area: Bengaluru (synthetic demonstration dataset)")
    df = load_and_clean_data(input_file, output_file)
    print(f"Cleaned records: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    create_analysis_outputs(df, ROOT / "reports")
    print("Analysis complete. Check dataset/processed and reports/.")

if __name__ == "__main__":
    main()
