from pathlib import Path
import pandas as pd
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "dataset" / "processed" / "cleaned_orders.csv"
MODEL_DIR = ROOT / "models"
MODEL_DIR.mkdir(exist_ok=True)

def main():
    df = pd.read_csv(DATA)
    features = ["distance_km", "traffic", "weather", "vehicle_type"]
    target = "delivery_time_min"
    X, y = df[features], df[target]

    numeric = ["distance_km"]
    categorical = ["traffic", "weather", "vehicle_type"]
    preprocess = ColumnTransformer([
        ("numeric", "passthrough", numeric),
        ("categorical", OneHotEncoder(handle_unknown="ignore"), categorical)
    ])
    model = Pipeline([
        ("preprocess", preprocess),
        ("regressor", RandomForestRegressor(n_estimators=150, random_state=42))
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print("Model evaluation (synthetic data only)")
    print(f"MAE:  {mean_absolute_error(y_test, predictions):.2f} minutes")
    print(f"RMSE: {mean_squared_error(y_test, predictions) ** 0.5:.2f} minutes")
    print(f"R2:   {r2_score(y_test, predictions):.3f}")

    joblib.dump(model, MODEL_DIR / "delivery_time_model.joblib")
    print("Saved model to models/delivery_time_model.joblib")

if __name__ == "__main__":
    main()
