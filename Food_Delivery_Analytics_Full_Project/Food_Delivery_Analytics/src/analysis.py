from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

def create_analysis_outputs(df, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Orders by hour
    hourly = df.groupby("order_hour")["order_id"].count()
    plt.figure(figsize=(9, 5))
    hourly.plot(kind="bar")
    plt.title("Food Delivery Orders by Hour")
    plt.xlabel("Hour of day")
    plt.ylabel("Number of orders")
    plt.tight_layout()
    plt.savefig(output_dir / "orders_by_hour.png", dpi=150)
    plt.close()

    # Revenue by area
    area_revenue = df.groupby("area")["food_revenue"].sum().sort_values(ascending=False)
    plt.figure(figsize=(9, 5))
    sns.barplot(x=area_revenue.values, y=area_revenue.index)
    plt.title("Food Revenue by Bengaluru Area")
    plt.xlabel("Food revenue (INR)")
    plt.ylabel("Area")
    plt.tight_layout()
    plt.savefig(output_dir / "revenue_by_area.png", dpi=150)
    plt.close()

    # Delivery time by traffic
    traffic_time = df.groupby("traffic")["delivery_time_min"].mean().reindex(["Low", "Medium", "High"])
    plt.figure(figsize=(7, 5))
    traffic_time.plot(kind="bar")
    plt.title("Average Delivery Time by Traffic")
    plt.xlabel("Traffic")
    plt.ylabel("Average minutes")
    plt.tight_layout()
    plt.savefig(output_dir / "delivery_time_by_traffic.png", dpi=150)
    plt.close()

def get_kpis(df):
    delivered = df[df["order_status"] == "Delivered"]
    return {
        "orders": int(len(df)),
        "delivered": int(len(delivered)),
        "delivery_rate": float(len(delivered) / len(df) * 100) if len(df) else 0,
        "food_revenue": float(df["food_revenue"].sum()),
        "avg_delivery_time": float(delivered["delivery_time_min"].mean()) if len(delivered) else 0,
        "avg_order_value": float(df["order_amount"].mean()) if len(df) else 0,
    }
